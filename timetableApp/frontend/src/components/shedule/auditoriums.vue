<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="auditoriums"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn @click="isAddAuditorium = true">Добавить аудиторию</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="isAddAuditorium"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить аудиторию</h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
              v-model="formClass.name"
              label="Название"
              outlined>
            </v-text-field>
            <v-text-field
              v-model="formClass.count"
              label="Вместимость"
              outlined>
            </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddAuditorium = false">
            Отмена
          </v-btn>
          <v-btn @click="createClass(idShedule)">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  props: ['idShedule'],
  data: () => ({
    headers: [
      {
        text: 'Название аудитории',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Вместимость', value: 'count' }
    ],
    auditoriums: [],
    formClass: {
      name: '',
      count: ''
    },
    isAddAuditorium: false
  }),
  created () {
    this.$nextTick(() => {
      this.getAuditoriums(this.idShedule)
    })
  },
  methods: {
    getAuditoriums (id) {
      this.$http.get(`/api/audituriums?sheduleId=${id}`)
        .then(response => {
          this.auditoriums = response.data.map(classData => {
            return {
              name: classData.name,
              count: classData.capacity
            }
          })
          console.log(this.auditoriums)
        })
        .catch(error => {
          console.log(error)
        })
    },
    createClass (id) {
      const postForm = {
        name: this.formClass.name,
        capacity: this.formClass.count
      }
      console.log(postForm)
      this.$http.post(`/api/audituriums?sheduleId=${id}`, postForm)
        .then(response => {
          console.log(response)
          this.getAuditoriums(this.idShedule)
          this.isAddAuditorium = false
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
