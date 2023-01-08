<template>
  
  <!-- search bar for song serching -->
   <v-responsive
    class="mt-5 mx-auto"
    max-width="400"
    >
    <!-- the search text field -->
    <v-text-field
      id="songSearch"
      max-width=2
      rounded="lg"
      variant="outlined"
      filled
      color="black"
      placeholder="search song"
      append-inner-icon="mdi-magnify"
      >
      <!-- search button -->
      <template v-slot:append>
          <v-btn @click="search" tile elevation=0 v-ripple color="pink" >search</v-btn>
      </template>

      <v-snackbar
      v-model="snackbar"
    >
      {{ text }}

      <template v-slot:actions>
        <v-btn
          color="pink"
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
  <!-- </v-col> -->


</template>

<script>
import { defineComponent } from 'vue';


export default defineComponent({
  name: 'search',


  data: () => ({
    snackbar: false,
    text: "Searching the web for ${songSearch}.",
    tags: [
      "BPM",
      "GENRE",
      "COUNTRY",
      "POPULARITY"
      ],
  }),

  // the search call to the API
  methods: {
    search() {
      this.snackbar = true

    }
  }
  
});
</script>
