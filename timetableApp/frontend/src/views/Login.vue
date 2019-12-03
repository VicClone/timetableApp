<template>
  <v-container>
    <v-col cols="12" sm="6">
      <v-card-title>Авторизация</v-card-title>
      <v-form @submit.prevent="login">
        <v-layout row wrap center>
          <v-flex class="main" xs10>
            <v-text-field
              v-model="form.login"
              label="Login"
              outlined>
            </v-text-field>
          </v-flex>
          <v-flex xs10>
            <v-text-field
              v-model="form.password"
              label="Пароль"
              outlined>
            </v-text-field>
          </v-flex>
          <v-flex xs10>
            <v-btn @click="login">Вход</v-btn>
          </v-flex>
        </v-layout>
      </v-form>
    </v-col>
  </v-container>
</template>

<script>
import Form from 'vform'

export default {
  data: () => ({
    form: new Form({
      login: '',
      password: ''
    })
  }),
  methods: {
    async login () {
      await this.form.get('api/login/')

      const form = new Form({
        'username': this.form.email,
        'password': this.form.password
      })
      try {
        const { data: { token } } = await form.get('/api/login/')
        this.$store.dispatch('auth/saveToken', { token, remember: true })
        await this.$store.dispatch('auth/fetchUser')
        this.$router.push({ name: 'home' })
      } catch (e) {
        console.log('error: ', e)
      }
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
