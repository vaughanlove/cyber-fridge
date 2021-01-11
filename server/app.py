from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from neo4j import GraphDatabase
import json

f=open("credentials.txt","r")
lines=f.readlines()
neo4jpass=lines[0]
f.close()

driver = GraphDatabase.driver(uri='bolt://localhost:11004', auth=("neo4j", neo4jpass))
session = driver.session()
app = Flask(__name__)
CORS(app)
api = Api(app)
# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument('ingredients')

class SEARCH(Resource):
  def post(self):
    args = parser.parse_args()
    ingredients = json.loads(args['ingredients'])
    length = len(ingredients)

    for k in range(length, 0, -1):
      for j in range(length - k + 1):
        # print(ingredients[j:k + j])
        query = ''
        temp = 'a'
        temp2 = 'b'
        for i in ingredients[j:k + j]:
          word = i.lower()
          query += 'MATCH (' + temp + ' { ingredientName: \'' + str(
            word) + '\' })-[' + temp2 + ':INGREDIENT_IN]->(recipe) '
          temp += 'a'
          temp2 += 'b'
        query += ' return recipe '
        #print(query)
        results = session.run(query).data()
        if results != []:
          print([result for result in results])
          rN = str(results[0]['recipe']['name'])
          rU = str(results[0]['recipe']['url'])
          #return {'recipe_name': rN, 'recipe_url': rU}
          return [result for result in results]

        #results = session.run(query).data()
        if (results == []):
          return {'recipe_name': 'no valid results, try removing some ingredients', 'recipe_url': ''}
        '''
        else:
          print(results[0]['recipe']['name'], results[0]['recipe']['url'])
          rN = str(results[0]['recipe']['name'])
          rU = str(results[0]['recipe']['url'])
          return {'recipe_name': rN, 'recipe_url': rU}'''

class ingredient_list(Resource):
  def get(self):
    query = """
    match (i:Ingredient) return i.ingredientName
    """

    results = session.run(query)

    final_list = []

    for result in results:
      final_list.append(result.data()['i.ingredientName'])

    print(final_list)
    return final_list

api.add_resource(SEARCH, "/search")
api.add_resource(ingredient_list, "/ingredient_list")

if __name__ == "__main__":
  app.run(debug=True)