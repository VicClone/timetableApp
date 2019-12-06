<template>
  <v-container fluid>
    <h1>Мои расписания</h1>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="shedules"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn>Добавить расписания</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    headers: [
      {
        text: 'Название',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Дата создания', value: 'dateCreate' },
      { text: 'Дата публикации', value: 'datePublic' },
      { text: 'Классы', value: 'classes' }
    ],
    shedules: [
      {
        name: 'Расписание I четверть\n2019-2020гг. начальная школа',
        dateCreate: '06.12.19',
        datePublic: '06.12.19',
        classes: '1-11 классы'
      },
      {
        name: 'Расписание I четверть\n2019-2020гг. средняя школа',
        dateCreate: '06.12.19',
        datePublic: '06.12.19',
        classes: '1-11 классы'
      }
    ]
  }),
  methods: {
    /*
    getShedule() {
      this.$$http.get('api/login/')
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
    } */
  }
}
</script>
