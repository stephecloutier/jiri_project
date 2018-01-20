<template>
    <div>
        <a @click.prevent="goBack">Précédent</a>
        <h2>Création d'un nouveau travail</h2>
        <div>
            <label for="title">Nom du travail</label>
            <input type="text" id="title" v-model="project.title">
            <br>
            <label for="description">Description</label>
            <textarea id="description" cols="30" rows="10" v-model="project.description"></textarea>
            <br>
            <label for="weight">Pondération par défaut</label>
            <input type="number" id="weight" v-model="project.weight" min="0" max="1" step=".01" placeholder="0,3">
            <br>
            <input type="submit" value="Ajouter le travail" @click.prevent="createProject">
        </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

export default {
  name: 'create-project',
  data() {
      return {
          project: {
              title: '',
              description: '',
              weight: undefined,
          }
      }
  },
  methods: {
      goBack() {
          router.push({ path: `/projects` })
      },
      createProject() {
        this.$store.dispatch('createProject', this.project)
            .then((response) => {
                console.log(response)
                this.project = {title: '', description: '', weight: undefined}
                router.push({path: '/projects'})
            }).catch((error) => {
                console.log(error)
            })
        }
  }
}
</script>
