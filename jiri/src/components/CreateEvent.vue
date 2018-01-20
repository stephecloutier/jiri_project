<template>
    <div>
        <p>
          <router-link to="/events/add/">Informations</router-link>
          <router-link to="/events/add/projects">Travaux</router-link>
          <router-link to="/events/add/students">Étudiants</router-link>
          <router-link to="/events/add/users">Jurés</router-link>
          <router-link to="/events/add/recap">Récapitulatif</router-link>
        </p>
        <router-view v-bind:event="this.event" @update="onUpdate"></router-view>
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
              exam_date: undefined,
              projects: {},
              students: {},
              users: {},
          }
      }
  },
  methods: {
    onUpdate(data) {
      this.event.course_name = data.course_name
      this.event.exam_session = data.exam_session
      this.event.exam_date = data.exam_date
      //this.event = {...this.event, data.course_name}
    }
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
