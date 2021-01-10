
<template>
  <div id="app">
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
      <header class="mb-auto">
        <div>
          <nav class="nav nav-stacked float-sm-right ">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
            <a class="nav-link" href="#">About</a>
            <a class="nav-link" href="https://github.com/vaughanlove/">Github</a>
          </nav>
          <h1 class="offset-1 text-primary font-weight-bolder mt-5 mb-3">supper</h1>
          <p class="offset-1 pt-sm-2 mb-5 py-0">welcome, still new (buggy) but functional.</p>

        </div>
      </header>

      <b-container>
        <b-row align-h="center">
          <h4 class="text-center pt-sm-2 mt-0 py-0 mb-2">what's in your fridge?</h4>
        </b-row>

        <b-row class="justify-content-center mt-2">
        </b-row>
        <b-row align-h="center">
            <b-form-select v-model="selected" required id="my-list-id" @keyup.enter="addIngredient" class="w-50">
              <option v-for="ingredient in all_ingredients" :key="ingredient">{{ ingredient }}</option>
            </b-form-select>
            <b-button variant="primary" class="mx-1" v-model="selected" @click="addIngredient" >add</b-button>
        </b-row>

        <b-row align-h="center">
          <ul class="list-unstyled d-inline-flex flex-wrap mt-2">
          <b-button
            v-for="ingredient in ingredients"
            :key="ingredient"
            @click="removeIngredient(ingredient)"
            class="mt-1 mr-2 pr-2"
            variant="dark"
            body-class="py-1 text-nowrap text-primary"
          >{{ ingredient }}</b-button>
        </ul>
        </b-row>

        <b-row align-h="center">
          <b-button @click="searchRecipes" class="text-center">search</b-button>
        </b-row>
      </b-container>

      <b-row align-h="center">
          <h3 class="center mt-5">
            {{ found_recipe['recipe_name'] }}
          </h3>
      </b-row>
      <b-row align-h="center">
        <a v-bind:href="''">
            {{ found_recipe['recipe_url'] }}
        </a>
      </b-row>
      <b-row align-h="center">
        <b-list-group @mouseover="hovered=found['recipe']['id']"
              @mouseleave="hovered=null" class="w-75 center-block" v-for="found in found_recipe" :key="found['recipe']['id']">
          <b-list-group-item
              target="_blank"
              :href="found['recipe']['url']"
              v-if="hovered == found['recipe']['id']"
              active
              >{{found['recipe']['name']}}</b-list-group-item>
          <b-list-group-item
              target="_blank"
              :href="found['recipe']['url']"
              v-else
              >{{found['recipe']['name']}}</b-list-group-item>
        </b-list-group>
      </b-row>


      <div class="fixed-bottom text-black-50 py-3">
        <b-container>
          Made by <a href="https://github.com/vaughanlove/" class="text-black"> Vaughan </a>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'App',
  components: {
  },
  data(){
    return {
        model: null,
        selected: '',
        hovered: false,
        ingredients: ['apple', 'orange', 'peach'],
        //found_recipe: {'recipe_name': '', 'recipe_url': ''},
        found_recipe: [],
        all_ingredients: ['apple1','apple6','apple5','apple4','apple3','apple2']
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:5000/ingredient_list').then((response) => {
      this.all_ingredients = response.data
    })
  },
  methods: {
    addIngredient(a) {
      console.log(a.target.value);
      if (a.target.value != ''){
        this.ingredients.push(a.target.value);
      }
      a.target.value = '';
    },
    searchRecipes() {
      axios.post('http://127.0.0.1:5000/search', {'ingredients':JSON.stringify(this.ingredients)}).then((response) => {
        this.found_recipe = response.data
      })
      console.log(this.found_recipe)
    },

    removeIngredient(e) {
      console.log(e);
      const a = this.ingredients.indexOf(e)
      this.ingredients.splice(a, 1)
    },
    search(input) {
      if (input.length < 1) { return [] }
      return this.all_ingredients.filter(ingredient => {
        return ingredient.toLowerCase()
          .startsWith(input.toLowerCase())
  })
}
  },
}
</script>
<style lang="scss">
  @import "../themes/custom.scss";
  @import "~bootstrap/scss/bootstrap.scss";
</style>
