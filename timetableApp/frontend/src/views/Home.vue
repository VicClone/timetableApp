<template>
  <div class="home">
    <h1>Генератор расписание</h1>
    <v-row>
      <v-col cols="12">
        <v-btn color="red">
          <router-link :to="{name: 'login'}">Login</router-link>
        </v-btn>
        <v-btn color="blue" v-if="!getAuth()">
          <router-link :to="{name: 'register'}">Register</router-link>
        </v-btn>
        <v-btn color="green" v-if="getAuth()">
          <router-link :to="{name: 'profile'}">Profile</router-link>
        </v-btn>
      </v-col>
    </v-row>
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
