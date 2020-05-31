<template>
  <v-card>
    <v-list max-height="500" class="overflow-y-auto">
      <p v-if="!items.length">
        No items Found!
        <strong>Please add using the bottom right button</strong>
      </p>
      <v-list-item v-else v-for="item in items" :key="item.id">
        <router-link :to="'/' + item.id">
          <v-list-item-avatar>
            <v-img :src="item.image"></v-img>
          </v-list-item-avatar>
        </router-link>

        <v-list-item-content>
          <router-link :to="'/' + item.id">
            <v-list-item-title v-text="item.name"></v-list-item-title>
          </router-link>
          <v-list-item-subtitle>$ {{ item.price }}</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <v-btn class="mx-2" fab dark small color="red">
            <v-icon dark @click="deleteItem(item.id)">mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
export default {
  name: "ListItem",
  props: {
    items: Array,
  },
  methods: {
    async deleteItem(id) {
      try {
        await this.axios.delete("/items/", { params: { id: id } });
        this.$emit("on-delete");
      } catch (error) {
        console.log(error);
        alert("Failed to delete item");
      }
    },
  },
};
</script>
