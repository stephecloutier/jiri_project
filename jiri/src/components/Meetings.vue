<template>
    <div>
        <h1>Bravo tu es connecté, non administrateur !</h1>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    //import router from '../router'

    export default {
        name: 'meetings',
        computed: {
            ...mapGetters([
                // 'getToken',
            ]),
        },
        created () {
            //this.$store.dispatch('getHome')
        },
    }
</script>

<!--
<template>
  <div class="post">
    <div class="loading" v-if="loading">
      Loading...
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="post" class="content">
      <h2>{{ post.title }}</h2>
      <p>{{ post.body }}</p>
    </div>
  </div>
</template>-->

// export default {
//   data () {
//     return {
//       loading: false,
//       post: null,
//       error: null
//     }
//   },
//   created () {
//     // fetch the data when the view is created and the data is
//     // already being observed
//     this.fetchData()
//   },
//   watch: {
//     // call again the method if the route changes
//     '$route': 'fetchData'
//   },
//   methods: {
//     fetchData () {
//       this.error = this.post = null
//       this.loading = true
//       // replace `getPost` with your data fetching util / API wrapper
//       getPost(this.$route.params.id, (err, post) => {
//         this.loading = false
//         if (err) {
//           this.error = err.toString()
//         } else {
//           this.post = post
//         }
//       })
//     }
//   }
// }
