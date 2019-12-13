<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="classes"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn>Добавить класс</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  props: ['idShedule'],
  data: () => ({
    headers: [
      {
        text: 'Название класса',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Количество учеников', value: 'count' }
    ],
    classes: [
      {
        name: '1a',
        count: '20'
      },
      {
        name: '1б',
        count: '20'
      },
      {
        name: '1в',
        count: '20'
      },
      {
        name: '2a',
        count: '20'
      }

    ]
  }),
  created () {
    this.$nextTick(() => {
      this.getClasses(this.idShedule)
    })
  },
  methods: {
    getClasses (id) {
      this.$http.get(`/api/groups?sheduleId=${id}`)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
