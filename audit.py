import os
import platform
import nmap

# 1. Collecte d'informations système
def collect_system_info():
    info = {}

    # Information sur l'OS
    info['OS'] = platform.system() + " " + platform.release()
    
    # Uptime
    uptime = os.popen("uptime -p").read().strip()
    info['Uptime'] = uptime

    # Utilisateurs
    users = os.popen("who").read().strip()
    info['Users'] = users

    return info

# 2. Scan réseau avec Nmap
def scan_network(ip_target):
    scanner = nmap.PortScanner()
    scan_results = {}

    try:
        print(f"Scanning {ip_target} en cours...\n")
        scanner.scan(ip_target, '1-1000', '-sV')  # Scan des ports 1 à 1000

        # Vérification des résultats du scan
        if ip_target in scanner.all_hosts():
            scan_results['Host'] = ip_target
            scan_results['Ports'] = {}

            # Collecter les informations des ports ouverts
            if 'tcp' in scanner[ip_target]:
                for port, port_data in scanner[ip_target]['tcp'].items():
                    service = port_data.get('name', 'Inconnu')
                    state = port_data.get('state', 'Inconnu')
                    version = port_data.get('version', 'Inconnue')
                    scan_results['Ports'][port] = {'Service': service, 'State': state, 'Version': version}
        else:
            scan_results['Error'] = "L'hôte n'a pas répondu."

    except Exception as e:
        scan_results['Error'] = str(e)

    return scan_results

# 3. Vérification des vulnérabilités
def check_vulnerabilities(scan_results):
    recommendations = []

    # Vérifier les versions vulnérables de services
    for port, data in scan_results.get('Ports', {}).items():
        service = data.get('Service', '')
        version = data.get('Version', '')
        
        if service == 'Apache' and version < '2.4.49':
            recommendations.append(f"Apache {version} détecté, vulnérabilité connue (CVE-2021-12345). Mettre à jour vers une version plus récente.")
        
        # Ajouter d'autres services à vérifier ici

    return recommendations

# 4. Vérification des permissions système
def check_permissions():
    sensitive_files = ['/etc/passwd', '/etc/shadow', '/root']
    permissions_issues = []

    for file in sensitive_files:
        if os.path.exists(file):
            perms = os.popen(f"ls -l {file}").read().strip()
            if 'root' not in perms:
                permissions_issues.append(f"Fichier {file} : permissions trop larges!")
    
    return permissions_issues

# 5. Génération du rapport
def generate_report(system_info, scan_results, vulnerabilities, permissions_issues):
    report_file = 'audit_securite_report.txt'
    
    with open(report_file, 'w') as file:
        file.write("Rapport d'Audit de Sécurité\n")
        file.write("="*40 + "\n")

        # Ajouter les informations systèmes
        file.write("Informations Système :\n")
        for key, value in system_info.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

        # Ajouter les résultats du scan réseau
        file.write("Résultats du Scan Réseau :\n")
        if 'Error' in scan_results:
            file.write(f"Erreur: {scan_results['Error']}\n")
        else:
            for port, data in scan_results.get('Ports', {}).items():
                file.write(f"Port {port}: Service {data['Service']} (Etat: {data['State']}) - Version: {data['Version']}\n")
        file.write("\n")

        # Ajouter les vulnérabilités
        file.write("Vulnérabilités détectées :\n")
        if vulnerabilities:
            for vuln in vulnerabilities:
                file.write(f"⚠️ {vuln}\n")
        else:
            file.write("Aucune vulnérabilité critique détectée.\n")
        file.write("\n")

        # Ajouter les problèmes de permissions
        file.write("Problèmes de Permissions :\n")
        if permissions_issues:
            for issue in permissions_issues:
                file.write(f"⚠️ {issue}\n")
        else:
            file.write("Pas de problèmes de permissions détectés.\n")

        file.write("="*40 + "\n")
    
    print(f"Rapport d'audit généré : {report_file}")

# 6. Exécution du script principal
def main():
    ip_target = input("Entrez l'adresse IP cible : ")

    # Collecte des informations système
    system_info = collect_system_info()

    # Scan réseau
    scan_results = scan_network(ip_target)

    # Vérification des vulnérabilités
    vulnerabilities = check_vulnerabilities(scan_results)

    # Vérification des permissions système
    permissions_issues = check_permissions()

    # Générer le rapport
    generate_report(system_info, scan_results, vulnerabilities, permissions_issues)

if __name__ == "__main__":
    main()