<style lang="scss">
  @import "../themes/custom.scss";
  @import "~bootstrap/scss/bootstrap.scss";
</style>

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
          <b-form-tags v-model="ingredients" no-outer-focus class="mb-2 w-50 align-content-center">
            <template v-slot="{ tags, inputAttrs, inputHandlers, addTag, removeTag }">
              <b-input-group aria-controls="my-custom-tags-list">
                <input
                  v-bind="inputAttrs"
                  v-on="inputHandlers"
                  placeholder="Mozzarella"
                  class="form-control w-50">
                <b-input-group-append>
                  <b-button @click="addTag()" variant="primary">Add</b-button>
                </b-input-group-append>
              </b-input-group>
              <ul
                id="my-custom-tags-list"
                class="list-unstyled d-inline-flex flex-wrap mt-2"
                aria-live="polite"
                aria-atomic="false"
                aria-relevant="additions removals"
              >
                <b-button
                  v-for="tag in tags"
                  :key="tag"
                  :id="`my-custom-tags-tag_${tag.replace(/\s/g, '_')}_`"
                  tag="li"
                  @click="removeTag(tag)"
                  class="mt-1 mr-2 pr-2"
                  variant="dark"
                  body-class="py-1 text-nowrap text-primary"
                >{{ tag }}
                </b-button>
              </ul>
            </template>
          </b-form-tags>
        </b-row>
      </b-container>

      <div class="fixed-bottom text-black-50 py-3">
        <b-container>
          Made by <a href="https://github.com/vaughanlove/" class="text-black"> Vaughan </a>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {
        newIngredient: '',
        ingredients: ['apple', 'orange', 'peach'],
        tags: ['apple', 'orange', 'peach'],
    }
  },
  methods: {
   addIngredient(){
     if (this.newIngredient !== ''){
       this.ingredients.push({id: 3, name: this.newIngredient, priority: 'low'});
     }
     this.newIngredient = '';
  }
  }
}
</script>

<style>

</style>
