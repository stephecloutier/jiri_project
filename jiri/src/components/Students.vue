<template>
  <div>
    <h2>Gérer les étudiants à ajouter aux épreuves</h2>
    <div v-if="this.loading">
      Loading...
    </div>
    <ul v-else>
      <li v-for="student in this.getStudents" :key="student.id" @click.prevent="updateStudent(student.id)">
        {{ student.first_name }} {{ student.last_name }}
        <!-- <div v-if="this.deploy">
          <img :src="student.profile_pic" alt="">
        </div> -->
      </li>
    </ul>
    <a @click.prevent="createStudent">Ajouter un étudiant</a>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import router from '../router'


export default {
  name: 'students',
  data() {
    return {
      loading: true,
      deploy: false,
    }
  },
  computed: {
    ...mapGetters([
      'getStudents'
    ])
  },
  methods: {
    fetchStudents() {
      this.loading = true
      this.$store.dispatch('fetchAllStudents')
        .then((response) => {
          this.loading = false
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deployStudent(id) {
      //this.deploy = true
    },
    updateStudent() {
      console.log('updateStudent')
    },
    createStudent() {
      router.replace({path: '/students/add'})
      console.log('createStudent')
    }
  },
  created() {
    console.log('Student created')
    this.fetchStudents()
  },
}
</script>
