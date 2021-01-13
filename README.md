# cyber-fridge
ingredient => recipe

1. webscraped 60k recipes including ingredient lists, urls, recipe names
2. Created a neo4j graph database containing 
  - recipe nodes with name, url properties
  - ingredient nodes of the 900 most common ingredients present in the data.
  - INGREDIENT_IN relation that maps every ingredient to the recipe theyre present in
3. Setup a flask api to query the database to find common recipes based off user inputted ingredients
4. Simple vuejs frontend that lets you input predetermined ingredients and search.




