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
        </div>
      </header>

      <main class="px-lg-0">
        <h1 class="text-danger font-weight-bolder  mt-5 mb-3 ">supper</h1>
        <p class="pt-sm-2 my-0 py-0">welcome, still new (buggy) but functional.</p>
        <p class="pt-sm-2 mt-0 py-0">what's in your fridge?</p>
        <p class="lead">
          <a href="#" class="btn btn-md btn-primary fw-bold border-secondary bg-secondary my-5">start</a>
        </p>
      </main>
      <div class="footer-copyright text-center text-black-50 py-3">
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
        recipe: {
          'name': '',
          'url': '',
        },
        recipes: []
    }
  },
  async created(){
    var response = await fetch('http://127.0.0.1:8000/api/recipes/');
    this.recipes = await response.json();
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
