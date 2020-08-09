import Vue, { VueConstructor } from 'vue'
import VueApollo from "../node_modules/vue-apollo/types";

declare module 'vue/types/vue' {
  interface VueConstructor {
    $apolloProvider: VueApollo;
  }
}
// declare module 'vue-apollo'{
//   function createProvider(): VueApollo;
// }