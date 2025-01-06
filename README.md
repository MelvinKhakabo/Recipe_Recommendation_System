# Recipe_Recommendation_System
A Python application that recommends recipes based on the ingredients the user has at hom

# Recipe Recommendation System
## Objective
Create a Python application that recommends recipes based on the ingredients the user has at home. The app will include a database of recipes and suggest dishes the user can make with their available ingredients.
## Features
### Input Ingredients
Allow the user to input a list of ingredients they have.
### Recipe Matching
Match the input ingredients with a database of recipes to find suitable options.
Show recipes that require the least additional ingredients.
### Detailed Recipe Display
Provide step-by-step instructions, cooking time, and a list of ingredients for the chosen recipe.
### Expand Recipe Database
Allow users to add new recipes to the database.
### Save Favorite Recipes
Enable users to save their favorite recipes for easy access later.

# How it works
How It Works:
## Recipe Storage
Recipes are stored in a JSON file (recipes.json) with their ingredients and steps.
## Adding Recipes
The user can input a new recipe by providing the name, ingredients, and cooking steps.
## Finding Recipes
The user enters the ingredients they have.
The program finds recipes that use these ingredients and displays the missing ingredients, if any.
## Viewing Recipes
The user can view the details (ingredients and steps) of a specific recipe by its name.


# Example Interaction
Recipe Recommendation System
1. Add Recipe
2. Find Recipes
3. View Recipe Details
4. Exit
Choose an option: 1
Enter the recipe name: Pancakes
Enter the ingredients (comma-separated): flour, eggs, milk, sugar
Enter the cooking steps: Mix ingredients and fry in a pan.
Recipe 'pancakes' added successfully!

Recipe Recommendation System
1. Add Recipe
2. Find Recipes
3. View Recipe Details
4. Exit
Choose an option: 2
Enter the ingredients you have (comma-separated): flour, eggs, milk
Recipe Recommendations:
- Pancakes (Missing Ingredients: sugar)

Recipe Recommendation System
1. Add Recipe
2. Find Recipes
3. View Recipe Details
4. Exit
Choose an option: 3
Enter the recipe name to view: Pancakes

Pancakes Recipe:
Ingredients: flour, eggs, milk, sugar
Steps: Mix ingredients and fry in a pan.


#### Possible Enhancements:(YET TO IMPLEMENT)
##### Nutritional Information
Display calorie count and other nutritional data for each recipe.
##### Custom Preferences
Allow filtering by cuisine type, dietary restrictions, or difficulty level.
##### Random Recipe Feature
Suggest a random recipe if the user is unsure what to cook.
##### Integration with an API
Use a recipe API (e.g., Spoonacular) to fetch more recipes dynamically.