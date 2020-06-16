import requests
from bs4 import BeautifulSoup

def UrlToIngredients(botLim, topLim, URL):
    listList = []
    for i in range(botLim, topLim):
        url = URL + str(i)
        ingredientList = []

        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print('recipe doesn\'t exist')
            break

        ingredients = soup.find_all(class_="ingredient-description")

        for ingredient in ingredients:
            if ingredient.text not in ingredientList:
                ingredientList.append(ingredient.text)
        if len(ingredientList) > 0:
            listList.append(ingredientList)
    return listList
