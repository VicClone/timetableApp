<template>
  <v-container>
    <v-col cols="12" sm="6">
      <v-card-title>Авторизация</v-card-title>
      <v-form @submit.prevent="login">
        <v-layout row wrap center>
          <v-flex class="main" xs10>
            <v-text-field
              v-model="email"
              label="E-mail"
              outlined>
            </v-text-field>
          </v-flex>
          <v-flex xs10>
            <v-text-field
              v-model="password"
              label="Пароль"
              outlined>
            </v-text-field>
          </v-flex>
          <v-flex xs10>
            <v-btn>Вход</v-btn>
          </v-flex>
        </v-layout>
      </v-form>
    </v-col>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    email: '',
    password: ''
  }),
  methods: {
    login () {
      const email = this.email
      const password = this.password
      this.$store.dispatch('login', { email, password })
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))
    }
  }
}
</script>

<style lang="scss">
.main {
  &-1 {
    color: red;
  }
}
</style>
