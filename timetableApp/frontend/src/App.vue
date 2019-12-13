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
      return this.$store.getters['auth/check']
    }
  },
  mounted () {
    this.$store.dispatch('auth/fetchUser')

    // this.$nextTick(() => {
    //   this.checkAuth()
    // })
  },

  methods: {
    logout () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    checkAuth () {
      if (!this.$store.getters['auth/check']) {
        this.$router.push({ name: 'home' })
      }
    }
  }
}
</script>
