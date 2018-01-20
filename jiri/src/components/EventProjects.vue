<template>
<div>
  <h2>Ajout de travaux</h2>
  <a @click.prevent="next">Suite</a>
</div>
</template>

<script>
import {router} from '../router'

export default {
  name: 'event-projects',
  methods: {
    next() {
      router.push({path: '/events/add/students'})
    }
  }
}
</script>
