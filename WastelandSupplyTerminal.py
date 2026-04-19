from recipelist import recipes
import time
from colorama import init, Fore
import shutil
import os

validCats = ["food", "chems", "drinks", "alcohol", "big bloom", "misc", "more food", "more drinks"]
terminalWidth = shutil.get_terminal_size().columns

init()
print(Fore.GREEN)

def typewriter(text):
    for char in text:
        print(char, end="", flush=True)
        if char != " ":
            time.sleep(0.025)


def printlogo():
    print("██████   ██████   ██████          ████████  ███████   ██████".center(terminalWidth))
    print(" ██   ██  ██  ██   ██   ██            ██     ██        ██     ".center(terminalWidth))
    print(" ██████   ██  ██   ██████   ██████    ██     █████     ██     ".center(terminalWidth))
    print(" ██  ██   ██  ██   ██   ██            ██     ██        ██     ".center(terminalWidth))
    print("██   ██  ██████   ██████             ██     ███████   ██████".center(terminalWidth))

terminalHeight = shutil.get_terminal_size().lines
blankLines = terminalHeight - 10
blankLines = (blankLines / 3) * 2

print("\n" * 3)
print(("=" * 70).center(terminalWidth))
print()
printlogo()
print()
print("INDUSTRIES".center(terminalWidth))
print(("=" * 70).center(terminalWidth))
time.sleep(1.0)

print("\n" * int(blankLines -3))
typewriter("INITIALIZING...""\n")
time.sleep(1.0)

typewriter("LOADING DATABASE...""\n")
time.sleep(1.0)
typewriter("SYSTEM ONLINE.")
time.sleep(1.5)

os.system("cls")

print(("=" * 50).center(terminalWidth))
typewriter("ROB-TEC INDUSTRIES UNIFIED OPERATING SYSTEM".center(terminalWidth))
typewriter("COPYRIGHT 2075-2077 ROB-TEC INDUSTRIES".center(terminalWidth))
print(("=" * 50).center(terminalWidth))
typewriter("WASTELAND SUPPLY TERMINAL".center(terminalWidth))
typewriter("-- FALLOUT 76 --".center(terminalWidth))
print(("=" * 50).center(terminalWidth))
print()
typewriter("Recipe Directory: type recipe directory or rd.""\n""To exit: type quit.""\n")
print("\n" * 2)

while True:

    typewriter("Enter recipes (comma separated):""\n")
    recipeChoice = input().lower().strip()
    shoppingList = {}

    if recipeChoice == "":
        typewriter("Invalid input.""\n")
        continue
    elif recipeChoice == "quit":
        break
    elif recipeChoice == "recipe directory" or recipeChoice == "rd":
        print()
        print("RECIPE DIRECTORY")
        print("=" * 17)
        print("Food""\n""More Food""\n""Drinks""\n""More Drinks""\n""Alcohol""\n""Chems""\n""Big Bloom""\n""Misc""\n")
        print()


        while True:
            print()
            typewriter("Enter a category (type 'all' to see everything, or 'exit' to return):""\n")
            catChoice = input().lower().strip()
            print()
            if catChoice == "exit":
                break
            elif catChoice == "all":
                print("=" * 20)
                print(catChoice.upper())
                print("=" * 20)
                for recipe in recipes:
                    print(recipe.title())
            elif catChoice in validCats:
                print("=" * 20)
                print(catChoice.upper())
                print("=" * 20)
                for recipe in recipes:
                    recipeData = recipes.get(recipe)
                    if recipeData.get("category") == catChoice:
                        print(recipe.title())
            else:
                typewriter("Invalid input.")
            print("=" * 20)





    else:
        separateRecipes = [recipe.strip().replace("'", "").replace("’", "").replace("-", " ") for recipe in recipeChoice.split(",") if recipe.strip() != ""]
        uniqueRecipes = []
        for recipe in separateRecipes:
            if recipe not in uniqueRecipes:
                uniqueRecipes.append(recipe)
        separateRecipes = uniqueRecipes
        invalidRecipes = [recipe for recipe in separateRecipes if recipe not in recipes]
        validRecipes = [recipe for recipe in separateRecipes if recipe in recipes]

        if invalidRecipes:
            print("\n" * 2)
            typewriter("Invalid recipes will be skipped.""\n")
            typewriter("Invalid Recipes: ""\n")
        for recipe in invalidRecipes:
            print(recipe.title())
        print()
        if validRecipes:
            typewriter("You chose: ""\n")

        for recipe in validRecipes:
            print(recipe.title())
        print()

        for recipe in validRecipes:
            typewriter("How many " + recipe.title() + " do you need?""\n")

            while True:
                quantityInput = input().strip()
                if quantityInput.isdigit():
                    quantityRecipes = int(quantityInput)
                    break
                else:
                    typewriter("Invalid input. Please type a number.""\n")#allows it to continue asking if input is not int

            recipeData = recipes.get(recipe)
            ingredients = recipeData.get("ingredients")
            for ingredient, ingredientAmount in ingredients.items():
                totalNeeded = ingredientAmount * quantityRecipes
                if ingredient in shoppingList:
                    shoppingList[ingredient] = shoppingList[ingredient] + totalNeeded
                else:
                    shoppingList[ingredient] = totalNeeded

        print()
        print("=" * 22)
        if validRecipes:
            typewriter("FINAL MATERIALS LIST: ""\n")
            print("=" * 22)
        for ingredient, ingredientAmount in shoppingList.items():
            print(ingredient + ": " + str(ingredientAmount))
        print("\n" * 2)





