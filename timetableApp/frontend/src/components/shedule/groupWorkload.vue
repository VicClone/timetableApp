<template>
  <v-container>
    <h1>Нагрузка по классам</h1>
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
    <v-row v-if="value">
      <v-col cols="12">
        <workload
          :idClass="value"
          :idShedule="idShedule">
        </workload>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: ['idShedule'],

  components: {
    workload: () => import('@/components/workload/workload')
  },

  data: () => ({
    classes: [],
    value: null

  }),

  created () {
    this.$nextTick(() => {
      this.classes = this.getClasses(this.idShedule)
    })
  },

  computed: {
    classNames () {
      return this.classes.map(classItem => {
        return classItem.name
      })
    },
    classValues () {
      return this.classes.map(classItem => {
        return classItem.name
      })
    }
  },

  watch: {
    values (val) {
      console.log(val)
    }
  },
  methods: {
    getClasses (id) {
      this.$http.get(`/api/groups?sheduleId=${id}`)
        .then(response => {
          this.classes = response.data.map(classData => {
            return {
              id: classData.gid,
              name: classData.name,
              count: classData.people_count,
              maxLessons: classData.max_lessons,
              maxRepeatLessons: classData.max_repeat_lessons
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
