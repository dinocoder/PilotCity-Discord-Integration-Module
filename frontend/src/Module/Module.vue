<template>
<!--  TODO: make the inputs into actual components -->
  <v-container class="module">
    <div class="module__container">
      <div class="module__title">
        <div class="module__image rounded-circle">
          <v-img
          height="87px"
          max-width="93px"
          src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2c9addc0-037f-4fd8-a226-e21468527db6%2FUntitled.png?table=block&id=c58eba0c-df1a-46c2-8bee-5578fde10ebe&width=2610&cache=v2">
          </v-img>
        </div>
        <div class="module__header text-md-h5 text-sm-subtitle-1 d-flex align-end">
          <input type="text" class="module__header-text" :value="moduleName">
        </div>
      </div>
      <div class="module__body">
        <div class="module__pagination">
          <div
          :class="{'active': currentPage==page}"
          v-for="page in pages" :key="page">
            <div class="module__pagination-button--active"/>
            <v-btn
            :ripple="false"
            class="module__pagination-button elevation-0"
            color="transparent" height="40" small
            @click="currentPage=page">
              {{ page }}
            </v-btn>
          </div>
        </div>
        <div class="module__page">
          <keep-alive>
            <component :is="getComponent"/>
          </keep-alive>
        </div>
      </div>
    </div>
  </v-container>
</template>
<script lang="ts">
import Vue from 'vue';
import '@/styles/module.scss';
import * as Module from './components';

export default Vue.extend({
  name: 'Microapp',
  components: {
    'module-link': Module.Link,
    'module-verify': Module.Verify,

  },
  data: () => ({
    moduleName: 'Discord Integration',
    pages: ['Link', 'Verify'],
    currentPage: 'Link',
  }),
  computed: {
    getComponent() {
      return `module-${this.currentPage.toLowerCase()}`;
    },
  },
});
</script>
