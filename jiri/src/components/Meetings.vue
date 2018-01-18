<template>
    <div>
        <h1>Bravo tu es connecté, non administrateur !</h1>

        <div class="loading" v-if="loading">
            Loading...
        </div>

        <div class="errors" v-if="getErrors">
            <span v-for="error in getErrors" :key="error.index">{{ error }}</span>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'

    export default {
        name: 'meetings',
        data() {
            return {
                loading: false,
            }
        },
        computed: {
            ...mapGetters([
                'getErrors',
            ]),
        },
        created () {
            // have to get data for the CURRENT event (or closest)
            this.fetchData()
        },
        methods: {
            fetchData() {
                this.loading = true
                this.$store.dispatch('fetchEvent')
                    .then((response) => {
                        this.loading = false
                        console.log(response)
                    }).catch((error) => {
                        console.log(error)
                    })
            }
        }
    }
</script>
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
