<template>
  <v-app>
    <v-app-bar color="deep-purple accent-4" app dark elevation="12">
      <v-btn to="/" icon>
        <v-icon>mdi-tea</v-icon>
      </v-btn>
      <v-toolbar-title>
        <router-link to="/" class="toolbar-title"
          >Sadguru's Amrit-Tulya - Tea Shop</router-link
        >
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>

<style scoped>
.toolbar-title {
  color: inherit;
  text-decoration: inherit;
}
</style>
