<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<style>
* {
  font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
}
button.confirma {
  width: 220px;
  height: 50px;
  font-size: 25px;
  border-radius: 6px;
  background-color: #2a88e2;
  color: #fff !important;
}

h2,
.margemTit {
  margin-bottom: 10px;
}
h1,
h2,
h3,
h4 {
  padding: 15px 15px 15px 15px;
  color: #007dc9;
  font-weight: normal;
}
h2#topoEsquerda {
  margin-top: -1px;
  padding: 15px 15px 15px 15px;
  border-bottom: 1px solid #ddd;
  background-color: #fff;
}
h2#topoDireita {
  align-content: flex-start;
  padding: 15px 15px 15px 25px;
  background-color: #fff;
  border-bottom: 1px solid #ddd;
}
h2 a {
  padding: 2px 5px 2px 5px;
  text-decoration: none;
  font-size: 12px;
  color: #007dc9;
}
</style>
