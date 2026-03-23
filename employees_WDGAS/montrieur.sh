#!/bin/bash

# Dossier source
BASE_DIR="/home/youssef.hirchaou@Digital-Grenoble.local/campus/Lunix/employees_WDGAS/"

# Se placer dans le dossier
cd "$BASE_DIR" || exit

# Parcourir tous les fichiers
for file in *; do
    if [ -f "$file" ]; then
        
        # Extraire nom sans extension
        name="${file%.*}"
        ext="${file##*.}"

        # Découper avec "_"
        IFS="_" read -r prenom nom dept <<< "$name"

        # Vérifier département
        if [[ "$dept" == "BU" || "$dept" == "HR" || "$dept" == "IT" ]]; then
            
            # Créer dossier si besoin
            mkdir -p "$dept"

            # Nouveau nom
            new_name="$(echo "${nom}_${prenom}.data" | tr 'A-Z' 'a-z')"

            # Déplacer + renommer
            mv "$file" "$dept/$new_name"

            echo "$file → $dept/$new_name"
        fi
    fi
done
