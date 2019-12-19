<template>
  <v-container>
    <h1>Расписание классов</h1>
    <h2>Выберите класс</h2>
    <v-row>
      <v-col cols="6" xs12 md6>
        <v-autocomplete
          v-if="classes && classes.length > 0"
          label="Классы"
          v-model="value"
          :items="classes"
          item-text="name"
          item-value="id"
          outlined
        ></v-autocomplete>
        <span v-else>Нет классов</span>
      </v-col>
    </v-row>
    <!-- <v-row v-if="value">
      <v-col cols="12">
        <workload
          :idClass="value"
          :idShedule="idShedule">
        </workload>
      </v-col>
    </v-row> -->
  </v-container>
</template>

<script>
export default {
  props: ['idShedule'],
  data: () => ({
    teachers: [],
    value: null

  }),

  created () {
    this.$nextTick(() => {
      this.teachers = this.getTeachers(this.idShedule)
    })
  },

  methods: {
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
  }
}
</script>
