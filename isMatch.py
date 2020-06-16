from URLToIngredients import UrlToIngredients
import fulljson as JSON

recipes = UrlToIngredients(botLim=53787, topLim=53803, URL='https://www.delish.com/cooking/recipe-ideas/recipes/a')
myIngredients = ['bacon', 'extra-virgin olive oil, divided', 'chicken breast', 'Italian seasoning', 'kosher salt', 'Freshly ground black pepper', 'freshly grated Parmesan, plus more for sprinkling', 'pizza dough', 'Caesar dressing', 'shredded mozzarella, plus more for sprinkling', 'green onions, thinly sliced', 'Egg wash', 'chopped parsley']

for recipe in recipes:
    if myIngredients.sort() == recipe.sort():
        print(recipe)