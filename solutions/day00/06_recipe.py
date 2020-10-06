
cookbook = {
    "sandwich"  : {
        'ingredients'   : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal'          : 'lunch',
        'prep_time'     : 10
    },
    "cake"      : {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal'        : 'dessert',
        'prep_time'   : 60
    },
    "salad"     : {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal'        : 'lunch',
        'prep_time'   : 15
    }
}


def printRecipe(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print("Recipe for {name}:\nIngredients list: {r[ingredients]}\nTo be eaten for {r[meal]}.\nTakes {r[prep_time]} minutes of cooking.".format(name=recipe_name, r=recipe))
    else:
        print("Recipe not found!")

def deleteRecipe(recipe_name):
    if recipe_name in cookbook:
        cookbook.pop(recipe_name)
        print("Recipe deleted!")
    else:
        print("Recipe not found!")

def addRecipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {
        'ingredients' : ingredients,
        'meal'        : meal,
        'prep_time'   : prep_time
    }

def printAllRecipeNames():
    print(list(cookbook.keys()))

def manage():
    allowed_input = [1, 2, 3, 4, 5]

    while True:
        nbr = input("\nPlease select an option by typing the corresponding number: \n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> ")


        if not nbr.isnumeric() or int(nbr) not in allowed_input:
            print("This option does not exist, please type the corresponding number.")
            continue

        nbr = int(nbr)
        if nbr == 1:
            recipe_name = input("Please enter the recipe's name:\n>> ")

            ingredients = input("Please enter the recipe's ingredients separated by commas:\n>> ")
            ingredients = ingredients.split(',')

            meal = input("Please enter the recipe's meal type:\n>> ")

            prep_time = ""
            while not prep_time.isnumeric():
                prep_time = input("Please enter the recipe's preparation time:\n>> ")
            prep_time = int(prep_time)

            addRecipe(recipe_name, ingredients, meal, prep_time)
        elif nbr == 2:
            recipe_name = input("Please enter the recipe's name to delete it:\n>> ")
            deleteRecipe(recipe_name)
        elif nbr == 3:
            recipe_name = input("Please enter the recipe's name to get its details:\n>> ")
            printRecipe(recipe_name)
        elif nbr == 4:
            print("Recipes in the cookbook:\n")
            printAllRecipeNames()
        elif nbr == 5:
            print("Cookbook closed.")
            exit()

manage()