<template>
    <div>
        <p>
          <router-link to="/events/add/">Informations</router-link>
          <router-link to="/events/add/projects">Travaux</router-link>
          <router-link to="/events/add/students">Étudiants</router-link>
          <router-link to="/events/add/users">Jurés</router-link>
          <router-link to="/events/add/recap">Récapitulatif</router-link>
        </p>
        <router-view v-bind:event="this.event" @update="onUpdate" @save="createEvent"></router-view>
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
              projects: [],
              students: [],
              users: [],
              isBeingCreated: false,
          },
          isEventCreated: false,
          implementations: [],
      }
  },
  methods: {
    onUpdate(data) {
      if(data.course_name) this.event.course_name = data.course_name
      if(data.exam_session) this.event.exam_session = data.exam_session
      if(data.exam_date) this.event.exam_date = data.exam_date
      if(data.project) this.event.projects = data.projectsId
    },
    createEvent() {
      this.event.isBeingCreated = true,

      this.$store.dispatch('createEvent', this.event)
          .then((response) => {
            console.log(this.event.projects)
            this.addImplementations(response.data.id)
            this.$store.dispatch('createImplementations', this.implementations)
              .then((response) => {
                console.log(response)
                this.isEventCreated = true,
                router.push({path: '/events'})
              }).catch((error) => {
                console.log(error)
              })
          }).catch((error) => {
              console.log(error)
          })
      },
      addImplementations(eventId) {
        this.event.students.forEach((student) => {
          this.event.projects.forEach((project) => {
            this.implementations.push({ student: student, project: project, event: eventId })
          })
        })
      }
  },
  beforeRouteLeave (to, from , next) {
    if(this.isEventCreated) {
      next()
    } else {
      const answer = window.confirm('Voulez-vous vraiment quitter la création de l\'épreuve?')
        if (answer) {
          next()
        } else {
          next(false)
        }
    }
    
  }
}
</script>
