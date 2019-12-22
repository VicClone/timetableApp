<template>
  <v-container>
    <h1>Расписание звонков</h1>
    <v-row>
      <v-col xs12>
        <v-data-table
          :headers="headers"
          :items="times"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
      </v-col>
    </v-row>
    <v-row no-gutters>
      <v-btn-toggle
        v-model="toggle_exclusive"
        mandatory
      >
        <v-btn
          v-for="(dayWeek, i) in dayWeeks" :key="i"
          @click="setDayWeek(i)">
          <span>{{ dayWeek }}</span>
        </v-btn>
      </v-btn-toggle>
      <v-spacer></v-spacer>
      <v-btn @click="isAddTime = true">Добавить звонок</v-btn>
    </v-row>
    <v-dialog
      v-model="isAddTime"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить звонок</h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
              v-model="formTime.number"
              label="Номер урока"
              outlined>
            </v-text-field>
            <v-row>
              <v-col xs6>
                <v-text-field
                  v-model="formTime.start"
                  readonly
                  label="Начало"
                  outlined
                  @click="menu.start = true">
                </v-text-field>
                <v-menu
                  v-model="menu.start"
                  :close-on-content-click="false"
                >
                  <template v-slot:activator="{ on }">
                    <div></div>
                  </template>
                  <v-time-picker
                    v-model="formTime.start"
                    class="mt-2"
                    format="24hr"
                    :scrollable="true"
                  >
                    <v-spacer></v-spacer>
                      <v-btn @click="menu.start = false">
                        Готово
                      </v-btn>
                  </v-time-picker>
                </v-menu>
              </v-col>
              <v-col xs6>
                <v-text-field
                  v-model="formTime.end"
                  readonly
                  label="Конец"
                  outlined
                  @click="menu.end = true">
                </v-text-field>
                <v-menu
                  v-model="menu.end"
                  :close-on-content-click="false"
                >
                  <template v-slot:activator="{ on }">
                    <div></div>
                  </template>
                    <v-time-picker
                      v-model="formTime.end"
                      class="mt-2"
                      format="24hr"
                      :scrollable="true"
                    >
                      <v-spacer></v-spacer>
                      <v-btn @click="menu.end = false">
                        Готово
                      </v-btn>
                    </v-time-picker>
                </v-menu>
              </v-col>
            </v-row>
        </v-card-text>
        <v-card-text>
          <v-btn-toggle
            v-model="formTime.day_week"
            mandatory
          >
            <v-btn
              v-for="(dayWeek, i) in dayWeeks" :key="i"
              :value="i + 1">
              <span>{{ dayWeek }}</span>
            </v-btn>
          </v-btn-toggle>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddTime = false">
            Отмена
          </v-btn>
          <v-btn @click="createTime(idShedule)">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  props: ['idShedule'],
  data: () => ({
    headers: [
      {
        text: '№ урока',
        align: 'left',
        sortable: false,
        value: 'number'
      },
      { text: 'Начало', value: 'start' },
      { text: 'Окончание', value: 'end' }
    ],
    times: [],
    dayWeeks: [
      'ПН',
      'ВТ',
      'СР',
      'ЧТ',
      'ПТ',
      'СБ'
    ],
    timesOfDays: [],
    toggle_exclusive: undefined,
    isAddTime: false,
    formTime: {
      number: 1,
      start: '8:00',
      end: '8:45',
      day_week: 1
    },
    menu: {
      start: false,
      end: false
    }
  }),
  created () {
    this.$nextTick(() => {
      this.getTimes(this.idShedule)
    })
  },
  methods: {
    getTimes (id) {
      this.$http.get(`/api/times?sheduleId=${id}`)
        .then(response => {
          this.setTimes(response.data)
          this.setDayWeek(0)
        })
        .catch(error => {
          console.log(error)
        })
    },
    setTimes (timesData) {
      for (let i = 0; i < this.dayWeeks.length; i++) {
        this.timesOfDays[i] = timesData
          .filter(time => time.day_week === i + 1)
          .map(time => {
            return {
              number: time.number,
              start: time.start,
              end: time.end
            }
          })
      }
    },
    createTime (id) {
      this.$http.post(`/api/times?sheduleId=${id}`, this.formTime)
        .then(response => {
          this.getTimes(this.idShedule)
          this.isAddTime = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    setDayWeek (day) {
      this.times = this.timesOfDays[day]
    }

  }
}
</script>
