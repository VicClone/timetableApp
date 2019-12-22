<template>
  <v-container>
    <h1>Готовые расписания</h1>
    <!-- <pre>{{  shedules}}</pre> -->
    <div v-if="groups">
    <div v-for="group in groups" :key="group">
      <h2>Расписание для {{ group }}</h2>
      <v-data-table
          :headers="headers"
          :items="shedules[group]"
          :items-per-page="8"
          class="elevation-1"
        ></v-data-table>
    </div>
    </div>
    <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn @click="generateShedule(idShedule)">Сгенерировать расписание</v-btn>
          </div>
        </v-row>
  </v-container>
</template>

<script>
export default {
  props: ['idShedule'],
  data: () => ({
    headers: [
      {
        text: 'Время',
        align: 'left',
        sortable: false,
        value: 'time'
      },
      {
        text: 'Пн',
        align: 'left',
        sortable: false,
        value: 'mon'
      },
      {
        text: 'Вт',
        align: 'left',
        sortable: false,
        value: 'tue'
      },
      {
        text: 'Ср',
        align: 'left',
        sortable: false,
        value: 'wen'
      },
      {
        text: 'Чт',
        align: 'left',
        sortable: false,
        value: 'thu'
      },
      {
        text: 'Пт',
        align: 'left',
        sortable: false,
        value: 'fri'
      }
    ],
    shedules: {},
    groups: null,
    time: [ '8:00', '9:00', '10:00', '11:00', '12:00' ],
    daysWeek: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт'],
    daysWeekEn: ['mon', 'tue', 'wen', 'thu', 'fri']

  }),
  created () {
    this.$nextTick(() => {
      this.getShedules(this.idShedule)
    })
  },
  methods: {
    getShedules (id) {
      this.$http.get(`/api/generate?sheduleId=${id}`)
        .then(response => {
          console.log(response)
          this.shedules = this.formatShedule(response.data.data)
          this.getSubjects(this.shedules)
        })
        .catch(error => {
          console.log(error)
        })
    },

    generateShedule (id) {
      this.$http.post(`/api/generate?sheduleId=${id}`)
        .then(response => {
          console.log(response)
          this.getShedules(this.idShedule)
          this.isGenerate = false
        })
        .catch(error => {
          console.log(error)
        })
    },

    formatShedule (listShedule) {
      const uniqueGroup = new Set()
      const finalSh = {}

      listShedule.forEach(val => {
        uniqueGroup.add(val.group.name)
      })

      this.groups = uniqueGroup

      uniqueGroup.forEach(nameGroup => {
        const groupShedule = listShedule
          .filter(item => {
            return item.group.name === nameGroup
          })

        // console.log(groupShedule, 'groupShedule')
        finalSh[nameGroup] = []

        this.time.forEach(timeDef => {
          finalSh[nameGroup].push({
            time: timeDef,
            mon: groupShedule.find(item => {
              return item.time === timeDef && item.day_week === 'пн'
            }),
            tue: groupShedule.find(item => {
              return item.time === timeDef && item.day_week === 'вт'
            }),
            wen: groupShedule.find(item => {
              return item.time === timeDef && item.day_week === 'ср'
            }),
            thu: groupShedule.find(item => {
              return item.time === timeDef && item.day_week === 'чт'
            }),
            fri: groupShedule.find(item => {
              return item.time === timeDef && item.day_week === 'пт'
            })
          })
        })
      })

      return finalSh
    },

    getSubjects (shedules) {
      for (const shedule in shedules) {
        shedules[shedule].forEach(val => {
          for (const dayWeek in val) {
            if (val[dayWeek] === undefined) {
              val[dayWeek] = ''
            }

            if (val[dayWeek] !== undefined && typeof val[dayWeek] === 'object') {
              val[dayWeek] = val[dayWeek].discipline.name + '\n' + val[dayWeek].auditurium.name + '\n' + val[dayWeek].teacher.name
            }
          }
        })
      }
    }
  }
}
</script>
