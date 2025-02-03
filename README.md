# python-nmap-port_scanner
Scan de Ports avec Nmap et Python
Ce projet implémente un scanner de ports simple en utilisant nmap et Python. Il permet de scanner les 1000 premiers ports d'une cible et de sauvegarder les résultats dans un fichier texte. Le script détecte également les services associés à chaque port, ainsi que leur état et leur version.
Fonctionnalités

    Scan de ports : Scanne les 1000 premiers ports TCP de la cible spécifiée.
    Affichage des résultats : Affiche les résultats dans la console avec des informations sur chaque port détecté (service, état, version).
    Sauvegarde dans un fichier : Enregistre les résultats du scan dans un fichier scan_results.txt.
    Gestion des erreurs : Le script gère les erreurs liées à la connexion et au processus de scan.

Prérequis

    Python 3.x
    Nmap
    Module python-nmap installé

Installation de python-nmap

Pour installer le module Python nécessaire, utilisez la commande suivante :

pip install python-nmap

Installation de Nmap

Si Nmap n'est pas installé sur votre machine, vous pouvez l'installer via :

    Sur Debian/Ubuntu :

    sudo apt install nmap

    Sur Windows/Mac :
    Vous pouvez télécharger et installer Nmap depuis le site officiel.

Utilisation

    Clonez ce repository ou téléchargez le fichier scan.py.
    Exécutez le script Python en utilisant la commande suivante :

    python3 scan.py

    Entrez l'adresse IP cible lorsque le script le demande.
    Le script procédera au scan et affichera les résultats dans la console.
    Un fichier scan_results.txt sera créé dans le répertoire du projet, contenant les résultats détaillés du scan.

Exemple de sortie

Scanning 192.168.1.1 en cours...

✅ Résultats pour 192.168.1.1 :

Port 22 : ssh (open) - Version: OpenSSH 7.2p2
Port 80 : http (open) - Version: Apache 2.4.18
📂 Résultats enregistrés dans 'scan_results.txt'.

Résultats dans le fichier scan_results.txt :

Résultats du scan pour 192.168.1.1 :
Port 22 : ssh (open) - Version: OpenSSH 7.2p2
Port 80 : http (open) - Version: Apache 2.4.18

Gestion des erreurs

Le script prend en charge les erreurs suivantes :

    L'hôte n'est pas accessible.
    Aucun port TCP ouvert détecté.
    Autres erreurs liées au processus de scan.
