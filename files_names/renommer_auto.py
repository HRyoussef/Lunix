import os

# Répertoire contenant les fichiers
folder = "/home/youssef.hirchaou@Digital-Grenoble.local/campus/Lunix/files_names/"

# Lister tous les fichiers dans le dossier
for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)
    
    # Ignorer les dossiers
    if os.path.isdir(old_path):
        continue
    
    # Stratégie de renommage :
    # - tout en minuscules
    # - remplacer les espaces par des underscores
    new_name = filename.lower().replace(" ", "_")
    
    new_path = os.path.join(folder, new_name)
    
    # Renommer le fichier seulement si le nom change
    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"{filename} → {new_name}")

print("Renommage terminé.")
