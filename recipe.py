import json

# File to store recipes
RECIPE_FILE = "recipes.json"

# Load recipes from file
def load_recipes():
    try:
        with open(RECIPE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save recipes to file
def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

# Add a new recipe
def add_recipe(recipes):
    name = input("Enter the recipe name: ").strip().lower()
    if name in recipes:
        print("This recipe already exists!")
        return

    ingredients = input("Enter the ingredients (comma-separated): ").strip().lower().split(",")
    steps = input("Enter the cooking steps: ").strip()

    recipes[name] = {
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "steps": steps
    }
    save_recipes(recipes)
    print(f"Recipe '{name}' added successfully!")

# Find recipes based on available ingredients
def find_recipes(recipes):
    if not recipes:
        print("No recipes available! Add some first.")
        return

    available_ingredients = input("Enter the ingredients you have (comma-separated): ").strip().lower().split(",")
    available_ingredients = [ingredient.strip() for ingredient in available_ingredients]

    matches = []
    for name, details in recipes.items():
        missing_ingredients = [ing for ing in details["ingredients"] if ing not in available_ingredients]
        matches.append((name, missing_ingredients))

    # Sort recipes by the number of missing ingredients
    matches.sort(key=lambda x: len(x[1]))

    print("\nRecipe Recommendations:")
    for name, missing in matches:
        print(f"- {name.title()} (Missing Ingredients: {', '.join(missing) if missing else 'None'})")

# View recipe details
def view_recipe(recipes):
    name = input("Enter the recipe name to view: ").strip().lower()
    if name not in recipes:
        print("Recipe not found!")
        return

    recipe = recipes[name]
    print(f"\n{name.title()} Recipe:")
    print("Ingredients:", ", ".join(recipe["ingredients"]))
    print("Steps:", recipe["steps"])

# Main menu
def main():
    recipes = load_recipes()

    while True:
        print("\nRecipe Recommendation System")
        print("1. Add Recipe")
        print("2. Find Recipes")
        print("3. View Recipe Details")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            find_recipes(recipes)
        elif choice == "3":
            view_recipe(recipes)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
