<template>
    <div>
        <a @click.prevent="goBack">Précédent</a>
        <h2>Création d'un nouvel étudiant</h2>
        <div>
            <label for="first_name">Prénom</label>
            <input type="text" id="first_name" v-model="newStudent.first_name">
            <br>
            <label for="last_name">Nom</label>
            <input type="text" id="last_name" @keyup.enter="createStudent" v-model="newStudent.last_name">
            <br>
            <input type="submit" value="Ajouter l'étudiant" @click.prevent="createStudent">
        </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import router from '../router'

export default {
  name: 'create-student',
  data() {
      return {
          newStudent: {
              first_name: '',
              last_name: '',
          }
      }
  },
  methods: {
      goBack() {
          router.push({ path: `/students` })
      },
      createStudent() {
        this.$store.dispatch('createStudent', this.newStudent)
            .then((response) => {
                this.newStudent = {first_name: '', last_name: ''}
                router.push({path: '/students'})
            }).catch((error) => {
                console.log(error)
            })
        }
  }
}
</script>
