<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="teachers"
          :items-per-page="5"
          class="elevation-1"
        >
        </v-data-table>
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
          <h3>Добавить учителя</h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formTeacher.name"
            label="Имя"
            outlined>
          </v-text-field>
        </v-card-text>
        <v-card-text>
          <v-autocomplete
            v-if="subjects && subjects.length > 0"
            label="Предметы"
            v-model="subValue"
            :items="subjects"
            item-text="name"
            item-value="id"
            outlined
          ></v-autocomplete>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddTeachers = false">
            Отмена
          </v-btn>
          <v-btn @click="addTeacher(idShedule, subValue)">
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
        value: 'name'
      },
      { text: 'Предмет', value: 'subject' }
    ],
    teachers: [],
    subjects: [],
    subValue: null,
    formTeacher: {
      name: ''
    },
    isAddTeachers: false
  }),

  created () {
    this.$nextTick(() => {
      this.getSubjects(this.idShedule)
    })
    this.$nextTick(() => {
      this.getTeacher(this.idShedule)
    })
  },

  methods: {
    getSubjects (id) {
      this.$http.get(`/api/subjects?sheduleId=${id}`)
        .then(response => {
          this.subjects = response.data.map(subjectsData => {
            return {
              id: subjectsData.did,
              name: subjectsData.name
            }
          })
        })
        .catch(error => {
          console.log(error)
        })
    },
    getTeacher (id) {
      this.$http.get(`/api/teachers?sheduleId=${id}`)
        .then(response => {
          console.log(response, 'teacher')
          this.teachers = response.data.map(teacherData => {
            return {
              name: teacherData.name,
              subject: this.getNameSub(teacherData.discipline)
            }
          })
        })
        .catch(error => {
          console.log(error)
        })
    },
    addTeacher (sheduleId, disciplineId) {
      this.$http.post(
        `/api/teachers?sheduleId=${sheduleId}&disciplineId=${disciplineId}`,
        { name: this.formTeacher.name }
      )
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
        .finally(() => {
          this.isAddTeachers = false
        })
    },
    getNameSub (id) {
      const sub = this.subjects.find((el) => {
        return el.id === id
      })

      return sub.name
    }
  }
}
</script>
