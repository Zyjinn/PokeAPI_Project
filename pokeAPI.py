# Imports Json and requests (to get API requests)
import json
import requests

# Get the pokemon's names, weight, and height and return them within the python console
def main():
    # Get the pokemon's name
    pokemonName = getPokemonName()

    # Request the pokemon from the API
    requestDictionary = requestPokeAPI(pokemonName)

    # Print the data for the pokemon
    printPokeInfo(requestDictionary)


# Ask the user for what pokemon's name they want to retrieve
# given: None
# returns: pokemon name(taken from user input)
def getPokemonName(): 
    print("What Pokemon do you want to retrieve information for?")
    pokeName = input()
    return pokeName

# TODO: Create a get request to get the pokemon's name, weight and height from the json
# Gets the requested pokemon from the API
# Given, a pokemon name
# prints the data(name + weight + height) to the console for said pokemon to the console
def requestPokeAPI(pokeName):
    print(f'Requesting {pokeName} from the API...')
    # Create string for request URL pokemon's name
    requestURL = "https://pokeapi.co/api/v2/pokemon/" + pokeName
    # Make sure the request is lowercase
    requestURL = requestURL.casefold()
    print(requestURL) # TESTING

    # Fetch the data from the URL
    r = requests.get(requestURL)

    # Get data as a json
    jsonInfo = r.json
    # data = json.load(jsonInfo)

    pokeDictionary = r.json()
    print(f'Request for {pokeName} complete!\n')
    return pokeDictionary




# TODO: print and format the data in the json
def printPokeInfo(pokeDictionary):
    # Easy variables for printing
    name = pokeDictionary['name'].title()

    weight = pokeDictionary['weight']
    # Convert hectograms -> kilograms
    weight = weight/10

    height = pokeDictionary['height']
    # convert decimeters -> to feet
    height = height*3.937008
    heightFt = round(height/12)
    heightIn = round(height%12)


    # Print the information for the specified
    print(f'Name: {name}\nWeight: {weight}kg\nHeight: {heightFt}ft, {heightIn}in')



# Main function called
if __name__ == "__main__":
    main()