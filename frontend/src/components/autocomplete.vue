<script>
import Vue from 'vue';
export default {
    data() {
        return {
            open: false,
            current: 0
        }
    },
    props: {
        suggestions: {
            type: Array,
            required: true
        },
        selection: {
            type: String,
            required: true,
            twoWay: true
        }
    },
    computed: {
        matches() {
            return this.suggestions.filter((str) => {
                return str.indexOf(this.selection) >= 0;
            });
        },
        openSuggestion() {
            return this.selection !== "" &&
                   this.matches.length != 0 &&
                   this.open === true;
        }
    },
    methods: {
        enter() {
            this.selection = this.matches[this.current];
            this.open = false;
        },
        up() {
            if(this.current > 0)
                this.current--;
        },
        down() {
            if(this.current < this.matches.length - 1)
                this.current++;
        },
        isActive(index) {
            return index === this.current;
        },
        change() {
            if (this.open == false) {
                this.open = true;
                this.current = 0;
            }
        },
        suggestionClick(index) {
            this.selection = this.matches[index];
            this.open = false;
        },
    }
}
</script>
<template>
  <div style="position:relative" v-bind:class="{'open':openSuggestion}">
      <input class="form-control" type="text" v-model="selection"
          @keydown.enter = 'enter'
          @keydown.down = 'down'
          @keydown.up = 'up'
          @input = 'change'
      />
      <ul class="dropdown-menu" style="width:100%">
          <li v-for="suggestion in matches"
              v-bind:class="{'active': isActive($index)}"
              @click="suggestionClick($index)"
          >
              <a href="#">{{ suggestion }}</a>
          </li>
      </ul>
  </div>
</template>

<style>
  form {
    display: flex;
  }

  /**
   * Autocomplete has a root div which wraps the
   * entire component, and messes up styling a
   * bit. Sorry!
   */
  form > div {
    flex: 1;
  }

  .autocomplete-input {
    border-top-right-radius: 0 !important;
    border-bottom-right-radius: 0 !important;
  }

  button {
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    border: 1px solid #ddd;
    padding: 16px;
    line-height: 1;
    background: #ddd;
    cursor: pointer;
    font-family: inherit;
    font-size: 13px;
    font-weight: normal;
    letter-spacing: .5px;
    text-transform: uppercase;
  }

  button:focus {
    outline: none;
    border-color: #ccc;
    background: #ccc;
  }

  pre {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    overflow: auto;
    padding: 24px;
  }
</style>