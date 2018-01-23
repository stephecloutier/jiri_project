<template>
<div>
    <h2>Ajout d'étudiants</h2>
  <div v-if="this.loading">
      Loading...
  </div>
  <div v-else>
    <select v-model="selectedStudentId">
      <option v-for="student in this.remainingStudents" :key="student.id" :value="student.id">
        {{ student.first_name }} {{ student.last_name }}
      </option>
    </select>
    <input type="submit" @click.prevent="addSelectedStudent" value="Ajouter l'étudiant">

    <h2>Étudiants déjà ajoutés</h2>
    <div v-if="this.students == false">
      Vous n'avez pas encore ajouté d'étudiants
    </div>
    <ul v-else>
      <li v-for="student in this.students" :key="student.id" @click.prevent="updateStudent(student.id)">
        {{ student.first_name }} {{ student.last_name }}
      </li>
    </ul>
  </div>
  <a  class="button" @click.prevent="next">Suite</a>
</div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

export default {
  name: 'event-students',
  props: ['event'],
  data() {
    return {
      loading: true,
      selectedStudentId: undefined,
      students: [],
      remainingStudents: [],
      info: {
        studentsId: this.event.students,
      },
    }
  },
  computed: {
    ...mapGetters([
      'getStudents'
    ])
  },
  methods: {
    next() {
      router.push({path: '/events/add/users'})
    },
    fetchStudents() {
      this.loading = true
      this.$store.dispatch('fetchAllStudents')
        .then((response) => {
          this.loading = false
          this.selectedStudentId = this.remainingStudents[0].id
        })
        .catch((error) => {
          console.log(error)
        })
    },
    addSelectedStudent() {
      if(this.selectedStudentId == undefined) {
        console.log('Vous devez sélectionner un étudiant!')
        return
      }
      if(this.info.studentsId.find((student) => student == this.selectedStudentId)) {
        console.log('L\'étudiant a déjà été ajouté')
      } else {
        this.info.studentsId.push(this.selectedStudentId)
        let selectedStudent = this.getStudents.find((student) => {
          return student.id == this.selectedStudentId
        })
        this.students.push(selectedStudent)
        let studentIndex = this.remainingStudents.findIndex((student) => {
          return student.id == selectedStudent.id
        })
        this.remainingStudents.splice(studentIndex, 1)
        if(this.remainingStudents != false) {
          this.selectedStudentId = this.remainingStudents[0].id
        } else {
          this.selectedStudentId = undefined
        }
      }
    },
    updateStudent() {
      console.log('updateStudent')
    },
  },
  created() {
    this.fetchStudents()
    let selectedStudents = this.getStudents.filter((student) => {
          return this.info.studentsId.includes(student.id) 
    })
    this.students = selectedStudents
    this.remainingStudents = this.getStudents
  },
  updated() {
    this.$emit('update', this.info)
  },
}
</script>