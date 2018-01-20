<template>
    <div>
        <p>
          <router-link to="/events/add/">Informations</router-link>
          <router-link to="/events/add/projects">Travaux</router-link>
          <router-link to="/events/add/students">Étudiants</router-link>
          <router-link to="/events/add/users">Jurés</router-link>
          <router-link to="/events/add/recap">Récapitulatif</router-link>
        </p>
        <router-view></router-view>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

export default {
  name: 'create-event',
  data() {
      return {
          event: {
              course_name: '',
              exam_session: undefined,
              exam_data: undefined,
              projects: {},
              students: {},
              users: {},
          }
      }
  },
  methods: {
      // createProject() {
      //   this.$store.dispatch('createProject', this.project)
      //       .then((response) => {
      //           console.log(response)
      //           this.project = {title: '', description: '', weight: undefined}
      //           router.push({path: '/projects'})
      //       }).catch((error) => {
      //           console.log(error)
      //       })
      //   }
  }
}
</script>
