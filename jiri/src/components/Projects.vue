<template>
  <div>
    <h2>Gérer les travaux à ajouter aux épreuves</h2>
    <div v-if="this.loading">
      Loading...
    </div>
    <ul v-else>
      <li v-for="project in this.getProjects" :key="project.id" @click.prevent="updateProject(project.id)" v-if="!project.is_default">
        {{ project.name }}
      </li>
    </ul>
    <a @click.prevent="createProject">Créer un travail</a>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'


export default {
  name: 'projects',
  data() {
    return {
      loading: true,
    }
  },
  computed: {
    ...mapGetters([
      'getProjects'
    ])
  },
  methods: {
    fetchProjects() {
      this.loading = true
      this.$store.dispatch('fetchAllProjects')
        .then((response) => {
          this.loading = false
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateProject() {
      console.log('updateProject')
    },
    createProject() {
      router.replace({path: '/projects/add'})
    }
  },
  created() {
    this.fetchProjects()
  },
}
</script>
