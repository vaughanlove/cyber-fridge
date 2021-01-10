import requests
from bs4 import BeautifulSoup

def UrlToIngredients(botLim, topLim, URL):
    listList = []
    for i in range(botLim, topLim):
        url = URL + str(i)
        ingredientList = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        ingredients = soup.find_all(class_="ingredient-description")

        if ingredients:
            for ingredient in ingredients:
                if ingredient.text not in ingredientList:
                    ingredientList.append(ingredient.text)
            listList.append(ingredientList)
    return listList
