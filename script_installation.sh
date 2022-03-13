#!/usr/bin/bash
# coding: utf-8
#script décrivant la suite des cmd pour lancer le main.py de SMS/AirMore
sudo apt-get install -y python3.9 git python3-pip
mkdir ~/Sms
cd Sms
# copier les fichiers de github dans un répertoire Sms
# aller dans le répertoire y lancer cmder
python3.9 -m venv .venv
#Il faut que le nom de dossier soit .venv Ce dossier représente l environnement virtuel.
source ~/Sms/.venv/bin/activate
#tu vas avoir un "venv" devant ton invite cela signifie que l environnement virtuel est activé
pip install -r requirements.txt
#va charger les bibliothèques
git clone https://github.com/Alain-f5gfe/py-test-code
# copie tous les fichiers dans le répertoire Sms
python.pythonPath: $"{Sms}~/Sms/.venv/bin/python"
# va ajouter venv au path
python main.py

