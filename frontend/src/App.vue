<style lang="scss">
  @import "../themes/custom.scss";
  @import "~bootstrap/scss/bootstrap.scss";
</style>

<template>
  <div id="app">
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
      <header class="mb-auto">
        <div>
          <nav class="nav nav-stacked float-sm-right">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
            <a class="nav-link" href="#">About</a>
            <a class="nav-link" href="https://github.com/vaughanlove/">Github</a>
          </nav>
          <h1 class="offset-1 text-danger font-weight-bolder mt-5 mb-3">supper</h1>
          <p class="offset-1 pt-sm-2 mb-5 py-0">welcome, still new (buggy) but functional.</p>

        </div>
      </header>

      <b-container>
        <b-row align-h="center">
          <h4 class="text-center pt-sm-2 mt-0 py-0 mb-2">what's in your fridge?</h4>
        </b-row>
        <b-form>
          <b-row align-v="center" class="no-gutters mt-2">
            <b-col cols="4"></b-col>
            <b-col cols="3">
              <label class="sr-only" for="inline-form-input-ingredient">ingredient</label>
               <b-form-input
                id="inline-form-input-ingredient"
                class="mb-2 mb-sm-0"
                placeholder="mozzarella"
                ></b-form-input>
            </b-col>
            <b-col cols="1" class="mx-1">
              <b-form-checkbox class="" >Preferred</b-form-checkbox>
            </b-col>
            <b-col cols="1" class="mx-1">
              <b-button class="py-0 px-1" variant="primary">add</b-button>
            </b-col>
            <b-col cols="4"></b-col>
          </b-row>
          <b-row>
            <b-col cols = "4"></b-col>
            <b-col cols = "4" align-h="center" class="mt-3" >
              <b-list-group horizontal="False" v-for="ingredient in ingredients" :key="ingredient">
                <b-list-group-item class="py-1 px-1 text-secondary">{{ ingredient }}
                  <b-btn-close class="ml-2 px-0"></b-btn-close>
                </b-list-group-item>
              </b-list-group>
            </b-col>
            <b-col cols = "4"></b-col>
          </b-row>

        </b-form>
      </b-container>

      <div class="text-right text-black-50 py-3">
        <mdb-container fluid>
          Made by <a href="https://github.com/vaughanlove/" class="text-black"> Vaughan </a>
        </mdb-container>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {
        ingredients: [ 'apple',
                       'orange',
                       'ground beef',
        ]
    }
  },
  async created(){
    var response = await fetch('http://127.0.0.1:8000/api/recipes/');
    this.recipes = await response.json();
  }
}
</script>

<style>

</style>
