<template>
  <v-app>

    <!-- the app bar -->
    <div>
      <v-toolbar
        color="cyan-darken-2"
        dark
        temporary
      >

        <v-toolbar-title>Synched</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn plain class="ml-10" @click.stop = "sign_up = true" >
         sign up
        </v-btn>

        <v-btn plain @click.stop = "log_in = true" >
         sign in
        </v-btn>

      </v-toolbar>
    </div>
    <!-- ------------------ -->

    <!-- registration popup -->
    <v-dialog
      v-model="sign_up"
      max-width="500"
    >
      <v-card>
        <v-card-title class="text-h5">
          User sign up
        </v-card-title>

       <v-card elevation="0" class="mx-9 px-6 py-8" max-width="auto">
      <v-form
        v-model="form"
        @submit.prevent="onSubmit"
      >
        <v-text-field
          v-model="username"
          :readonly="loading"
          :rules="[required]"
          class="mb-2"
          clearable
          label="Username"
        ></v-text-field>

        <v-text-field
          v-model="email"
          :readonly="loading"
          :rules="[required]"
          class="mb-2"
          clearable
          label="Email"
          type="email"
          placeholder="Enter your email addres"
        ></v-text-field>

        <v-text-field
          v-model="password"
          :readonly="loading"
          :rules="[required]"
          clearable
          label="Password"
          type="password"
          placeholder="Enter your password"
        ></v-text-field>

        <br>

        <v-btn
          :disabled="!form"
          :loading="loading"
          block
          color="success"
          size="large"
          type="submit"
          variant="elevated"
        >
          Sign up
        </v-btn>
      </v-form>
    </v-card>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="sign_up = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <!-- login popup -->
    <v-dialog
      v-model="log_in"
      max-width="290"
    >
      <v-card>
        <v-card-title class="text-h5">
          Use Google's location service?
        </v-card-title>

        <v-card-text>
          Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="log_in = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="log_in = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>



    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App',

  data () {
    return {

      drawer: false,
      group: null,
      sign_up: '',
      log_in: '',
      
    }
  },

  // hook
  watch: {
    group() {
      this,drawer = false
    },
  },
})
</script>
