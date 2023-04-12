import requests

url = input("Entrez l'URL du site web: ")
payloads = ["'", "\"", "\\", ";", ")", "(", ">", "<", "=", "*", "%", "-", "+", "#", "--", "/*", "*/"]
results = []

for payload in payloads:
    injection_url = url + payload
    response = requests.get(injection_url)

    if "erreur dans votre syntaxe SQL" in response.text or "mysql_fetch_array()" in response.text or "mysql_num_rows()" in response.text or "mysql_query()" in response.text:
        results.append(injection_url)

print("Vulnérabilités d'injection SQL trouvées:")
for result in results:
    print(result)
