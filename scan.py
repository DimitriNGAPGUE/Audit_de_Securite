import nmap

scanner = nmap.PortScanner()

ip_target = input("Entrez l'adresse IP cible : ") # Demande à l'utilisateur d'entrer l'adresse IP cible

print(f"Scanning {ip_target} en cours...\n") # Message à l'écran pour demander ç l'utilisateur de patienter

try:
    scanner.scan(ip_target, '1-1000', '-sV')

    # Vérifier si l'hôte a répondu
    if ip_target in scanner.all_hosts():
        print(f"\n✅ Résultats pour {ip_target} :")

        # Ouvrir un fichier pour sauvegarder les résultats
        with open("scan_results.txt", "w") as file:
            file.write(f"Résultats du scan pour {ip_target} :\n")

            # Vérifier si des ports TCP sont ouverts
            if 'tcp' in scanner[ip_target]:
                for port, port_data in scanner[ip_target]['tcp'].items():
                    service = port_data.get('name', 'Inconnu')
                    state = port_data.get('state', 'Inconnu')
                    version = port_data.get('version', 'Inconnue')

                    result_line = f"Port {port} : {service} ({state}) - Version: {version}"
                    print(result_line)
                    file.write(result_line + "\n")

                print("\n📂 Résultats enregistrés dans 'scan_results.txt'.")

            else:
                print("❌ Aucun port TCP ouvert détecté.")
                file.write("Aucun port TCP ouvert détecté.\n")

    else:
        print("❌ L'hôte n'a pas répondu ou n'est pas accessible.")

except Exception as e:
    print(f"⚠️ Erreur lors du scan : {e}")
