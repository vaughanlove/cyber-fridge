import requests
from bs4 import BeautifulSoup


URL = 'https://www.delish.com/cooking/recipe-ideas/'
URL2 = 'https://www.delish.com/cooking/recipe-ideas/recipes/a53802/'

# loop numbers are relative to the URL codes on delish to access. It ranges from 15000 - ~54000
# delish also uses 'a
# one point of optimization could be to ignore specific types of recipes, like specifying for a dinner recipe.

for i in range(53789, 53803):
    ingredientList = []
    URL = 'https://www.delish.com/cooking/recipe-ideas/recipes/a' + str(i)
    try:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
    except:
        print('recipe doesn\'t exist')
        break

    ingredients = soup.find_all(class_="ingredient-description")
    for ingredient in ingredients:
        if ingredient.text not in ingredientList:
            ingredientList.append(ingredient.text)
    print(ingredientList)

