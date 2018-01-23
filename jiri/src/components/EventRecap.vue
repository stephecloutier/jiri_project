<template>
  <div>
      <h2>
        <span class="recap-title">Épreuve&nbsp;:</span> {{ this.recap.course_name || '' }}
        <span class="recap-error" v-if="!this.recap.course_name">Vous devez fournir le <a class="error-redirect" title="Modifier le nom du cours" @click.prevent="navigate('info')">nom du cours</a></span>
      </h2>

      <p class="h2-like">
        <span class="recap-title">Session de l'épreuve&nbsp;:</span> {{ this.recap.exam_session || '' }}
        <span class="recap-error" v-if="!this.recap.exam_session">Vous devez fournir la <a class="error-redirect" title="Modifier la session de l'épreuve" @click.prevent="navigate('info')">session de l'épreuve</a></span>
      </p>

      <p class="h2-like">
        <span class="recap-title">Date de l'épreuve&nbsp;:</span> {{ this.recap.exam_date || '' }}
          <span class="recap-error" v-if="!this.recap.exam_date">Vous devez fournir la <a class="error-redirect" title="Modifier la date de l'épreuve" @click.prevent="navigate('info')">date de l'épreuve</a></span>
      </p>

      <div class="recap-projects">
        <span class="recap-title recap-list-title">Travaux</span>
        <ul v-if="this.recap.projects != false">
          <li v-for="project in this.projects" :key="project.id">
            {{ project.name }}
          </li>
        </ul>
        <span class="recap-error" v-else>
          Vous devez <a class="error-redirect" title="Modifier les travaux de l'épreuve" @click.prevent="navigate('projects')">ajouter des travaux à l'épreuve</a>
        </span>
      </div> 

      <div class="recap-students">
        <span class="recap-title recap-list-title">Étudiants</span>
        <ul v-if="this.recap.students != false">
          <li v-for="student in this.students" :key="student.id">
            {{ student.first_name + ' ' + student.last_name }}
          </li>
        </ul>
        <span class="recap-error" v-else>
          Vous devez <a class="error-redirect" title="Modifier les étudiants de l'épreuve" @click.prevent="navigate('students')">ajouter des étudiants à l'épreuve</a>
        </span>
      </div> 

        <div class="recap-users">
        <span class="recap-title recap-list-title">Jurés</span>
        <ul v-if="this.recap.users != false">
          <li v-for="user in this.users" :key="user.id">
            {{ user.first_name + ' ' + user.last_name }}
          </li>
        </ul>
        <span class="recap-error" v-else>
          Vous devez <a class="error-redirect" title="Modifier les jurés de l'épreuve" @click.prevent="navigate('users')">ajouter des jurés à l'épreuve</a>
        </span>
      </div> 

      <div class="recap-validation-errors recap-error" v-if="this.validationErrors">
        Vous devez corriger les erreurs avant d'enregistrer l'épreuve
      </div>
      <a @click.prevent="save">Enregistrer</a>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

export default {
  name: 'event-recap',
  props: ['event'],
  data() {
      return {
          recap: {
              course_name: this.event.course_name,
              exam_session: this.event.exam_session,
              exam_date: this.event.exam_date,
              projects: this.event.projects,
              students: this.event.students,
              users: this.event.users,
          },
          projects: [],
          students: [],
          users: [],
          validationErrors: false,
      }
  },
  computed: {
    ...mapGetters([
      'getProjects',
      'getStudents',
      'getUsers',
    ])
  },
  methods: {
    retrieveIdInfos() {
      this.students = this.getStudents.filter((student) => {
          return this.recap.students.includes(student.id) 
      })
      this.projects = this.getProjects.filter((project) => {
          return this.recap.projects.includes(project.id) 
      })
      this.users = this.getUsers.filter((user) => {
          return this.recap.users.includes(user.id) 
      })
    },
    save() {
      console.log('saving')
      if(!this.recap.course_name || !this.recap.exam_session || !this.recap.exam_date || this.recap.students == false || this.recap.projects == false || this.recap.users == false) {
        this.validationErrors = true
        return
      }
    },
    navigate(path) {
      if(path == 'info') {
        router.push({path: '/events/add/'})
      } else {
        router.push({path: '/events/add/'+ path})
      }
    }
  },
  created() {
    this.retrieveIdInfos()
    this.validationErrors = false
  }
}
</script>

<style>
  .recap-error {
    display: inline-block;
    color: red;
    font-weight: 600;
    text-transform: none;
    letter-spacing: 0;
    font-size: 1rem;
    margin-top: 0.5em;
  }
  .recap-title {
    letter-spacing: 0;
    font-weight: 600;
    text-transform: none;
    font-size: 1.25rem;
  }
  .recap-list-title {
    display: block;
  }
  .recap-projects, .recap-students, .recap-users {
    margin-top: 0.5rem;
    margin-bottom: 0;
  }
  .error-redirect {
    text-decoration: underline;
    cursor: pointer;
    transition: 0.2s ease-out;
  }
  .error-redirect:hover {
    color: darkred
  }
  .h2-like {
    font-family: 'Dosis', Helvetica, Arial, sans-serif;
    font-weight: 600;
    color: #2C003D;
    letter-spacing: 1px;
    font-size: 1.25rem;
    margin: 0;
  }

</style>
