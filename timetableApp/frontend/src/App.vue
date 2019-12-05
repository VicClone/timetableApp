<template>
  <v-app>
    <v-content>
      <v-btn v-if="isAuth" @click="logout">Выйти</v-btn>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',

  components: {

  },

  data: () => ({
    //
  }),

  computed: {
    isAuth () {
      return this.$store.getters.isAuth
    }
  },
  mounted () {
    this.$store.dispatch('auth/fetchUser')
  },

  methods: {
    logout () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    }
  }
}
</script>
