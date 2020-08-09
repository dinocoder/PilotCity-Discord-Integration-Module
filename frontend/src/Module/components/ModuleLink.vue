<template>
<!--  TODO: make the inputs into actual components -->
  <v-container class="module-link">
    <div class="module-link__container">
      <div class="module-link__description">
        <div :contenteditable=!readonly @input="updateDesc" class="font-weight-black text-body-1">
          {{moduleDescription}}
        </div>
      </div>
      <div class="module-link__instructions">
      </div>
      <div class="d-flex flex-column">
        <div v-if="!readonly" class="module-link__actions">
          <v-btn :ripple="false" height="40" outlined
          class="active module-link__actions-joinserver elevation-0">
            Join Server
          </v-btn>
        </div>
      </div>
      <div class="module-link__actions-hasaccount">
        <div class="font-weight-black text-body-1">
          <p>{{joinedText}}</p>
        </div>
      </div>
      <div class="module-link__linkexisting">
        <div :contenteditable=!readonly @input="updateDesc" class="font-weight-grey text-body-1">
      </div>
      <div class="d-flex flex-column">
        <div v-if="!readonly" class="module-link__actions">
          <v-btn :ripple="false" height="40" outlined
          class="active module-link__actions-joinserver elevation-0">
            Link Account
          </v-btn>
        </div>
      </div>
      </div>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import gql from 'graphql-tag';

export default Vue.extend({
  name: 'ModuleLink',
  props: {
    readonly: {
      type: Boolean,
      default: false,
    },
  },
  apollo: {
    instructions: gql`query instructQuery{
      mApracticelogOpt{
        instructions
      }
    }`,
  },
  data: () => ({
    moduleDescription: 'Discord is a text and voice chat program that PilotCity uses to coordinate teams and grow our community. Please create an account at https://discord.com/register and join our Discord server by clicking the link below!',
    joinedText: 'Already joined the server? Enter your username and ID below (ex. user#1234) to link. (do not use if you haven\'t joined)',
  }),
  methods: {
    updateDesc(e: Event) {
      const el = e.target as HTMLTextAreaElement;
      this.moduleDescription = el.innerText;
      console.log('description has been updated!');
    },
    updateItem(e: Event, i: number) {
      const el = e.target as HTMLTextAreaElement;
      this.instructions[i] = el.innerText;
      console.log(`instruction ${i} has been updated!`);
    },
    addItem() {
      this.instructions.push('');
    },
  },
});
</script>
