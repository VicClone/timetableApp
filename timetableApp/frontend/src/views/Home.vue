<template>
  <div class="home">
    <h1>Home page</h1>
    <v-btn color="red">
      <router-link :to="{name: 'login'}">Login</router-link>
    </v-btn>
    <v-btn color="blue">
      <router-link :to="{name: 'register'}">Register</router-link>
    </v-btn>
    {{ getAuth() }}
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
  },
  methods: {
    getAuth () {
      // console.log(this.$store)
      return this.$store.getters['auth/check']
    }
  }
}
</script>
