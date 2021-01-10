from neo4j import GraphDatabase
import csv
from uuid import uuid4


from_file = './testset.csv'

# driver=GraphDatabase.driver(uri='bolt://localhost:11005', auth=("neo4j","GlassGlobe101!"))
# session = driver.session()

fp = open(from_file, 'r')
reader = csv.reader(fp)

for row in reader:
    unique_id = uuid4()
    recipe_url = row[0]
    recipe_name = row[1]
    ingredients = row[2].lower().split(' ')
    query = """
            CREATE (r:Recipe{{name: '{recipe_name}', url: '{recipe_url}', uuid: '{unique_id}'}})
            """.format(recipe_name=recipe_name, recipe_url=recipe_url, unique_id=unique_id)
    #session.run(query)
    print(query)
    print(ingredients)


'''query = f"""
            MATCH (i:Ingredient)
            WHERE i.ingredientName =~ '(?i){word}'
            RETURN i.ingredientId
            """
            results = session.run(query)'''




