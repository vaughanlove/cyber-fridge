from neo4j import GraphDatabase


def addRelation(ingredients):
    length = len(ingredients)
    for k in range(length, 0, -1):
        #print(f"word length: {k}")
        for j in range(length - k + 1):
            #print(f"word: {' '.join(ingredients[j:k+j])}")
            word = ' '.join(ingredients[j:k+j])
            query = f"""
            MATCH (i:Ingredient)
            WHERE i.ingredientName =~ '(?i){word}'
            RETURN i.ingredientId
            """
            #results = session.run(query)

            #if (results.single() != None):
                #print(f'adding relation to recipe for ingredient: {word}')
                # this is where the ingredient relation needs to be added to the database


