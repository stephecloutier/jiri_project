<template>
<div>
  <h2>Ajout de travaux</h2>
  <div v-if="this.loading">
      Loading...
  </div>
  <div v-else>
    <select v-model="selectedProjectId">
      <option v-for="project in this.remainingProjects" :key="project.id" :value="project.id">
        {{ project.name }}
      </option>
    </select>
    <input type="submit" @click.prevent="addSelectedProject" value="Ajouter le travail">

    <h2>Travaux déjà ajoutés</h2>
    <div v-if="this.projects == false">
      Vous n'avez pas encore ajouté de travaux
    </div>
    <ul v-else>
      <li v-for="project in this.projects" :key="project.id" @click.prevent="updateProject(project.id)">
        {{ project.name }}
      </li>
    </ul>
  </div>
  
  <a @click.prevent="next">Suite</a>
</div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

export default {
  name: 'event-projects',
  props: ['event'],
  data() {
    return {
      loading: true,
      selectedProjectId: undefined,
      projects: [],
      remainingProjects: [],
      info: {
        projectsId: this.event.projects,
      },
    }
  },
  computed: {
    ...mapGetters([
      'getProjects'
    ])
  },
  methods: {
    next() {
      router.push({path: '/events/add/students'})
    },
    fetchProjects() {
      this.loading = true
      this.$store.dispatch('fetchAllProjects')
        .then((response) => {
          this.loading = false
          this.selectedProjectId = this.remainingProjects[0].id
        })
        .catch((error) => {
          console.log(error)
        })
    },
    addSelectedProject() {
      if(this.selectedProjectId == undefined) {
        console.log('Vous devez sélectionner un projet!')
        return
      }
      if(this.info.projectsId.find((project) => project == this.selectedProjectId)) {
        console.log('Le travail a déjà été ajouté')
      } else {
        this.info.projectsId.push(this.selectedProjectId)
        let selectedProject = this.getProjects.find((project) => {
          return project.id == this.selectedProjectId
        })
        this.projects.push(selectedProject)
        let projectIndex = this.remainingProjects.findIndex((project) => {
          return project.id == selectedProject.id
        })
        this.remainingProjects.splice(projectIndex, 1)
        if(this.remainingProjects != false) {
          this.selectedProjectId = this.remainingProjects[0].id
        } else {
          this.selectedProjectId = undefined
        }
      }
    },
    updateProject() {
      console.log('updateProject')
    },
  },
  created() {
    this.fetchProjects()
    let selectedProjects = this.getProjects.filter((project) => {
          return this.info.projectsId.includes(project.id) 
    })
    this.projects = selectedProjects
    this.remainingProjects = this.getProjects
  },
  updated() {
    this.$emit('update', this.info)
  },
}
</script>
