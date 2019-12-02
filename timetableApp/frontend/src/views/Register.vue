<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6">
        <h2>Регистрация</h2>
        <v-form>
          <v-col>
            <v-text-field
              label="Логин"
              outlined
              v-model="form.login">
            </v-text-field>
            <v-text-field
              label="Имя"
              outlined
              v-model="form.firstName">
            </v-text-field>
            <v-text-field
              label="Фамилия"
              outlined
              v-model="form.lastName">
            </v-text-field>
            <v-text-field
              label="E-mail"
              outlined
              v-model="form.email">
            </v-text-field>
            <v-text-field
              label="Пароль"
              outlined
              v-model="form.password">
            </v-text-field>
            <v-text-field
              label="Повторите пароль"
              outlined
              v-model="form.passwordConfirm">
            </v-text-field>
            <v-btn>Зарегистрироваться</v-btn>
          </v-col>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Form from 'vform'

export default {
  data: () => ({
    form: {
      login: '',
      lastName: '',
      firstName: '',
      email: '',
      password: '',
      passwordConfirm: ''
    }
  }),
  methods: {
    /* register () {
      const data = {
        name: this.name,
        email: this.email,
        password: this.password
      }
      this.$store.dispatch('register', data)
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))
    }, */

    async register () {
      await this.form.post('api/register')

      const form = new Form({
        'username': this.form.email,
        'password': this.form.password
      })
      try {
        const { data: { token } } = await form.post('/api/login')
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
