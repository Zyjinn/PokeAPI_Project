# Imports Json and requests (to get API requests)
import json
import requests

# Get the pokemon's names, weight, and height and return them within the python console
def main():
    # Get the pokemon's name
    pokemonName = getPokemonName()


# Ask the user for what pokemon's name they want to retrieve
# given: None
# returns: pokemon name(taken from user input)
def getPokemonName(): 
    print("What Pokemon do you want to retrieve information for?")
    pokeName = input()
    return pokeName

# TODO: Create a get request to get the pokemon's name, weight and height from the json


# TODO: print and format the data in the json



# Main function called
if __name__ == "__main__":
    main()