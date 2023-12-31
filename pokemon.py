# one can update to the latest dex by running this python script
import requests
import json
from pathlib import Path

from bs4 import BeautifulSoup

URL = "https://pokemondb.net/pokedex/national"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
pokemonData = {}

results = soup.findAll(class_="infocard")

for result in results:
    dexNumber = result.find("small")
    pokemonName = result.find("a", class_="ent-name")
    pokemonData[dexNumber.text[1:]
                ] = pokemonName.text.lower().replace("\u00e9", "e").replace("\u2640", "-f").replace("\u2642", "-m")
    pokemonData[pokemonName.text.lower().replace("\u00e9", "e").replace("\u2640", "-f").replace("\u2642", "-m")
                ] = dexNumber.text[1:]

jsonData = json.dumps(pokemonData)

with open('./pokedexdata.json', 'w') as f:
    f.write(jsonData)

imageData = {}
images = Path("./[HOME] Pokémon Renders/Shiny").glob("*.png")
for image in images:
    pokedexNumber = (str(image).split("/")[2][13:17])
    pokemonImage = str(image)
    imageData[pokemonImage] = pokedexNumber

jsonImageData = json.dumps(imageData)
with open('./Images/shiny.json', 'w') as y:
    y.write(jsonImageData)

imageDataNormal = {}
imagesNormal = Path("./[HOME] Pokémon Renders/Normal").glob("*.png")
for imageNormal in imagesNormal:
    pokedexNumberNormal = (str(imageNormal).split("/")[2][13:17])
    pokemonImageNormal = str(imageNormal)
    imageDataNormal[pokemonImageNormal] = pokedexNumberNormal

jsonImageNormalData = json.dumps(imageDataNormal)
with open('./Images/normal.json', 'w') as z:
    z.write(jsonImageNormalData)
