<template>
  <div id="app">
    <navigation></navigation>
    <router-view/>
  </div>
</template>

<script>
import Navigation from "./components/Navigation.vue";
import { mapGetters, mapMutations } from "vuex";

export default {
  name: "App",
  components: {
    Navigation
  },
  computed: {
    ...mapGetters([
      "getState"
      ])
  },
  methods: {
    ...mapMutations([
      "setInitialValueOfState"
      ])
  },
  created() {
    let stateFromStorage = JSON.parse(localStorage.getItem("datas")) || [];
    this.setInitialValueOfState(stateFromStorage);
  },
  updated() {
    localStorage.setItem("datas", JSON.stringify(this.getState));
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
body {
}
</style>
