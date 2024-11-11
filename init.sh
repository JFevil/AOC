#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage : ./init day year"
    exit 1
fi

day=$1
annee=$2
url="https://adventofcode.com/$annee/day/$day/input"
destination="./$annee/$day/input.txt"
cookie="session=53616c7465645f5f694bcddb7db208b66bfa129100b26cc80feec03e83d4d06003b55c7a15bceae1d393b206fc28557b043c7d9b05c0fd8520b9938d24d09bf8"

# Vérification et création du répertoire pour l'année
if [ ! -d "./$annee" ]; then 
    mkdir "$annee"
    echo "Création du répertoire $annee"
fi

# Vérification et création du sous-répertoire pour le jour
if [ ! -d "./$annee/$day" ]; then 
    mkdir "$annee/$day"
    echo "Création du répertoire $annee/$day"
fi

fichier="./$annee/$day/$day.py"
# Vérification et création du fichier Python pour le jour
if [ ! -f $fichier ]; then
    touch $fichier
    chmod u+x $fichier
    echo "Création du fichier $fichier"
    echo "with open(\"input.txt\") as f:" > $fichier
    echo "	texte = f.read()" >> $fichier
fi

if [ ! -f $destination ]; then
	if ! wget --header="Cookie: $cookie" --tries=3 --timeout=10 -q -O "$destination" "$url"; then
	    echo "Erreur : Le téléchargement a échoué après 3 tentatives."
	    echo "URL : $url"
	    echo "Peut-être qu'il n'y a juste pas d'input aujourd'hui !"
	    exit 1
	else
	    echo "Téléchargement de input.txt réussi."
	fi
fi

subl ./$annee/$day &