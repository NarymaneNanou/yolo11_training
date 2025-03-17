import requests

# Lien public Dropbox (avec le paramètre 'dl=1' pour téléchargement direct)
url_dropbox = 'https://www.dropbox.com/scl/fi/aa4ms7lcmvsubui1iaif9/all.zip?rlkey=fvahkfpp1q85qold1cnryl88j&st=ezwxa97y&dl=1'

# Chemin où vous souhaitez enregistrer le fichier sur votre machine locale
chemin_local = 'all_data.zip'

# Télécharger le fichier depuis Dropbox
response = requests.get(url_dropbox)

# Vérifier si le téléchargement a réussi
if response.status_code == 200:
    with open(chemin_local, 'wb') as fichier:
        fichier.write(response.content)
    print(f"Fichier téléchargé avec succès : {chemin_local}")
else:
    print(f"Erreur lors du téléchargement, code HTTP : {response.status_code}")

