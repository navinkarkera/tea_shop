<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-card class="mx-auto my-12" width="500">
        <v-img :src="image"> </v-img>

        <v-card-title>{{ name }}</v-card-title>
        <v-card-subtitle>$ {{ price }}</v-card-subtitle>

        <v-card-text class="text--primary">
          {{ description }}
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "DetailView",
  data: () => ({
    name: "",
    description: "",
    price: null,
    image: "",
  }),
  beforeMount() {
    this.loadItem();
  },
  methods: {
    async loadItem() {
      try {
        console.log(this.$route.params.id);
        const response = await this.axios.get(
          "/items/" + this.$route.params.id
        );
        const data = await response.data;
        this.name = data.name;
        this.description = data.description;
        this.price = data.price;
        this.image = data.image;
      } catch (error) {
        console.log(error);
        alert("Failed to fetch item");
        this.$router.push({ name: "Home" });
      }
    },
  },
};
</script>
