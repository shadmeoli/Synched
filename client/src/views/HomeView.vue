<template>


  <v-form>
    <v-card height="10">
    <v-text-field type="email" v-model="password" solo elevation="10" width="10dp"></v-text-field>
  </v-card>
  </v-form>

</template>

<script lang="ts">
import { defineComponent } from 'vue';

// Components
import WelcomeItem from '../components/WelcomeItem.vue'

export default defineComponent({
  name: 'HomeView',

  components: {
    WelcomeItem
  },
});
</script>
