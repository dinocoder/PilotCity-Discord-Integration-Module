<template>
  <v-container class="module-verify">
    <div class="module-verify__container">
        <div class="module-verify__description">
          <div class="font-weight-black text-body-1">
          Is this your Discord account?
        </div>
        <div :contenteditable=!readonly @input="updateDesc" class="font-weight-black text-body-1">
          <div style=display:inline-block>
            example#1234
            <img src="https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png" class="module-verify__profilepicture">
          </div>
        </div>
      </div>
      <div class="d-flex flex-column">
        <div class="module-verify__actions">
          <v-btn :ripple="false" height="40" outlined
          class="active module-verify__actions-save elevation-0">
            Link Account
          </v-btn>
          <v-btn :ripple="false" height="40" outlined
          class="active module-verify__actions-save elevation-0">
            No
          </v-btn>
        </div>
      </div>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import gql from 'graphql-tag';

export default Vue.extend({
  name: 'ModuleVerify',
  verifyText: 'Is this your Discord account?',
  exampleUser: 'example#1234', // Replace with usernam+id gathered from bot
  exampleProfilePictureLink: 'https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png', // Replace with profile picture gathered from
});
</script>
