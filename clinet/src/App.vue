<template>
  <v-app dark>
    <!-- adding the nav bar for all screes -->
    <v-app-bar
        color="pink"
        elevation=0
      >
        <v-app-bar-title>SYNCHED</v-app-bar-title>

        <template v-slot:append>

          <v-btn icon elevation=5 @click.stop="drawer = !drawer">
            <v-avatar
              color="white"
              size="large"
            >
            <v-icon>mdi-account</v-icon>
          </v-avatar>
          </v-btn>
        </template>

      </v-app-bar>
      <v-navigation-drawer
        v-model="drawer"
        class="gray"
        theme="light"
        temporary
      >
            <v-btn variant="plain" height=45 class="mb-2" block elevation=0>
              saved playlist
            </v-btn>
            <v-btn variant="plain" height=45 class="mb-2" block elevation=0>
              Create playlist
            </v-btn>
            <v-btn variant="plain" height=45 class="mb-2" block elevation=0>
              About us
            </v-btn>
            <v-btn variant="plain" height=45 class="mb-2" block elevation=0>
              Profile
            </v-btn>
          

        <template v-slot:append>
          <!-- action -->
          <div class="pa-2">
            <v-btn height=45 class="mb-2" block color="pink" elevation-0>
              Signup
            </v-btn>
            <v-btn height=45 variant="outlined" block color="pink" elevation-0>
              Logout
            </v-btn>

            <!-- url redirect buttons -->
            <v-btn-group dense>
              <v-btn>
                <v-icon>mdi-github</v-icon>
              </v-btn>

              <v-btn>
                <v-icon>mdi-twitter</v-icon>
              </v-btn>

              <v-btn>
                <v-icon>mdi-instagram</v-icon>
              </v-btn>

              <v-btn>
                <v-icon>mdi-facebook</v-icon>
              </v-btn>
            </v-btn-group>
          </div>
        </template>
      </v-navigation-drawer>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
    drawer: null,
  }),
}
</script>
