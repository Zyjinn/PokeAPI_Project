# Imports Json and requests (to get API requests)
import json
import requests


# Ask the user for what pokemon's name they want to retrieve
# given: None
# returns: pokemon name(taken from user input)
def getPokemonName(): 
    print("What Pokemon do you want to retrieve information for?")
    pokeName = input()
    return pokeName

# Gets the requested pokemon from the API
# Given, a pokemon name
# prints the data(name + weight + height) to the console for said pokemon to the console
def requestPokeAPI(pokeName):
    print(f'Requesting {pokeName} from the API...')
    # Create string for request URL pokemon's name
    requestURL = "https://pokeapi.co/api/v2/pokemon/" + pokeName
    # Make sure the request is lowercase
    requestURL = requestURL.casefold()
    # print(requestURL) # TESTING

    # Fetch the data from the URL
    r = requests.get(requestURL)

    # Check if a valid request
    if(r.ok != True):
        return "error"

    # Get data as a json
    jsonInfo = r.json
    # data = json.load(jsonInfo)

    pokeDictionary = r.json()
    print(f'Request for {pokeName} complete!\n')
    return pokeDictionary

# Print the information (height, weight, name) 
# For the given pokemon
# Given: dictionary(of json data)
# Return: printed name, height, and weight of pokemon
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
    return

# Get the pokemon's names, weight, and height and return them within the python console
def main():
    newRequest = True
    while(newRequest == True):
        # Get the pokemon's name
        pokemonName = getPokemonName()

        # Request the pokemon from the API
        requestDictionary = requestPokeAPI(pokemonName)

        # Check if it's a valid request
        if(requestDictionary == "error"):
            print("That pokemon was not found\n")

        # It's a valid request
        else:
            # Print the data for the pokemon
            printPokeInfo(requestDictionary)

        # Ask user if they want to continue requesting pokemon
        validRequest = False
        while(validRequest == False):
            print("\nRequest another pokemon?")
            print("1: Yes")
            print("2: No")
            menuChoice = input()
            # User wants to request another pokemon
            if menuChoice == '1':
                validRequest = True

            # User wants to quit requesting pokemon
            elif menuChoice == '2':
                validRequest = True
                newRequest = False
            
            # User input invalid menu choice
            else:
                print("Invalid menu choice, try again")

    print("\n***Thanks for catching them all gamer!***")
# Main function called
if __name__ == "__main__":
    main()