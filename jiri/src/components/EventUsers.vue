<template>
    <div>
        <h2>Ajout de jurés</h2>
        <div v-if="this.loading">
            Loading...
        </div>
        <div v-else>
          <select v-model="selectedUserId">
            <option v-for="user in this.remainingUsers" :key="user.id" :value="user.id">
              {{ user.first_name }} {{ user.last_name }}
            </option>
          </select>
          <input type="submit" @click.prevent="addSelectedUser" value="Ajouter le juré">

          <h2>Jurés déjà ajoutés</h2>
          <div v-if="this.users == false">
            Vous n'avez pas encore ajouté de juré
          </div>
          <ul v-else>
            <li v-for="user in this.users" :key="user.id" @click.prevent="updateUser(user.id)">
              {{ user.first_name }} {{ user.last_name }}
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
  name: 'event-users',
  props: ['event'],
  data() {
    return {
      loading: true,
      selectedUserId: undefined,
      users: [],
      info: {
        usersId: this.event.users,
      },
      remainingUsers: [],
    }
  },
  computed: {
    ...mapGetters([
      'getUsers'
    ])
  },
  methods: {
    next() {
      router.push({path: '/events/add/recap'})
    },
    fetchUsers() {
      this.loading = true
      this.$store.dispatch('fetchAllUsers')
        .then((response) => {
          this.loading = false
          this.selectedUserId = this.remainingUsers[0].id
        })
        .catch((error) => {
          console.log(error)
        })
    },
    addSelectedUser() {
      if(this.selectedUserId == undefined) {
        console.log('Vous devez sélectionner un juré!')
        return
      }
      if(this.info.usersId.find((user) => user == this.selectedUserId)) {
        console.log('Le juré a déjà été ajouté')
      } else {
        this.info.usersId.push(this.selectedUserId)

        let selectedUser = this.getUsers.find((user) => {
          return user.id == this.selectedUserId
        })
        this.users.push(selectedUser)

        let userIndex = this.remainingUsers.findIndex((user) => {
          return user.id == selectedUser.id
        })
        this.remainingUsers.splice(userIndex, 1)
        if(this.remainingUsers != false) {
          this.selectedUserId = this.remainingUsers[0].id
        } else {
          this.selectedUserId = undefined
        }
      }
    },
    updateUser() {
      console.log('updateUser')
    },
  },
  created() {
    this.fetchUsers()
    let selectedUsers = this.getUsers.filter((user) => {
          return this.info.usersId.includes(user.id) 
    })
    this.users = selectedUsers
    this.remainingUsers = this.getUsers
  },
  updated() {
    this.$emit('update', this.info)
  },
}
</script>