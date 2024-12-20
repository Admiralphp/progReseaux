
# Examen Pratique - Programmation Réseaux

Ce projet est un script Python qui utilise la bibliothèque Netmiko pour se connecter à un routeur Cisco, exécuter des commandes pour récupérer des informations, configurer une interface loopback, et enregistrer des données dans un fichier.

## Prérequis

Avant d'exécuter le script, assurez-vous de disposer des éléments suivants :

- **Python** : Version 3.6 ou supérieure.
- **Netmiko** : Installé via pip (instructions ci-dessous).
- **Connexion Internet** : Nécessaire pour accéder au routeur sandbox Cisco.

## Configuration

Les paramètres suivants sont utilisés pour se connecter au routeur :

- **Hôte** : `sandbox-iosxe-latest-1.cisco.com`
- **Port SSH** : `22`
- **Utilisateur** : `admin`
- **Mot de passe** : `C1sco12345`

## Installation

1. **Cloner le dépôt ou télécharger les fichiers** :
   ```bash
   git clone https://github.com/Admiralphp/progReseaux.git
   cd progReseaux
   ```

2. **Installer les dépendances** :
   Assurez-vous que la bibliothèque Netmiko est installée :
   ```bash
   pip install netmiko
   ```

3. **Vérifiez que vous avez Python installé** :
   ```bash
   python --version
   ```

## Fonctionnalités

Le script réalise les tâches suivantes :

1. **Connexion au routeur** :
   - Se connecte au routeur sandbox Cisco en utilisant les paramètres fournis.

2. **Afficher la date côté routeur** :
   - Exécute la commande `show clock` et affiche la date actuelle sur le routeur.

3. **Sauvegarder les informations des interfaces** :
   - Exécute la commande `show ip interface brief` et sauvegarde le résultat dans un fichier `interfaces.txt`.

4. **Configurer une interface Loopback** :
   - Crée une interface `Loopback0` avec l'adresse IP `10.8.8.8/28`.

5. **Déconnexion** :
   - Ferme proprement la connexion au routeur.

## Utilisation

1. **Exécutez le script Python** :
   ```bash
   python <nom_du_script>.py
   ```

2. **Résultats attendus** :
   - La date actuelle du routeur est affichée dans la console.
   - Les informations des interfaces sont sauvegardées dans le fichier `interfaces.txt`.
   - L'interface Loopback est configurée avec succès.

3. **Vérifiez le fichier `interfaces.txt`** :
   - Vous y trouverez les informations sur les interfaces réseau du routeur.

## Exemple de Sortie

### Console

```
Connexion au routeur...
Récupération de la date...
Date du routeur:
*09:39:19.916 UTC Mon Dec 2 2024
Récupération des interfaces...
Informations sur les interfaces sauvegardées dans 'interfaces.txt'.
Configuration de l'interface Loopback...
Interface Loopback configurée avec succès.
Déconnexion du routeur.

```

### Contenu de `interfaces.txt`
```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      
GigabitEthernet2       28.168.1.2      YES manual administratively down down    
GigabitEthernet3       192.168.22.22   YES manual up                    up      
Loopback0              10.8.8.8        YES manual up                    up      
Loopback1              2.2.2.2         YES manual up                    up      
Loopback2              unassigned      YES unset  up                    up      
Loopback5              unassigned      YES unset  up                    up      
Loopback8              unassigned      YES unset  up                    up      
Loopback10             unassigned      YES unset  up                    up      
Loopback40             40.40.40.40     YES other  up                    up      
Loopback99             99.99.99.99     YES other  up                    up      
Loopback100            10.10.10.10     YES other  up                    up      
Loopback143            192.168.64.143  YES other  up                    up      
Loopback148            148.148.148.148 YES other  up                    up      
Loopback158            unassigned      YES unset  up                    up      
Loopback888            172.16.100.1    YES other  up                    up      
Loopback999            unassigned      YES unset  up                    up      
Loopback3982           12.23.34.46     YES other  up                    up      
Loopback9875           192.168.98.75   YES other  up                    up      
Loopback9876           192.168.98.76   YES other  up                    up      
Loopback10041          10.0.10.41      YES other  up                    up      
VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up      
Vlan1                  10.10.1.1       YES manual up                    down    
Vlan2                  10.10.2.1       YES manual down                  down    
Vlan3                  192.168.3.7     YES manual down                  down    
Vlan4                  192.168.4.7     YES manual down                  down    
Vlan5                  192.168.5.7     YES manual down                  down    
Vlan6                  192.168.6.7     YES manual down                  down    
Vlan7                  10.10.7.1       YES manual down                  down    
Vlan8                  10.10.8.1       YES manual down                  down    
Vlan9                  10.10.9.1       YES manual down                  down    
Vlan10                 unassigned      YES unset  down                  down    
Vlan11                 10.10.11.1      YES manual down                  down    
Vlan12                 10.10.12.1      YES manual down                  down    
Vlan13                 10.10.13.1      YES manual down                  down    
Vlan14                 10.10.14.1      YES manual down                  down    
Vlan15                 10.10.15.1      YES manual down                  down    
Vlan16                 10.10.16.1      YES manual down                  down    
Vlan17                 10.10.17.1      YES manual down                  down    
Vlan18                 10.10.18.1      YES manual down                  down    
Vlan19                 10.10.19.1      YES manual down                  down    
Vlan20                 unassigned      YES unset  down                  down    
Vlan21                 10.10.21.1      YES manual down                  down    
Vlan22                 10.10.22.1      YES manual down                  down    
Vlan23                 10.10.23.1      YES manual down                  down    
Vlan24                 10.10.24.1      YES manual down                  down    
Vlan25                 10.10.25.1      YES manual down                  down    
Vlan26                 10.10.26.1      YES manual down                  down    
Vlan27                 10.10.27.1      YES manual down                  down    
Vlan28                 10.10.28.1      YES manual down                  down    
Vlan29                 10.10.29.1      YES manual down                  down    
Vlan30                 10.10.30.1      YES manual down                  down    
Vlan31                 10.10.31.1      YES manual down                  down    
Vlan32                 10.10.32.1      YES manual down                  down    
Vlan33                 10.10.33.1      YES manual down                  down    
Vlan34                 10.10.34.1      YES manual down                  down    
Vlan35                 10.10.35.1      YES manual down                  down    
Vlan36                 10.10.36.1      YES manual down                  down    
Vlan37                 10.10.37.1      YES manual down                  down    
Vlan38                 10.10.38.1      YES manual down                  down    
Vlan39                 10.10.39.1      YES manual down                  down    
Vlan40                 10.10.40.1      YES manual down                  down    
Vlan41                 10.10.41.1      YES manual down                  down    
Vlan42                 10.10.42.1      YES manual down                  down    
Vlan43                 10.10.43.1      YES manual down                  down    
Vlan44                 10.10.44.1      YES manual down                  down    
Vlan45                 10.10.45.1      YES manual down                  down    
Vlan46                 10.10.46.1      YES manual down                  down    
Vlan47                 10.10.47.1      YES manual down                  down    
Vlan48                 10.10.48.1      YES manual down                  down    
Vlan49                 10.10.49.1      YES manual down                  down    
Vlan50                 10.10.50.1      YES manual down                  down    
Vlan51                 10.10.51.1      YES manual down                  down    
Vlan52                 10.10.52.1      YES manual down                  down    
Vlan53                 10.10.53.1      YES manual down                  down    
Vlan54                 10.10.54.1      YES manual down                  down    
Vlan55                 10.10.55.1      YES manual down                  down    
Vlan56                 10.10.56.1      YES manual down                  down    
Vlan57                 10.10.57.1      YES manual down                  down    
Vlan58                 10.10.58.1      YES manual down                  down    
Vlan59                 10.10.59.1      YES manual down                  down    
Vlan60                 10.10.60.1      YES manual down                  down    
Vlan61                 10.10.61.1      YES manual down                  down    
Vlan62                 10.10.62.1      YES manual down                  down    
Vlan63                 10.10.63.1      YES manual down                  down    
Vlan64                 10.10.64.1      YES manual down                  down    
Vlan65                 10.10.65.1      YES manual down                  down    
Vlan66                 10.10.66.1      YES manual down                  down    
Vlan67                 10.10.67.1      YES manual down                  down    
Vlan68                 10.10.68.1      YES manual down                  down    
Vlan69                 10.10.69.1      YES manual down                  down    
Vlan70                 10.10.70.1      YES manual down                  down    
Vlan71                 10.10.71.1      YES manual down                  down    
Vlan72                 10.10.72.1      YES manual down                  down    
Vlan73                 10.10.73.1      YES manual down                  down    
Vlan74                 10.10.74.1      YES manual down                  down    
Vlan75                 10.10.75.1      YES manual down                  down    
Vlan76                 10.10.76.1      YES manual down                  down    
Vlan77                 10.10.77.1      YES manual down                  down    
Vlan78                 10.10.78.1      YES manual down                  down    
Vlan79                 10.10.79.1      YES manual down                  down    
Vlan80                 10.10.80.1      YES manual down                  down    
Vlan81                 10.10.81.1      YES manual down                  down    
Vlan82                 10.10.82.1      YES manual down                  down    
Vlan83                 10.10.83.1      YES manual down                  down    
Vlan84                 10.10.84.1      YES manual down                  down    
Vlan85                 10.10.85.1      YES manual down                  down    
Vlan86                 10.10.86.1      YES manual down                  down    
Vlan87                 10.10.87.1      YES manual down                  down    
Vlan88                 10.10.88.1      YES manual down                  down    
Vlan89                 10.10.89.1      YES manual down                  down    
Vlan90                 10.10.90.1      YES manual down                  down    
Vlan91                 10.10.91.1      YES manual down                  down    
Vlan92                 10.10.92.1      YES manual down                  down    
Vlan93                 10.10.93.1      YES manual down                  down    
Vlan94                 10.10.94.1      YES manual down                  down    
Vlan95                 10.10.95.1      YES manual down                  down    
Vlan96                 10.10.96.1      YES manual down                  down    
Vlan97                 10.10.97.1      YES manual down                  down    
Vlan98                 10.10.98.1      YES manual down                  down    
Vlan99                 10.10.99.1      YES manual down                  down    
Vlan100                10.10.100.1     YES manual down                  down    
Vlan101                10.10.101.1     YES manual down                  down    
Vlan102                10.10.102.1     YES manual down                  down    
Vlan103                10.10.103.1     YES manual down                  down    
Vlan104                10.10.104.1     YES manual down                  down    
Vlan105                10.10.105.1     YES manual down                  down    
Vlan106                10.10.106.1     YES manual down                  down    
Vlan107                10.10.107.1     YES manual down                  down    
Vlan108                10.10.108.1     YES manual down                  down    
Vlan109                10.10.109.1     YES manual down                  down    
Vlan110                10.10.110.1     YES manual down                  down    
Vlan111                10.10.111.1     YES manual down                  down    
Vlan112                10.10.112.1     YES manual down                  down    
Vlan113                10.10.113.1     YES manual down                  down    
Vlan114                10.10.114.1     YES manual down                  down    
Vlan115                10.10.115.1     YES manual down                  down    
Vlan116                10.10.116.1     YES manual down                  down    
Vlan117                10.10.117.1     YES manual down                  down    
Vlan118                10.10.118.1     YES manual down                  down    
Vlan119                10.10.119.1     YES manual down                  down    
Vlan120                10.10.120.1     YES manual down                  down    
Vlan121                10.10.121.1     YES manual down                  down    
Vlan122                10.10.122.1     YES manual down                  down    
Vlan123                10.10.123.1     YES manual down                  down    
Vlan124                10.10.124.1     YES manual down                  down    
Vlan125                10.10.125.1     YES manual down                  down    
Vlan126                10.10.126.1     YES manual down                  down    
Vlan127                10.10.127.1     YES manual down                  down    
Vlan128                10.10.128.1     YES manual down                  down    
Vlan129                10.10.129.1     YES manual down                  down    
Vlan130                10.10.130.1     YES manual down                  down    
Vlan131                10.10.131.1     YES manual down                  down    
Vlan132                10.10.132.1     YES manual down                  down    
Vlan133                10.10.133.1     YES manual down                  down    
Vlan134                10.10.134.1     YES manual down                  down    
Vlan135                10.10.135.1     YES manual down                  down    
Vlan136                10.10.136.1     YES manual down                  down    
Vlan137                10.10.137.1     YES manual down                  down    
Vlan138                10.10.138.1     YES manual down                  down    
Vlan139                10.10.139.1     YES manual down                  down    
Vlan140                10.10.140.1     YES manual down                  down    
Vlan141                10.10.141.1     YES manual down                  down    
Vlan142                10.10.142.1     YES manual down                  down    
Vlan143                10.10.143.1     YES manual down                  down    
Vlan144                10.10.144.1     YES manual down                  down    
Vlan145                10.10.145.1     YES manual down                  down    
Vlan146                10.10.146.1     YES manual down                  down    
Vlan147                10.10.147.1     YES manual down                  down    
Vlan148                10.10.148.1     YES manual down                  down    
Vlan149                10.10.149.1     YES manual down                  down    
Vlan150                10.10.150.1     YES manual down                  down    
Vlan151                10.10.151.1     YES manual down                  down    
Vlan152                10.10.152.1     YES manual down                  down    
Vlan153                10.10.153.1     YES manual down                  down    
Vlan154                10.10.154.1     YES manual down                  down    
Vlan155                10.10.155.1     YES manual down                  down    
Vlan156                10.10.156.1     YES manual down                  down    
Vlan157                10.10.157.1     YES manual down                  down    
Vlan158                10.10.158.1     YES manual down                  down    
Vlan159                10.10.159.1     YES manual down                  down    
Vlan160                10.10.160.1     YES manual down                  down    
Vlan161                10.10.161.1     YES manual down                  down    
Vlan162                10.10.162.1     YES manual down                  down    
Vlan163                10.10.163.1     YES manual down                  down    
Vlan164                10.10.164.1     YES manual down                  down    
Vlan165                10.10.165.1     YES manual down                  down    
Vlan166                10.10.166.1     YES manual down                  down    
Vlan167                10.10.167.1     YES manual down                  down    
Vlan168                10.10.168.1     YES manual down                  down    
Vlan169                10.10.169.1     YES manual down                  down    
Vlan170                10.10.170.1     YES manual down                  down    
Vlan171                10.10.171.1     YES manual down                  down    
Vlan172                10.10.172.1     YES manual down                  down    
Vlan173                10.10.173.1     YES manual down                  down    
Vlan174                10.10.174.1     YES manual down                  down    
Vlan175                10.10.175.1     YES manual down                  down    
Vlan176                10.10.176.1     YES manual down                  down    
Vlan177                10.10.177.1     YES manual down                  down    
Vlan178                10.10.178.1     YES manual down                  down    
Vlan179                10.10.179.1     YES manual down                  down    
Vlan180                10.10.180.1     YES manual down                  down    
Vlan181                10.10.181.1     YES manual down                  down    
Vlan182                10.10.182.1     YES manual down                  down    
Vlan183                10.10.183.1     YES manual down                  down    
Vlan184                10.10.184.1     YES manual down                  down    
Vlan185                10.10.185.1     YES manual down                  down    
Vlan186                10.10.186.1     YES manual down                  down    
Vlan187                10.10.187.1     YES manual down                  down    
Vlan188                10.10.188.1     YES manual down                  down    
Vlan189                10.10.189.1     YES manual down                  down    
Vlan190                10.10.190.1     YES manual down                  down    
Vlan191                10.10.191.1     YES manual down                  down    
Vlan192                10.10.192.1     YES manual down                  down    
Vlan193                10.10.193.1     YES manual down                  down    
Vlan194                10.10.194.1     YES manual down                  down    
Vlan195                10.10.195.1     YES manual down                  down    
Vlan196                10.10.196.1     YES manual down                  down    
Vlan197                10.10.197.1     YES manual down                  down    
Vlan198                10.10.198.1     YES manual down                  down    
Vlan199                10.10.199.1     YES manual down                  down    
Vlan200                10.10.200.1     YES manual down                  down    
```

## Auteur

- **Nom** : MoHamed ESSID
- **Contact** : mohamedessid2200@gmail.com

## Ressources

- [Documentation de Netmiko](https://github.com/ktbyers/netmiko)
- [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/)
