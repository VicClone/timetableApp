<template>
  <v-container>
    <h1>Расписание классов</h1>
    <h2>Выберите класс</h2>
    <v-row>
      <v-col cols="6" xs12 md6>
        <v-autocomplete
          v-if="teachers &&teachers.length > 0"
          label="Учителя"
          v-model="value"
          :items="teachers"
          item-text="name"
          item-value="id"
          outlined
        ></v-autocomplete>
        <span v-else>Нет учителей</span>
      </v-col>
    </v-row>
    <v-row v-if="value">
      <v-col cols="12">
        <shedule-teacher
          :idTeacher="value"
          :idShedule="idShedule">
        </shedule-teacher>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: ['idShedule'],

  components: {
    sheduleTeacher: () => import('@/components/personalShedule/sheduleTeacher')
  },

  data: () => ({
    teachers: [],
    value: null

  }),

  created () {
    this.$nextTick(() => {
      this.teachers = this.getTeachers(this.idShedule)
    })
  },

  watch: {
    value (val) {
      console.log(val)
    }
  },

  methods: {
    getTeachers (id) {
      this.$http.get(`/api/teachers?sheduleId=${id}`)
        .then(response => {
          console.log(response, 'teacher')
          this.teachers = response.data.map(teacherData => {
            return {
              id: teacherData.tid,
              name: teacherData.name
            }
          })
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
