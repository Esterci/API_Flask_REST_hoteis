<template>
  <div id="main">
    <v-row no-gutters class="justify-center">
      <v-col cols="2" class="mb-2">
        <v-img
          @click="$router.push({ name: 'home' })"
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
      <v-card
        :loading="loading"
        class="pa-4 rounded-xl"
        elevation="14"
        max-width="700"
      >
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>

        <v-card-title>Formulário de criação de hoteis</v-card-title>

        <v-card-text class="mt-4">
          <v-form>
            <v-row>
              <v-text-field
                v-model="hotel.nome"
                type="text"
                label="Nome"
                :rules="[rules.required]"
                outlined
                required
                counter="80"
              >
              </v-text-field>
            </v-row>

            <v-row>
              <v-text-field
                v-model="estrelas"
                type="number"
                label="N° de estrelas"
                :rules="[rules.required]"
                outlined
                required
              >
              </v-text-field>
            </v-row>

            <v-row>
              <v-text-field
                v-model="diaria"
                type="number"
                label="Valor da diária"
                :rules="[rules.required]"
                outlined
                required
              >
              </v-text-field>
            </v-row>

            <v-row>
              <v-text-field
                v-model="hotel.cidade"
                type="text"
                label="Cidade"
                :rules="[rules.required]"
                outlined
                required
                counter="40"
              >
              </v-text-field>
            </v-row>
          </v-form>
        </v-card-text>

        <v-divider class="mx-4"></v-divider>

        <v-card-actions class="d-flex justify-space-between">
          <v-btn dark color="blue darken-4" @click="cadastrarHotel">
            Submeter
          </v-btn>
          <v-icon color="green" large v-if="submit">mdi-check-underline-circle</v-icon>
        </v-card-actions>
      </v-card>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rules: {
        required: (value) => !!value || "Campo obrigatório.",
      },
      loading: false,
      estrelas: undefined,
      diaria: undefined,
      hotel: {},
      submit: false,
    };
  },
  watch: {
    estrelas() {
      if (this.estrelas > 5) {
        this.estrelas = 5;
      } else {
        if (this.estrelas < 0) {
          this.estrelas = 0;
        }
      }
    },
    diaria() {
      if (this.diaria < 0) {
        this.diaria = 0;
      }
    },
  },
  methods: {
    async cadastrarHotel() {
      this.hotel.estrelas = this.estrelas;
      this.hotel.diaria = this.diaria;
      await this.$http
        .post(`registrar-hoteis/`, this.hotel)
        .then(() => (this.submit = true));
    },
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