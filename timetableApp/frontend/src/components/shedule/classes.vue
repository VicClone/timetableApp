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
            <v-btn @click="isAddClass = true">Добавить класс</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="isAddClass"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить класс</h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
              v-model="formClass.name"
              label="Название"
              outlined>
            </v-text-field>
            <v-text-field
              v-model="formClass.count"
              label="Количество учеников"
              outlined>
            </v-text-field>
            <v-text-field
              v-model="formClass.workload"
              label="Нагрузка"
              outlined>
            </v-text-field>
            <v-text-field
              v-model="formClass.maxLessons"
              label="Максимум уроков"
              outlined>
            </v-text-field>
            <v-text-field
              v-model="formClass.maxRepeatLessons"
              label="Максимум повторяющихся уроков"
              outlined>
            </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddClass = false">
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
        text: 'Название класса',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Количество учеников', value: 'count' },
      { text: 'Нагрузка', value: 'workload' },
      { text: 'Максимум уроков', value: 'maxLessons' },
      { text: 'Максимум повторяющихся уроков', value: 'maxRepeatLessons' }
    ],
    classes: [],
    formClass: {
      name: '',
      count: '',
      workload: '',
      maxLessons: '',
      maxRepeatLessons: ''
    },
    isAddClass: false
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
          this.classes = response.data.map(classData => {
            return {
              name: classData.name,
              count: classData.people_count,
              workload: classData.workload,
              maxLessons: classData.max_lessons,
              maxRepeatLessons: classData.max_repeat_lessons
            }
          })
        })
        .catch(error => {
          console.log(error)
        })
    },
    createClass (id) {
      const postForm = {
        name: this.formClass.name,
        people_count: this.formClass.count,
        workload: this.formClass.workload,
        max_lessons: this.formClass.maxLessons,
        max_repeat_lessons: this.formClass.maxRepeatLessons
      }
      console.log(postForm)
      this.$http.post(`/api/groups?sheduleId=${id}`, postForm)
        .then(response => {
          console.log(response)
          this.getClasses(this.idShedule)
          this.isAddClass = false
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
