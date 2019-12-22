export default {
  computed: {
    currentUser: {
      get () {
        return this.$store.state.currentUser
      },
      set (v) {

      }
    },
    loadUser () {
      return this.$store.state.loadUser
    },
    appSettings () {
      return this.$store.state.appSettings
    },
    loadSettings () {
      return this.$store.state.loadSettings
    }
  }
}
