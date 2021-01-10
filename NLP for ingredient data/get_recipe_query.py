from neo4j import GraphDatabase

ingredients = ["apple","orange","peach"]

driver=GraphDatabase.driver(uri='bolt://localhost:11005', auth=("neo4j","GlassGlobe101!"))
session = driver.session()

query_sample = '''MATCH (a { ingredientName: 'salt' })-[nn:INGREDIENT_IN]->(recipe)
        MATCH (k { ingredientName: 'sugar' })-[j:INGREDIENT_IN]->(recipe)
        MATCH (b { ingredientName: 'apple' })-[d:INGREDIENT_IN]->(recipe)
        MATCH (la { ingredientName: 'cranberry' })-[aa:INGREDIENT_IN]->(recipe)
        return recipe'''
query = ''
temp = 'a'
temp2 = 'b'

for i in ingredients:
    word = i.lower()
    query += 'MATCH (' + temp + ' { ingredientName: \'' + str(word) + '\' })-[' + temp2 +  ':INGREDIENT_IN]->(recipe) '
    temp +='a'
    temp2+='b'
query += ' return recipe'

results = session.run(query)

for result in results:
    print(result.data()['recipe']['name'], result.data()['recipe']['url'])
