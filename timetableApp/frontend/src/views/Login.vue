<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="6">
        <v-card-title>Авторизация</v-card-title>
        <v-form>
          <v-layout row wrap center>
            <v-flex class="main" xs10>
              <v-text-field
                v-model="form.username"
                label="Login"
                outlined>
              </v-text-field>
            </v-flex>
            <v-flex xs10>
              <v-text-field
                v-model="form.password"
                label="Пароль"
                type="password"
                outlined>
              </v-text-field>
            </v-flex>
            <v-flex xs10>
              <v-btn @click="login">Вход</v-btn>
            </v-flex>
            <!-- <v-flex xs10>
              <v-btn @click="logout">Выйти</v-btn>
            </v-flex> -->
            {{ getAuth() }}
          </v-layout>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import Form from 'vform'

export default {
  middleware: 'guest',
  data: () => ({
    /* form: new Form({
      login: '',
      password: ''
    }) */
    form: {
      username: '',
      password: ''
    }
  }),
  methods: {
    /* async login () {
      await this.form.post('api/login/')

      const form = new Form({
        'username': this.form.email,
        'password': this.form.password
      })
      try {
        const { data: { token } } = await form.post('/api/login/')
        this.$store.dispatch('auth/saveToken', { token, remember: true })
        await this.$store.dispatch('auth/fetchUser')
        this.$router.push({ name: 'home' })
      } catch (e) {
        console.log('error: ', e)
      }
    }, */

    login () {
      this.$http.post('api/login/', this.form)
        .then(resp => {
          console.log(resp.data.token)
          const token = resp.data.token
          this.$store.dispatch('auth/saveToken', { token, remember: true })
          this.$store.dispatch('auth/fetchUser')
            .then(resp => {
              this.$router.push({ name: 'home' })
            })
            .catch(err => {
              console.log(err)
            })
        })
        .catch(err => {
          console.log(err)
        })
    },
    getAuth () {
      this.$store.dispatch('auth/fetchUser')
      console.log(this.$cookie)
      return this.$cookie
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
