<template>
    <div>
        <a class="back" @click.prevent="goBack">Précédent</a>
        <h2>Création d'un nouveau juré</h2>
        <div>
            <label for="first_name">Prénom</label>
            <input type="text" id="first_name" v-model="newUser.first_name">
            <br>
            <label for="last_name">Nom</label>
            <input type="text" id="last_name" v-model="newUser.last_name">
            <br>
            <label for="email">Email</label>
            <input type="email" id="email" v-model="newUser.email">
            <br>
            <label for="password">Mot de passe</label>
            <input type="password" id="password" @keyup.enter="createUser" v-model="newUser.password">
            <br>
            <label for="is_admin">Administrateur</label>
            <input type="checkbox" id="is_admin" v-model="newUser.is_admin">
            <br>
            <input class="button" type="submit" value="Ajouter le juré" @click.prevent="createUser">
        </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

export default {
  name: 'create-user',
  data() {
      return {
          newUser: {
              first_name: '',
              last_name: '',
              email: '',
              password: '',
              is_admin: false,
          }
      }
  },
  methods: {
      goBack() {
          router.push({ path: `/users` })
      },
      createUser() {
        this.$store.dispatch('createUser', this.newUser)
            .then((response) => {
                this.newStudent = {first_name: '', last_name: '', email: '', password: '', is_admin: false,}
                router.push({path: '/users'})
            }).catch((error) => {
                console.log(error)
            })
        }
  }
}
</script>
