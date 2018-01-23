<template>
  <div>
    <h2>Gérer les jurés et administrateurs de l'application</h2>
    <div v-if="this.loading">
      Loading...
    </div>
    <ul v-else>
      <li v-for="user in this.getUsers" :key="user.id" @click.prevent="updateUser(user.id)">
        {{ user.first_name }} {{ user.last_name }}
        <!-- <div v-if="this.deploy">
          <img :src="student.profile_pic" alt="">
        </div> -->
      </li>
    </ul>
    <a class="button" @click.prevent="createUser">Ajouter un juré</a>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'


export default {
  name: 'users',
  data() {
    return {
      loading: true,
    }
  },
  computed: {
    ...mapGetters([
      'getUsers'
    ])
  },
  methods: {
    fetchUsers() {
      this.loading = true
      this.$store.dispatch('fetchAllUsers')
        .then((response) => {
          this.loading = false
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateUser() {
      console.log('updateUser')
    },
    createUser() {
      router.replace({path: '/users/add'})
    }
  },
  created() {
    this.fetchUsers()
  },
}
</script>
