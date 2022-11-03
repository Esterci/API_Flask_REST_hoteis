<template>
  <div id="main">
    <v-row no-gutters class="justify-center">
      <v-col cols="2" class="mb-2">
        <v-img
          @click="$router.push({ name: 'formulario' })"
          :aspect-ratio="1 / 1"
          contain
          id="logo"
          src="@/assets/logo-completa.png"
          width="250"
          alt=""
        />
      </v-col>
    </v-row>
    <v-row no-gutters class="justify-center mb-12">
      <v-card class="pa-4 rounded-xl" elevation="14" max-width="700">
        <v-card-title>Hoteis</v-card-title>
        <v-card-text class="mt-4">
          <v-data-table
            :headers="headers"
            :items="hoteis"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </v-card-text>
        <v-divider class="mx-4"></v-divider>

        <v-card-actions class="d-flex justify-space-between">
          <v-btn
            dark
            color="blue darken-4"
            @click="$router.push({ name: 'formulario' })"
          >
            Cadastrar Hotel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hoteis: undefined,
      headers: [
        { text: "Nome", align: "start", sortable: false, value: "nome" },
        { text: "Estrelas", value: "estrelas" },
        { text: "Diaria", value: "diaria" },
        { text: "Cidade", sortable: false, value: "cidade" },
      ],
    };
  },
  async beforeCreate() {
    await this.$http.get(`hoteis`).then((res) => {
      this.hoteis = res.data.hoteis;
      console.log(res.data.hoteis);
    });
  },
};
</script>

<style>
#main {
  height: 100%;
  width: 100%;
  background: rgb(63, 94, 251);
  background: radial-gradient(
    circle,
    rgba(63, 94, 251, 1) 0%,
    rgba(23, 46, 122, 1) 100%
  );
}
.v-row {
  width: 100%;
}

.v-form {
  width: 600px;
}
</style>