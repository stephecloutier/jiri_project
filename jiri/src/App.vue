<template>
  <div id="app">
    <header class="header">
      <navigation></navigation>
    </header>
    <main class="main">
      <router-view/>
    </main>
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
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  background-color: white;
  font-size: 16px;
}
.header {
  background: linear-gradient(to bottom, #2C003D, #410034);
  min-height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 20px;
}
.main {
  margin: 0 auto;
  text-align: left;
  max-width: 70%;
  width: 70%;
}
h2 {
  text-transform: uppercase;
  font-family: 'Dosis', Helvetica, Arial, sans-serif;
  font-weight: 600;
  color: #2C003D;
  letter-spacing: 2px;
  font-size: 1.5rem;
  margin: 1em 0 0.5em;
}
</style>
