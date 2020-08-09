/* eslint-disable @typescript-eslint/camelcase */
// !TODO: fix type errors :]
import Vue from 'vue';
import VueApollo from 'vue-apollo';
import {
  createApolloClient, restartWebsockets,
} from 'vue-cli-plugin-apollo/graphql-client';
//  Allows for using secure endpoint with apollo
import { setContext } from 'apollo-link-context';
import { HttpLink, InMemoryCache } from 'apollo-boost';
// Realm Setup
// eslint-disable-next-line import/no-unresolved
import * as RealmWeb from 'realm-web';

// Install the vue plugin
Vue.use(VueApollo);

// Name of the localStorage item
const AUTH_TOKEN = 'apollo-token';

//  Mongo App Setup
//  ! Replace with you App ID from Mongo Realm
export const APP_ID = 'microapp-lokxi';

const app = new RealmWeb.App({
  id: APP_ID,
  baseUrl: 'https://realm.mongodb.com',
});
const graphql_url = `https://realm.mongodb.com/api/client/v2.0/app/${APP_ID}/graphql`;
// Http endpoint
// ! Hide endpoint for production repos. Use .env variables
const httpEndpoint = process.env.VUE_APP_GRAPHQL_HTTP || graphql_url;
const authorizationHeaderLink = setContext(async (_, { headers }) => {
  if (app.currentUser) {
    // Refreshing custom data also refreshes the access token
    await app.currentUser.refreshCustomData();
  } else {
    // If no user is logged in, log in an anonymous user
    await app.logIn(RealmWeb.Credentials.anonymous());
  }
  // Get a valid access token for the current user
  const { accessToken } = app.currentUser;
  if (accessToken) { console.log('I HAVE ACCESS'); }
  console.log('currentUser', accessToken, app.currentUser);

  // Set the Authorization header, preserving any other headers
  return {
    headers: {
      ...headers,
      Authorization: `Bearer ${accessToken}`,
    },
  };
});
// Construct a new Apollo HttpLink that connects to your app's GraphQL endpoint

const httpLink = new HttpLink({ uri: graphql_url });
// Files URL root
export const filesRoot = process.env.VUE_APP_FILES_ROOT || httpEndpoint.substr(0, httpEndpoint.indexOf('/graphql'));

Vue.prototype.$filesRoot = filesRoot;

// Config
const defaultOptions = {
  // You can use `https` for secure connection (recommended in production)
  httpEndpoint,
  // You can use `wss` for secure connection (recommended in production)
  // Use `null` to disable subscriptions
  wsEndpoint: null,
  // LocalStorage token
  tokenName: AUTH_TOKEN,
  // Enable Automatic Query persisting with Apollo Engine
  persisting: false,
  // Use websockets for everything (no HTTP)
  // You need to pass a `wsEndpoint` for this to work
  websocketsOnly: false,
  // Is being rendered on the server?
  ssr: false,

  // Override default apollo link
  // note: don't override httpLink here, specify httpLink options in the
  // httpLinkOptions property of defaultOptions.
  link: authorizationHeaderLink.concat(httpLink),

  // Override default cache
  cache: new InMemoryCache(),

  // Override the way the Authorization header is set
  // getAuth: (tokenName) => ...

  // Additional ApolloClient options
  // apollo: { ... }

  // Client local data (see apollo-link-state)
  // clientState: { resolvers: { ... }, defaults: { ... } }
};

// Call this in the Vue app file
export function createProvider(options = {}) {
  // Create apollo client
  const { apolloClient, wsClient } = createApolloClient({
    ...defaultOptions,
    ...options,
  });
  apolloClient.wsClient = wsClient;

  // Create vue apollo provider
  const apolloProvider = new VueApollo({
    defaultClient: apolloClient,
    defaultOptions: {
      $query: {
        fetchPolicy: 'cache-and-network',
      },
    },
    errorHandler(error) {
      // eslint-disable-next-line no-console
      console.log('%cError', 'background: red; color: white; padding: 2px 4px; border-radius: 3px; font-weight: bold;', error.message);
    },
  });

  return apolloProvider;
}

// Manually call this when user log in
export async function onLogin(apolloClient, token) {
  if (typeof localStorage !== 'undefined' && token) {
    localStorage.setItem(AUTH_TOKEN, token);
  }
  if (apolloClient.wsClient) restartWebsockets(apolloClient.wsClient);
  try {
    await apolloClient.resetStore();
  } catch (e) {
    // eslint-disable-next-line no-console
    console.log('%cError on cache reset (login)', 'color: orange;', e.message);
  }
}

// Manually call this when user log out
export async function onLogout(apolloClient) {
  if (typeof localStorage !== 'undefined') {
    localStorage.removeItem(AUTH_TOKEN);
  }
  if (apolloClient.wsClient) restartWebsockets(apolloClient.wsClient);
  try {
    await apolloClient.resetStore();
  } catch (e) {
    // eslint-disable-next-line no-console
    console.log('%cError on cache reset (logout)', 'color: orange;', e.message);
  }
}
