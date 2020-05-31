<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn fixed dark fab bottom right color="pink" v-on="on">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </template>

    <v-card class="mx-auto" outlined>
      <v-card-title>
        <span class="headline">Add Item</span>
      </v-card-title>
      <v-card-text>
        <v-form v-model="valid">
          <v-container fluid>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="name"
                  :rules="nameRules"
                  :counter="128"
                  label="Item Name"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  v-model="description"
                  :rules="descriptionRules"
                  label="Description"
                  rows="1"
                  prepend-icon="mdi-comment"
                  required
                ></v-textarea>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  v-model="price"
                  :rules="priceRules"
                  label="Price"
                  prepend-icon="$"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-file-input
                  v-model="imageFile"
                  prepend-icon="mdi-camera"
                  accept="image/*"
                  label="Image File"
                ></v-file-input>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn :disabled="!valid" color="success" class="mr-4" @click="addItem">
          Add
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "CreateItem",
  data: () => ({
    name: "",
    description: "",
    price: null,
    imageFile: null,
    imageUrl: "",
    id: null,
    valid: false,
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => v.length <= 128 || "Name must be less than 10 characters",
    ],
    priceRules: [
      (v) => !!v || "Price is required",
      (v) => !isNaN(v) || "Price should be a number.",
    ],
    descriptionRules: [(v) => !!v || "Description is required"],
    dialog: false,
  }),
  methods: {
    async handleForm() {
      let formData = new FormData();
      formData.set("name", this.name);
      formData.set("description", this.description);
      formData.set("price", this.price);
      formData.append("file", this.imageFile);
      const resp = await this.axios.post("/items/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      this.imageUrl = await resp.data.image;
      this.id = await resp.data.id;
    },

    async addItem() {
      if (this.valid) {
        try {
          await this.handleForm();
          this.$emit("on-new-item");
          this.imageUrl = "";
          this.id = null;
        } catch (error) {
          console.log(error);
          alert("Failed to add item!");
        }
      }
      this.dialog = false;
    },
  },
};
</script>

<style lang="scss" scoped></style>
