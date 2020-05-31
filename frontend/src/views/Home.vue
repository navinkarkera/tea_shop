<template>
  <v-container fluid>
    <v-row align="center">
      <create-item @on-new-item="loadItems"></create-item>
    </v-row>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <list-item :items="items" @on-delete="loadItems"></list-item>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import CreateItem from "@/components/CreateItem.vue";
import ListItem from "@/components/ListItem.vue";

export default {
  name: "Home",
  data: () => ({
    items: [],
  }),
  components: {
    CreateItem,
    ListItem,
  },
  mounted() {
    this.loadItems();
  },
  methods: {
    async loadItems() {
      try {
        const response = await this.axios.get("/items/");
        const { data } = await response;
        this.items = data;
      } catch (error) {
        console.log(error);
        alert("Failed to fetch all items");
      }
    },
  },
};
</script>
