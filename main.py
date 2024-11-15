import os
import requests
import zipfile
import shutil
import subprocess
import sys
import yaml

def copy_with_overwrite(src, dest):
    """
    Copie récursivement les fichiers de src vers dest, en écrasant les fichiers existants,
    sans supprimer les fichiers dans dest qui ne sont pas présents dans src.
    """
    if os.path.isdir(src):
        if not os.path.exists(dest):
            os.makedirs(dest)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            copy_with_overwrite(s, d)
    else:
        # Copier le fichier en écrasant s'il existe déjà
        shutil.copy2(src, dest)

def update_code(config):
    """
    Met à jour le code en fonction des paramètres du fichier de configuration.
    Installe les dépendances pip du dépôt avant d'exécuter le code.
    Exécute le code en définissant le répertoire courant comme le dossier racine du code.
    """
    repo_url = config['repo_url']
    target_path = config['target_path']
    additional_folder = config.get('additional_folder')
    run_after_update = config.get('run_after_update', False)
    script_to_run = config.get('script_to_run', 'main.py')
    branch = config.get('branch', 'main')

    # Nettoyer l'URL du dépôt
    if repo_url.endswith('/'):
        repo_url = repo_url[:-1]
    if repo_url.endswith('.git'):
        repo_url = repo_url[:-4]

    # Construire l'URL de téléchargement du zip
    download_url = f"{repo_url}/archive/refs/heads/{branch}.zip"

    # Télécharger le fichier zip
    print("📥 Téléchargement de la dernière version du code...")
    response = requests.get(download_url)
    if response.status_code != 200:
        print(f"❌ Échec du téléchargement du dépôt: {response.status_code}")
        return

    zip_filename = 'latest_code.zip'
    with open(zip_filename, 'wb') as f:
        f.write(response.content)

    # Extraire le fichier zip dans un répertoire temporaire
    temp_dir = 'temp_code'
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # Obtenir le dossier racine à l'intérieur du zip
    root_folder = os.listdir(temp_dir)[0]
    code_path = os.path.join(temp_dir, root_folder)

    # Copier les fichiers vers le répertoire cible en utilisant copy_with_overwrite
    print("🔄 Mise à jour du code...")
    copy_with_overwrite(code_path, target_path)

    # Copier le contenu d'un dossier supplémentaire vers le code root
    if additional_folder:
        print("📁 Copie du contenu du dossier supplémentaire vers le code root...")
        copy_with_overwrite(additional_folder, target_path)

    # Nettoyer les fichiers temporaires
    os.remove(zip_filename)
    shutil.rmtree(temp_dir)
    print("✅ Mise à jour du code terminée.")

    # Installer les dépendances pip si requirements.txt existe
    requirements_path = os.path.join(target_path, 'requirements.txt')
    if os.path.exists(requirements_path):
        print("📦 Installation des dépendances pip...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])

    # Exécuter le code si demandé
    if run_after_update:
        print("🚀 Exécution du code...")
        script_path = os.path.join(target_path, script_to_run)
        if os.path.exists(script_path):
            # Changer le répertoire courant vers le répertoire cible
            os.chdir(target_path)
            # Exécuter le script
            subprocess.run([sys.executable, script_to_run])
        else:
            print(f"❌ Le script {script_to_run} n'existe pas dans le répertoire cible.")

if __name__ == '__main__':
    # Charger la configuration depuis le fichier YAML
    config_file = 'config.yaml'
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    update_code(config)
