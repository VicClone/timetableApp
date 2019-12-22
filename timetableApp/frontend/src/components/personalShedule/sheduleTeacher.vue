<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="businness"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>

        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn @click="isAddTeacherSchedule = true">Изменить занятость</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="isAddTeacherSchedule"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить занятость</h3>
        </v-card-title>
        <v-card-text>
          <v-autocomplete
            v-if="subjects && subjects.length > 0"
            label="Время"
            v-model="subValue"
            :items="subjects"
            item-text="name"
            item-value="id"
            outlined
          ></v-autocomplete>
        </v-card-text>
        <v-card-text>
          <v-autocomplete
            label="Занятость"
            v-model="busyValue"
            :items="busy"
            item-text="name"
            item-value="val"
            outlined
          ></v-autocomplete>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddWorkload = false">
            Отмена
          </v-btn>
          <v-btn @click="addSheduleTeacher(idClass, subValue)">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  props: ['idTeacher', 'idShedule'],

  data: () => ({
    headers: [
      {
        text: 'Звонки',
        align: 'left',
        sortable: false,
        value: 'time'
      }
    ],
    businness: [],
    isAddTeacherSchedule: false,
    formBusinness: {
      check: false
    },
    busy: [
      {
        name: 'Занят',
        val: true
      },
      {
        name: 'Свободен',
        val: false
      }
    ],
    busyValue: null,
    subjects: [],
    subValue: null,

    daysWeek: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт'],
    daysWeekEn: ['mon', 'tue', 'wen', 'thu', 'fri']
  }),

  created () {
    this.$nextTick(() => {
      this.getSheduleTeacher(this.idTeacher)
    })
  },

  methods: {
    getSheduleTeacher (teacherId) {
      this.$http.get(`/api/teacherShedule?teacherId=${teacherId}`)
        .then(response => {
          console.log(response)
          this.headers = this.headers.concat(this.getDaysWeek(response.data))
          this.businness = this.formatShedule(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },

    addSheduleTeacher (teacherId, timeId) {
      this.$http.post(`/api/teacherShedule?teacherId=${teacherId}&timeid=${timeId}`,
        { business: this.busyValue })
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    },

    formatShedule (shedule) {
      const uniqueTimes = new Set()
      const times = []

      shedule.forEach(val => {
        uniqueTimes.add(val.time.start)
      })

      uniqueTimes.forEach(uniqTime => {
        const timeShedule = shedule
          .filter(item => {
            return item.time.start === uniqTime
          })
          .sort((a, b) => {
            return a.time.day_week - b.time.day_week
          })

        const itemTime = {}
        itemTime['time'] = timeShedule[0].time.start

        timeShedule.forEach(val => {
          const indexDay = this.daysWeekEn[val.time.day_week - 1]
          itemTime[indexDay] = val.business
        })

        times.push(itemTime)
      })

      this.setTextBusy(times)

      return times
    },

    getDaysWeek (shedule) {
      const daysWeek = new Set()

      shedule.forEach(item => {
        daysWeek.add(item.time.day_week)
      })

      const formatDays = [...daysWeek].map(dayIndex => {
        return {
          text: this.daysWeek[dayIndex - 1],
          align: 'left',
          sortable: false,
          value: this.daysWeekEn[dayIndex - 1]
        }
      })

      return formatDays
    },

    setTextBusy (shedule) {
      shedule.forEach(item => {
        const keys = Object.keys(item)

        keys.forEach(key => {
          if (item[key] === false) {
            item[key] = 'Свободен'
          }
          if (item[key] === true) {
            item[key] = 'Занят'
          }
        })
      })
    }
  }
}
</script>
