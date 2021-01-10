from neo4j import GraphDatabase

driver=GraphDatabase.driver(uri='bolt://localhost:11014', auth=("neo4j","GlassGlobe101!"))
session = driver.session()


# this is where the recipe needs to be loaded in... and the inputs are assumed to be ingredient nodes.
# probably should learn how to throw errors here because if a unauthorized ingredient gets through - everything fials.
recipe = []

query="""
create(r:Recipe{name:"A",url:"B"})
RETURN n.name as name ,n.city as city
"""

results=session.run(query)

recipe_name = results["name"]

for ingred in recipe:

    query = """match(i:Ingredient{ingredientName:"Roni"}),(r:Recipe{recipeName:"recipe_name"}) 
    create (i)-[r1:INGREDIENT_OF]->(r)
    """