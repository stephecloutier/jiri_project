<template>
  <div>
      <h2>Récapitulatif</h2>
      <a @click.prevent="save">Enregistrer</a>
  </div>
</template>

<script>
export default {
  name: 'event-recap',
  methods: {
    save() {
      console.log('saving')
    }
  }
}
</script>
