<template>
    <div>
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <div class="main-content" v-else>
            <h2>Rencontrer un étudiant</h2>
            <select name="students" v-model="selectedStudentId">
                <option v-for="student in this.getCurrentEventStudentsList" :key="student.id" :value="student.id" selected>
                    {{ student.first_name + ' ' + student.last_name }}
                </option>
            </select>
            <input type="submit" value="Débuter la rencontre">
        </div>

        <!-- to handle later
        <div class="errors" v-if="getErrors">
            <span v-for="error in getErrors" :key="error.index">{{ error }}</span>
        </div>-->
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'

    export default {
        name: 'meetings',
        data() {
            return {
                loading: false,
                selectedStudentId: null,
            }
        },
        computed: {
            ...mapGetters([
                'getErrors',
                'getCurrentEventStudentsList'
            ]),
        },
        created () {
            this.fetchData()
        },
        methods: {
            fetchData() {
                this.loading = true
                this.$store.dispatch('fetchClosestEvent')
                    .then((response) => {
                        this.$store.dispatch('fetchCurrentEventStudentsList')
                            .then((response) => {
                                this.selectedStudentId = this.getCurrentEventStudentsList[0].id
                                this.loading = false
                            }).catch((error) => {
                                console.log(error)
                            })

                    }).catch((error) => {
                        console.log(error)
                    })
            },
            changeSelectedStudent($event) {
                this.selectedStudent = $event
                console.log($event)
            },
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
