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
    let stateFromStorage = JSON.parse(localStorage.getItem('store')) || []
    this.setInitialValueOfState(stateFromStorage)
  },
  beforeUpdate() {
    localStorage.setItem('store', JSON.stringify(this.getState));
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
  font-family: "Dosis", Helvetica, Arial, sans-serif;
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
sup {
  vertical-align: super;
  font-size: smaller;
}
.h2-like {
  font-family: 'Dosis', Helvetica, Arial, sans-serif;
  font-weight: 600;
  color: #2C003D;
  letter-spacing: 1px;
  font-size: 1.25rem;
  margin: 0 0 1em 0;
  display: inline-block;
}

.button {
  padding: 1em 2em;
  background-color: #C11843;
  color: white;
  display: inline-block;
  border: none;
  border-radius: 3em;
  margin: 0.5em;
  font-size: 16px;
  font-weight: 600;
  font-family: "Dosis", Helvetica, arial, sans-serif;
  letter-spacing: 1px;
  cursor: pointer;
  box-shadow: 0 2px 10px 0 rgba(0,0,0,0.5);
}

li {
  padding: 0.5em 1em;
  margin-bottom: 1em;
  color: #2C003D;
  font-weight: 500;
  background-color: #FBFAFB;
  cursor: pointer;
}

</style>
