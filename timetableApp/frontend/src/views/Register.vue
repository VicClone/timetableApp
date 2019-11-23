<template>
  <v-container>
    <v-card>
      <v-card-title>Register</v-card-title>
      <v-form>
        <v-layout>
          <v-flex>
          </v-flex>
          <v-flex>
            <!-- <v-textfield></v-textfield> -->
          </v-flex>
        </v-layout>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    form: {
      login: '',
      last_name: '',
      first_name: '',
      email: '',
      password: '',
      password_confirmation: ''
    }
  }),
  components: {
  }
}
</script>
