<template>
  <v-container fluid>
    <h1>Мои расписания</h1>
    <v-row>
      <v-col cols="12">
        <v-data-table
          v-if="shedules.length != 0"
          v-model="selected"
          :headers="headers"
          :items="shedules"
          :items-per-page="5"
          class="elevation-1"
        >
          <template v-slot:item.link="props">
            <td>
              <router-link
                :to="{
                  name: 'shedule',
                  params: {
                    id: props.item.link.sid,
                    component: 'times'
                  }
                }">
                Открыть
              </router-link>
            </td>
          </template>
        </v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn @click="isAddShedule=!isAddShedule">Добавить расписания</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="isAddShedule"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить расписание</h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
              v-model="formShedule.fourth"
              label="Номер четверти"
              outlined>
            </v-text-field>
            <v-text-field
              v-model="formShedule.period"
              label="Учебный период (гг)"
              outlined>
            </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddShedule = false">
            Отмена
          </v-btn>
          <v-btn @click="createShedule">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    selected: [],
    headers: [
      {
        text: 'Название',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Дата создания', value: 'dateCreate' },
      { text: 'Просмотр', value: 'link' }
    ],
    shedules: [],
    isAddShedule: false,
    formShedule: {
      fourth: 0,
      period: ''
    }
  }),
  created () {
    const vw = this
    setTimeout(function () {
      vw.getShedules()
    }, 10)
  },

  methods: {
    getShedules () {
      const user = this.$store.getters['auth/user']
      this.$http.get(`api/shedulesUser?userId=${user.pk}`)
        .then(response => {
          this.shedules = this.formatShedules(response.data.data)

          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },

    formatShedules (shedules) {
      const formatShedules = shedules.map(shedule => {
        return {
          name: `Расписание ${shedule.fourth} четверть,
            ${shedule.period}гг.`,
          dateCreate: shedule.date,
          link: {
            sid: shedule.sid
          }
        }
      })

      return formatShedules
    },

    createShedule () {
      this.$http.post('api/shedules', this.formShedule)
        .then(response => {
          this.getShedules()
          this.isAddShedule = false
        })
        .catch(error => {
          console.log(error)
        })
    },

    goRoute (item) {
      console.log(item)
    }
  }
}
</script>
