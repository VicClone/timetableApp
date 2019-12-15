<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="teachers"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn @click="isAddTeachers = true">Добавить учителя</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="isAddTeachers"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить предмет</h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
              v-model="formTeacher.name"
              label="Название"
              outlined>
            </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddTeachers = false">
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
        text: 'Имя преподавателя',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Предмет', value: 'discipline' },
      { text: 'Кабинет', value: 'auditorium' }
    ],
    teachers: [],
    formTeacher: {
      name: '',
      discipline: '',
      auditurium: ''
    },
    isAddTeachers: false
  }),
  created () {
    this.$nextTick(() => {
      this.getSubjects(this.idShedule)
    })
  },
  methods: {
    getSubjects (id) {
      this.$http.get(`/api/teachers?sheduleId=${id}`)
        .then(response => {
          console.log(response)
          this.subjects = response.data.map(subjectsData => {
            return {
              name: subjectsData.name
            }
          })
        })
        .catch(error => {
          console.log(error)
        })
    },
    createClass (id) {
      this.$http.post(`/api/subjects?sheduleId=${id}`, this.formTeacher)
        .then(response => {
          console.log(response)
          this.getSubjects(this.idShedule)
          this.isAddTeachers = false
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
