<template>
  
  <!-- search bar for song serching -->
   <v-responsive
    class="mt-5 mx-auto"
    max-width="500"
    >
    <!-- the search text field -->
    <v-text-field
      id="songSearch"
      v-model="song_search"
      elevation=0
      max-width=2
      rounded="lg"
      variant="solo"
      filled
      color="black"
      placeholder="search song"
      append-inner-icon="mdi-magnify"
      persistent-hint
      >
      <!-- search button -->
      <template v-slot:append>
          <v-btn @click="songSearch" tile elevation=0 v-ripple color="pink" >search</v-btn>
      </template>

      <!-- showing search result -->


      <v-snackbar
      v-model="snackbar"
      text-color="white"
    >
      {{ text }}

      <template v-slot:actions>
        <v-btn
          color="pink lighten-4"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>

    </v-snackbar>
      </v-text-field>

      <!-- adding more filter options  -->
        <v-chip-group
            justify="center"
            aligh-items="left"
            fliter
            column
            variant="solo"
            elevation=5
            class="mt-5" 
            color="pink" 
            text-color="white"
          >
            <v-chip
              v-for="tag in tags"
              :key="tag"
            >
              {{ tag }}
            </v-chip>
          </v-chip-group>
    </v-responsive>

</template>

<script>
import { defineComponent } from 'vue';
import searchResult from './search_results.vue';


export default defineComponent({
  name: 'search',

  // additional components
  components: {
    searchResult,
  },

  data: () => ({

    searchSong: '',
    snackbar: false,
    text: "Searching the web",
    tags: [
      "BPM",
      "GENRE",
      "COUNTRY",
      "POPULARITY"
    ],
  }),

  // the search call to the API
  methods: {
    

    async songSearch() {
      alert(this.song_search)

    }
  }
  
});
</script>
