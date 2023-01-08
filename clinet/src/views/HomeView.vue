<template>
  <search />
</template>

<script>
import { defineComponent } from 'vue';

// Components
import search from '../components/search.vue';

export default defineComponent({
  name: 'HomeView',

  components: {
    search,
  },
});
</script>
