import os
import shutil

# Dossier source
base_dir = "/home/youssef.hirchaou@Digital-Grenoble.local/campus/Lunix/employees_WDGAS/"

# Parcourir les fichiers
for filename in os.listdir(base_dir):
    file_path = os.path.join(base_dir, filename)

    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)
        parts = name.split("_")

        # Vérification du format
        if len(parts) == 3:
            prenom, nom, departement = parts

            # Vérifier département valide
            if departement in ["BU", "HR", "IT"]:

                # Créer dossier si inexistant
                dept_dir = os.path.join(base_dir, departement)
                os.makedirs(dept_dir, exist_ok=True)

                # Nouveau nom : nom_prenom.data
                new_filename = f"{nom.lower()}_{prenom.lower()}.data"
                new_path = os.path.join(dept_dir, new_filename)

                # Déplacer + renommer
                shutil.move(file_path, new_path)

                print(f"{filename} → {departement}/{new_filename}")
