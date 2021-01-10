from uuid import uuid4
import csv
from neo4j import GraphDatabase

from_file = './testset.csv'

driver=GraphDatabase.driver(uri='bolt://localhost:11005', auth=("neo4j","GlassGlobe101!"))
session = driver.session()

fp = open(from_file, 'r')
reader = csv.reader(fp)

unique_id = uuid4()
recipe_name='gabys victoria sandwich'
recipe_url='https://www.bbcgoodfood.com/recipes/1162657/gabys-victoria-sandwich'
#ingredients = ingredients.split(' ')

length = len(ingredients)
for k in range(length, 0, -1):
    #print(f"word length: {k}")
    for j in range(length - k + 1):
        #print(f"word: {' '.join(ingredients[j:k+j])}")
        word = ' '.join(ingredients[j:k+j])
        if (results.single() != None):
            print(f'adding relation to recipe for ingredient: {word}')
            # this is where the ingredient relation needs to be added to the database









query = """
        CREATE (r:Recipe{{name: '{recipe_name}', url: '{recipe_url}', uuid: '{unique_id}'}})
        """.format(recipe_name=recipe_name, recipe_url=recipe_url, unique_id=unique_id)


# 91e9b823-700a-4560-925f-fddbc72bfa75
# 834082bf-d60d-40ab-90ad-38f716947cc8
# add ingredient relations to:
# <id>:3501name:Chipotle Mayourl:https://www.feastingathome.com/chipotle-mayo/uuid:834082bf-d60d-40ab-90ad-38f716947cc8