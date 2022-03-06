#!~/Sms_read_send/.venv/bin/python3.9
# transfert message SMS via un smartphone equipe de AirMore
import sys
import json
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from pathlib import Path

ip = IPv4Address("192.168.1.24")  # Ip du smartphone sur le lan au format IPv4
session = AirmoreSession(ip)
services = MessagingService(session)


def lire_sms():
    """ fonction qui lit tous les sms présent sur le smartphone"""
    messages = services.fetch_message_history()  # messages contient tous les messages.
    for message in messages:
        tel = message.phone
        if message:
            home = Path.home()
            sms_recu = home /"Bureau"/"Sms_reçu.txt"
            sms_recu.touch()
            chat_messages = services.fetch_chat_history(message, 0, 100)
            chat_messages.reverse()
            indicatif = f"\n####### message envoyé par le teléphone N° {tel}. #######\n"
            a = 0
            print(indicatif)
            with open(sms_recu, "a") as f:
                f.write(indicatif)
                f.write("\n")
                for obj in chat_messages:
                    texte = chat_messages[a].content
                    print(texte)
                    f.write(texte)
                    f.write("\n")
                    a = a+1



def filtre_numero_tel(tel_filtre):
    """ Fonction qui envoie un ACK à la présence du signe "_" dans les sms du n° de tel prédéfinit"""
    messages = services.fetch_message_history()
    message = next(m for m in messages if m.phone == tel_filtre)
    for mot in message.content:
        print(mot)
        if mot == "_":
            ntel = tel_filtre
            print(ntel)
            textsms = "ACK: Ceci est une réponse automatique à votre sms"
            envoie_sms(ntel, textsms)
            print("un ACK à été envoyé au " + tel_filtre)
            sys.exit()


def envoie_sms(ntel, textsms):
    """ fonction qui envoie un sms à n°tel contenant textsms """
    try:
        services.send_message(ntel, textsms)
        print("Le message à été envoyé")
        sys.exit()
    except:
        print("le message n'ai pas parti!")


def envoie_multiple():
    """ Envoie à tous les correspondants du fichier rep_tel.json"""
    fichier = "rep_tel.json"
    with open(fichier, "r") as f:
        repertoir = json.load(f)
        print(repertoir)
        for key, ntel in repertoir.items():
            print(repertoir.get(key))
            ntel = repertoir.get(key)
            textsms = f"Bonjour {key} je te confirme que cela fonctionne A+ Alain"
            print(f"Bonjour {key} je te confirme que cela fonctionne A+ Alain")
            # envoie_sms(ntel, textsms)


print("Si vous invalidé l'une des 2 premières entrées vous passez en mode lecture\n"
      "En répondant O en ligne 3 vous envoyer un sms à tout le carnet d'adresse\n"
      "en entrant le N° tel à la 4me entrée vous créer une réponse automatique si\n"
      "un sms de ce correspondant contient un tiret bas\n" )
ntel = input("Entré le n° de tel de votre correspondant au format +336******** : ")
textsms = input("Entré le texte de votre message : ")
multi = input("Voulez vous envoyer un message au carnet d'adresses ? O/N  ")
tel_filtre = input("Entré le N° auquel vous voulez répondre en automatique : ")


if ntel == "" or textsms == "":
    lire_sms()
else:
    print(ntel, textsms)
    envoie_sms(ntel, textsms)

if multi == "O":
    envoie_multiple()

while True:
    if tel_filtre != "":
        filtre_numero_tel(tel_filtre)
    else:
        sys.exit()
