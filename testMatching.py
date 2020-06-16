from FASTURLToIngredients import Url2Ingredients
import numpy as np

myIngredients = np.array(['bacon', 'extra-virgin olive oil, divided', 'chicken breast', 'Italian seasoning', 'kosher salt', 'Freshly ground black pepper', 'freshly grated Parmesan, plus more for sprinkling', 'pizza dough', 'Caesar dressing', 'shredded mozzarella, plus more for sprinkling', 'green onions, thinly sliced', 'Egg wash', 'chopped parsley'])

Url2Ingredients(botLim=52803, topLim=53803, URL='https://www.delish.com/cooking/recipe-ideas/recipes/a', desiredRecipe=myIngredients)

