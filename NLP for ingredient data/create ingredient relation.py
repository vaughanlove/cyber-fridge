
query = ''
ingredients = ['one', 'two', 'three', 'four']
temp = ''
temp2 = ''
length = len(ingredients)


for k in range(length, 0, -1):
    for j in range(length - k + 1):
        #print(ingredients[j:k + j])
        query = ''
        temp = 'a'
        temp2 = 'b'
        for i in ingredients[j:k+j]:
            word = i.lower()
            query += 'MATCH (' + temp + ' { ingredientName: \'' + str(word) + '\' })-[' + temp2 + ':INGREDIENT_IN]->(recipe) '
            temp += 'a'
            temp2 += 'b'
        query += ' return recipe '
        print(query)