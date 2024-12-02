from netmiko import ConnectHandler

def main():
    # Configuration de la connexion au routeur
    cisco_router = {
        'device_type': 'cisco_ios',
        'host': 'sandbox-iosxe-latest-1.cisco.com',
        'username': 'admin',
        'password': 'C1sco12345',
        'port': 22,
    }

    try:
        # Connexion au routeur
        print("Connexion au routeur...")
        net_connect = ConnectHandler(**cisco_router)
        
        # Afficher la date côté routeur
        print("Récupération de la date...")
        show_clock = net_connect.send_command("show clock")
        print("Date du routeur:")
        print(show_clock)



        # Afficher les interfaces dans un fichier
        print("Récupération des interfaces...")
        interfaces_output = net_connect.send_command("show ip interface brief")
        with open("interfaces.txt", "w") as file:
            file.write(interfaces_output)
        print("Informations sur les interfaces sauvegardées dans 'interfaces.txt'.")

        # Configurer une interface loopback
        print("Configuration de l'interface Loopback...")
        config_commands = [
            "interface Loopback0",
            "ip address 10.8.8.8 255.255.255.240",
            "no shutdown"
        ]
        net_connect.send_config_set(config_commands)
        print("Interface Loopback configurée avec succès.")

        # Déconnexion
        net_connect.disconnect()
        print("Déconnexion du routeur.")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
