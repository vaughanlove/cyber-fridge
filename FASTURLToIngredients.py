import requests
from bs4 import BeautifulSoup
import numpy as np


def Url2Ingredients(botLim, topLim, URL, desiredRecipe):
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
            compareArray = np.array(ingredientList)
            if np.array_equal(desiredRecipe, compareArray):
                print('There is a match! The URL to your recipe is: ' + url)
            print(ingredientList)

