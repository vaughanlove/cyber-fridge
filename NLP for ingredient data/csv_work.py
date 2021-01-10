import csv
from uuid import uuid4

def addRelation(ID, ingredients):
    length = len(ingredients)
    for k in range(length, 0, -1):
        for j in range(length - k + 1):
            word = ' '.join(ingredients[j:k+j])
            writer.writerow([ID, word])


fromFile = './final_recipe.csv'
toRelationFile = './relation_list.csv'
toRecipeFile ='./unique_recipes.csv'

fp = open(fromFile, 'r')
fx = open(toRelationFile, 'w', newline='')
fn = open(toRecipeFile, 'w', newline='')

reader = csv.reader(fp)
writer = csv.writer(fx)
writer1 = csv.writer(fn)

for row in reader:
    unique_id = uuid4()
    #print(row[2].lower().split(' '), ID)
    ingredient_list = row[2].lower().split(' ')
    addRelation(unique_id,ingredient_list)
    writer1.writerow([unique_id, row[1], row[0]])






