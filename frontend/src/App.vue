<template>
  <v-app>
    <v-main>
      <Module/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
// import ApolloExample from './components/ApolloExample.vue';
import Module from './Module/Module.vue';

export default Vue.extend({
  name: 'App',

  components: {
    Module,
  },

  data: () => ({
    //
  }),
});
</script>
<style lang="scss">
  html, body{
    font-family: "Raleway";
    font-size: 16px;
    width: 100%;
    height: 100%;
  }
</style>
