<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6">
        <h2>Регистрация</h2>
        <v-form>
          <v-col>
            <v-text-field
              label="Логин"
              name="login"
              outlined
              v-model="form.login">
            </v-text-field>
            <v-text-field
              label="Имя"
              name="name"
              outlined
              v-model="form.first_name">
            </v-text-field>
            <v-text-field
              label="Фамилия"
              name="lastname"
              outlined
              v-model="form.last_name">
            </v-text-field>
            <v-text-field
              label="E-mail"
              name="email"
              outlined
              v-model="form.email">
            </v-text-field>
            <v-text-field
              label="Пароль"
              name="password"
              outlined
              v-model="form.password">
            </v-text-field>
            <v-text-field
              label="Повторите пароль"
              name="passwordConfirm"
              outlined
              v-model="form.password_confirmation">
            </v-text-field>
            <v-btn @click="register">Зарегистрироваться</v-btn>
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
    form: new Form({
      login: '',
      last_name: '',
      first_name: '',
      email: '',
      password: '',
      password_confirmation: ''
    })
  }),
  methods: {
    async register () {
      await this.form.post('api/register/')

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
    }
  }
}
</script>
