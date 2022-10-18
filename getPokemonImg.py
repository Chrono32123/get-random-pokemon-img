import random
import requests
import os
from PIL import Image

##Get Pokemon Image Script
##PURPOSE: Script to get Pokemon Name, Number, Official Art, and Generate Masked Art for stream overlays.
##AUTHOR: chrono
##LAST UPDATED: 10-18-2022
##Be sure to run pip install -r requirements.txt BEFORE running this!

##Image Cache Location (CHANGE THIS FOR YOUR SYSTEM)
scriptDir = f"C:\streaming\scripts\get-pokemon-images"
cache = f"{scriptDir}/cache"


##Generate random number out of total number of pokemon
pokeNum = random.randrange(1,906)

##Cache folder setup - creates a cache folder in the same directory this script is run.
def setupCache():
    if not os.path.exists(cache):
        os.mkdir(cache)

##Gets pokemon info from pokeapi - this number is used to name the image and text files generated and cached.
def getPokemonInfo():
    apiUrl = f'https://pokeapi.co/api/v2/pokemon/{pokeNum}'
    apiResponse = requests.get(apiUrl)

    #Get Info from Response
    pokeEntry = apiResponse.json()
    pokeName = pokeEntry["name"]
    pokeSprite = pokeEntry["sprites"]["other"]["official-artwork"]["front_default"]
    cache_image(pokeSprite, cache)
    name_to_file(pokeName, pokeNum)

##Caches the image to your local storage using the cache dir specified above (lines 10 + 11)
##If the image already exists then it will just return the path of the file.
def cache_image(link, location):
    filename = link.split("/")[-1]
    cacheFolder = f"{location}/"
    if not os.path.isfile(cacheFolder + filename):
        r = requests.get(link)
        with open(cacheFolder + filename, "wb") as f:
            f.write(r.content)
            f.close()
        r.close()
        hidePokemon(filename, cacheFolder)

    return cacheFolder + filename
    
##output the pokemon name to a text file for reference (this could be improved but it was simple this way)
def name_to_file(name, id):
    filename = f"{cache}/{id}.txt"
    if('-' in name):
        name = name.split("-")[0]
        
    if not os.path.isfile(filename):
        file = open(filename, "w")
        file.write(name.upper())
        file.close()

##create a silhouette of the pokemon retrieved from pokeapi
def hidePokemon(name, location):
    filename = f"{location}/{name[:-4]}-masked.png"
    if not os.path.isfile(filename):
        im = Image.open(location + name)
        alpha = im.getchannel('A')
        masked = Image.new('RGBA', im.size, color=(42,42,134))
        masked.putalpha(alpha)
        masked.save(filename)

setupCache()
getPokemonInfo()
print(pokeNum) ##prints the national dex number for the pokemon so that MixItUp can read this value.