# 🐍 Python - 🚀 Repo Updater

Ce script Python permet de télécharger automatiquement la dernière version **d'un dépôt GitHub**, de mettre à jour votre code local, de copier le contenu d'un dossier supplémentaire vers le répertoire racine de votre code, et d'exécuter le code mis à jour.

## 📝 Fonctionnalités

- 📥 **Téléchargement automatique** de la dernière version du dépôt GitHub spécifié.
- 🔄 **Mise à jour du code** local en écrasant les fichiers existants si nécessaire.
- 📁 **Copie du dossier supplémentaire** Le script copie le contenu du dossier supplémentaire vers le répertoire cible en **remplaçant uniquement les fichiers existants ou en ajoutant de nouveaux fichiers**, sans supprimer les fichiers qui existent déjà dans le répertoire cible mais qui ne sont pas dans le dossier supplémentaire. Cela permet, par exemple, de mettre à jour ou de remplacer des fichiers de configuration spécifiques sans affecter les autres fichiers du projet.
- 🚀 **Exécution automatique** du code après la mise à jour.

## 📦 Installation

1. **Clonez** ce dépôt ou (téléchargez)[https://github.com/YassiGame/PythonRepoUpdater/archive/refs/heads/main.zip] les fichiers `update_script.py`, `config.yaml`, et `requirements.txt`.
2. **Installez** les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Modifiez le fichier `config.yaml` avec les paramètres appropriés :

```yaml
repo_url: 'https://github.com/utilisateur/nom_du_depot'  # URL de votre dépôt GitHub
branch: 'main'  # Branche du dépôt à télécharger
target_path: '/chemin/vers/votre/code'  # Chemin où le code doit être mis à jour
additional_folder: '/chemin/vers/dossier/supplementaire'  # Chemin vers le dossier à copier (ou null)
run_after_update: true  # Exécuter le code après la mise à jour (true/false)
script_to_run: 'main.py'  # Script à exécuter après la mise à jour
```

## ▶️ Utilisation

Exécutez le script de mise à jour :

```bash
python update_script.py
```

## 🛠️ Personnalisation

- **Branche du dépôt :** Changez la valeur de `branch` dans `config.yaml` pour télécharger une autre branche.
- **Script à exécuter :** Modifiez `script_to_run` pour exécuter un script spécifique après la mise à jour.
- **Dossier supplémentaire :** Spécifiez un dossier dans `additional_folder` pour copier son contenu vers le répertoire racine du code.

## ❗ Remarques

- Assurez-vous d'avoir les **permissions nécessaires** pour écrire dans le répertoire cible et exécuter les scripts.
- Si le dépôt est **privé**, une authentification supplémentaire sera nécessaire.
- Le script suppose que la structure du dépôt correspond à celle attendue (par exemple, le script à exécuter existe).

## 🐍 Compatibilité

- Le script est compatible avec **Python 3.8** et supérieur.
- Si vous utilisez une version antérieure, remplacez les appels à `shutil.copytree` avec `dirs_exist_ok` par une fonction de copie personnalisée (voir le [code](main.py) pour les détails).

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📞 Support

Pour toute question ou assistance supplémentaire, n'hésitez pas à me contacter.
