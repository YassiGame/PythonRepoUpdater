# 🚀 Script de Mise à Jour Automatique du Code

Ce script Python permet de télécharger automatiquement la dernière version d'un dépôt GitHub, de mettre à jour votre code local, de copier le contenu d'un dossier supplémentaire vers le répertoire racine de votre code, et d'exécuter le code mis à jour.

## 📝 Fonctionnalités

- 📥 **Téléchargement automatique** de la dernière version du dépôt GitHub spécifié.
- 🔄 **Mise à jour du code** local en écrasant les fichiers existants si nécessaire.
- 📁 **Copie du contenu** d'un dossier supplémentaire vers le répertoire racine du code.
- 🚀 **Exécution automatique** du code après la mise à jour.

## 📦 Installation

1. **Clonez** ce dépôt ou téléchargez les fichiers `update_script.py`, `config.yaml`, et `.gitignore`.

2. **Installez** les dépendances nécessaires :

```bash
pip install requests pyyaml
```

## ⚙️ Configuration

Modifiez le fichier `config.yaml` avec les paramètres appropriés :

```yaml
repo_url: 'https://github.com/utilisateur/nom_du_depot'  # URL de votre dépôt GitHub
branch: 'main'  # Branche du dépôt à télécharger
target_path: '/chemin/vers/votre/code'  # Chemin où le code doit être mis à jour
overwrite: true  # Écraser les fichiers existants (true/false)
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
- Si vous utilisez une version antérieure, remplacez les appels à `shutil.copytree` avec `dirs_exist_ok` par une fonction de copie personnalisée (voir le code pour les détails).

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📞 Support

Pour toute question ou assistance supplémentaire, n'hésitez pas à me contacter.


---

**Remarques supplémentaires :**

- **Dépendances :** Le script utilise les modules `requests` et `pyyaml`. Assurez-vous de les installer en exécutant :

  ```bash
  pip install requests pyyaml
  ```

- **Fichier `.gitignore` :** Le fichier `.gitignore` est configuré pour ignorer les fichiers temporaires, les environnements virtuels, les fichiers compilés, les logs, et le fichier `config.yaml` si vous utilisez un système de contrôle de version comme Git.

- **Sécurité :**
  - **Prudence lors de l'exécution automatique du code :** Assurez-vous que le code téléchargé est fiable avant de l'exécuter automatiquement.
  - **Gestion des informations sensibles :** Évitez de stocker des informations sensibles dans le fichier `config.yaml`. Si nécessaire, utilisez des variables d'environnement ou un gestionnaire de secrets.

- **Gestion des versions antérieures à Python 3.8 :**

  Si vous utilisez une version de Python antérieure à 3.8, remplacez les appels à `shutil.copytree` par la fonction suivante :

  ```python
  def copy_directory(src, dest, overwrite):
      if os.path.exists(dest) and overwrite:
          shutil.rmtree(dest)
      shutil.copytree(src, dest)

  # Dans les boucles de copie, remplacez :
  if os.path.isdir(s):
      copy_directory(s, d, overwrite)
  else:
      if os.path.exists(d) and not overwrite:
          continue
      shutil.copy2(s, d)
  ```