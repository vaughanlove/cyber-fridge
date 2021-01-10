from neo4j import GraphDatabase
import csv
from uuid import uuid4


from_file = './final_recipe.csv'

driver=GraphDatabase.driver(uri='bolt://localhost:11005', auth=("neo4j","GlassGlobe101!"))
session = driver.session()

fp = open(from_file, 'r')
reader = csv.reader(fp)
num = 1

def addRelation(ingredients, recipe_Id):
    length = len(ingredients)
    for k in range(length, 0, -1):
        #print(f"word length: {k}")
        for j in range(length - k + 1):
            #print(f"word: {' '.join(ingredients[j:k+j])}")
            word = ' '.join(ingredients[j:k+j])
            #print(f'adding relation to recipe for ingredient: {word}')
            query = f'''MATCH (i:Ingredient),(r:Recipe)
                    WHERE i.ingredientName =~ '(?i){word}' AND r.uuid = '{recipe_Id}' CREATE (i)-[a:INGREDIENT_IN]->(r)
                    RETURN a'''
            session.run(query)

for row in reader:
    if num % 50 == 0:
        print(f"RECIPE: {num}")
    num+=1
    unique_id = uuid4()
    recipe_url = row[0]
    recipe_name = row[1]
    ingredients = row[2].lower().split(' ')
    query = """
            CREATE (r:Recipe{{name: '{recipe_name}', url: '{recipe_url}', uuid: '{unique_id}'}})
            """.format(recipe_name=recipe_name, recipe_url=recipe_url, unique_id=unique_id)
    session.run(query)
    addRelation(ingredients, unique_id)





session.close()
fp.close()

