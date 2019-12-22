<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="subjects"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn @click="isAddSubject = true">Добавить предмет</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="isAddSubject"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить предмет</h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
              v-model="formSubject.name"
              label="Название"
              outlined>
            </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddSubject = false">
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
        text: 'Название предмета',
        align: 'left',
        sortable: false,
        value: 'name'
      }
    ],
    subjects: [],
    formSubject: {
      name: ''
    },
    isAddSubject: false
  }),
  created () {
    this.$nextTick(() => {
      this.getSubjects(this.idShedule)
    })
  },
  methods: {
    getSubjects (id) {
      this.$http.get(`/api/subjects?sheduleId=${id}`)
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
      this.$http.post(`/api/subjects?sheduleId=${id}`, this.formSubject)
        .then(response => {
          console.log(response)
          this.getSubjects(this.idShedule)
          this.isAddSubject = false
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
