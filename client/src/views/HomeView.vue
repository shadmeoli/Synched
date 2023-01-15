<template>


  <LandingPage />

</template>

<script lang="ts">
import { defineComponent } from 'vue';

// Components
import LandingPage from '../components/LandingPage.vue'

export default defineComponent({
  name: 'HomeView',

  components: {
    LandingPage
  },
});
</script>
