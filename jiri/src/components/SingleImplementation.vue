<template>
    <div>
        <a  class="back" @click.prevent="navigate('meetings/' + getCurrentMeeting.id)">Retour</a>
        <h2>Rencontre avec {{ this.getCurrentStudent.first_name + ' ' + this.getCurrentStudent.last_name }}</h2>
        <div class="project-infos">
            <span class="h2-like">{{ this.project.name }}</span>
            <p>{{ this.project.description }}</p>
        </div>
        <div v-if="this.loading">
            Loading...
        </div>
        <div class="score-infos" v-else>
            <label for="score">Cote / 20</label>
            <input id="score" type="number" max="20" min="0" step=".01" v-model="score.score">
            <br>
            <label for="comment">Commentaire</label>
            <textarea id="comment" cols="30" rows="10" v-model="score.comment"></textarea>
            <br>
            <input class="button"  type="submit" value="Enregistrer" @click.prevent="saveScore">
        </div>
        <!-- <div class="loading" v-if="loading">
            Loading...
        </div>
        <div v-else>
            infos
        </div> -->
    </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

export default {
  name: 'single-implementation',
  data() {
      return {
          loading: false,
          project: {},
          score: {
              score: undefined,
              comment: '',
          },
          scoreAlreadyExists: false
      }
  },
  computed: {
      ...mapGetters([
          'getState',
          'getCurrentStudent',
          'getCurrentImplementation',
          'getProjects',
          'getCurrentMeeting',
      ]),
  },
  methods: {
      setProjectInfo() {
          this.project = this.getProjects.find((project) => {
              return project.id == this.getCurrentImplementation.project
          })
      },
      setCurrentScore() {
          this.loading = true
          let requestInfos = {
              meeting: this.getCurrentMeeting.id,
              implementation: this.getCurrentImplementation.id,
          }
          this.$store.dispatch('getCurrentScore', requestInfos)
            .then((response) => {
                this.loading = false
                if(response) {
                    this.score.score = response.score
                    this.score.comment = response.comment
                    this.scoreAlreadyExists = true
                }
            }).catch((error) => {
                this.loading = false
                // console.log(error)
            })
      },
      saveScore() {
          let scoreInfos = {
              score: this.score.score,
              comment: this.score.comment,
              meeting: this.getCurrentMeeting.id,
              implementation: this.getCurrentImplementation.id,
          }
          if(!scoreInfos.score || !scoreInfos.comment) {
              console.log('Vous devez entrer un score et un commentaire avant d\'enregistrer')
              return
          }
          if(this.scoreAlreadyExists) {
                this.$store.dispatch('updateScore', scoreInfos)
                router.push({path: `/meetings/${this.getCurrentMeeting.id}`})
                return
          }
          this.$store.dispatch('saveScore', scoreInfos)
            .then((response) => {
                router.push({path: `/meetings/${this.getCurrentMeeting.id}`})
            }).catch((error) => {
                console.log(error)
            })
      },
       navigate(path) {
            router.push({path: '/' + path})
        }
  },
  created() {
      this.setProjectInfo()
      this.setCurrentScore()
  },
}
</script>
