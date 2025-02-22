# Audit de Sécurité Réseau et Système

Ce script Python réalise un audit de sécurité sur une machine cible en analysant les services réseau ouverts et en identifiant les éventuelles vulnérabilités connues.

## 🔍 Fonctionnalités
- **Scan des ports ouverts** avec `nmap`
- **Identification des services et versions**
- **Détection des vulnérabilités connues** (via une base de données JSON)
- **Analyse des permissions critiques sur le système**
- **Génération automatique d'un rapport d'audit**

## 🚀 Installation
### Prérequis
- Python 3
- `nmap` installé sur votre machine (`sudo apt install nmap` sous Linux)
- Bibliothèques Python nécessaires :
  ```bash
  pip install python-nmap
  ```

### Cloner le dépôt
```bash
git clone https://github.com/DimitriNGAPGUE/Audit_de_Securite.git
```

## 🔧 Utilisation
Exécutez le script avec `sudo` pour avoir les permissions nécessaires :
```bash
sudo python3 audit.py
```
Saisissez l'adresse IP cible lorsque le script le demande.

### Exemple de sortie
```
Entrez l'adresse IP cible : 192.168.1.54
Scanning 192.168.1.54 en cours...

Rapport d'audit généré : audit_securite_report.txt
```

## 📄 Structure du Projet
```
📂 audit-securite
├── audit.py               # Script principal
├── vuln_db.json           # Base de données des vulnérabilités connues
├── README.md              # Documentation
├── requirements.txt       # Liste des dépendances
└── scan_results/          # Dossier contenant les rapports générés
```

## 📌 Améliorations possibles
- Intégrer `nmap --script vuln` pour une détection automatique des CVE
- Ajouter un export JSON du rapport d’audit
- Automatiser l’envoi du rapport par e-mail

## 🛠 Auteur
- **Dimitri** – [GitHub](https://https://github.com/DimitriNGAPGUE)

N’hésitez pas à contribuer ! 🚀

