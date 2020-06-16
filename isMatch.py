from URLToIngredients import UrlToIngredients

recipes = UrlToIngredients(botLim=53787, topLim=53803, URL='https://www.delish.com/cooking/recipe-ideas/recipes/a')

for recipe in recipes:
    if len(recipe) > 0:
        print(recipe)