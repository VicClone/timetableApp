<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="workloads"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn @click="isAddWorkload = true">Добавить нагрузку</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="isAddWorkload"
      max-width="600">
      <v-card>
        <v-card-title>
          <h3>Добавить нагрузку</h3>
        </v-card-title>
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
        <v-card-text>
          <v-text-field
            v-model="formWorkload.amount"
            label="Количество"
            outlined>
          </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="isAddWorkload = false">
            Отмена
          </v-btn>
          <v-btn @click="addWorkload(idClass, subValue)">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  props: ['idClass', 'idShedule'],

  data: () => ({
    headers: [
      {
        text: 'Название предмета',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Нагрузка', value: 'amount' }
    ],
    workloads: [],
    subjects: [],
    subValue: null,
    group: null,
    isAddWorkload: false,
    formWorkload: {
      amount: ''
    }
  }),

  created () {
    this.$nextTick(() => {
      this.getSubjects(this.idShedule)
      this.getWorkloads(this.idClass)
    })
  },

  methods: {
    getWorkloads (id) {
      const vm = this
      this.$http.get(`/api/workloadGroups?groupId=${id}`)
        .then(response => {
          console.log(response, 'workgroup')
          this.workloads = response.data.map(workloadData => {
            return {
              name: vm.getNameSub(workloadData.discipline),
              amount: workloadData.amount
            }
          })
        })
        .catch(error => {
          console.log(error)
        })
    },
    addWorkload (idGroup, idSub) {
      this.$http.post(`/api/workloadGroups?groupId=${idGroup}&disciplineId=${idSub}`, {
        amount: this.formWorkload.amount
      })
        .then(response => {
          this.getWorkloads(idGroup)
        })
        .catch(error => {
          console.log(error)
        })
        .finally(() => {
          this.isAddWorkload = false
        })
    },
    getSubjects (id) {
      this.$http.get(`/api/subjects?sheduleId=${id}`)
        .then(response => {
          console.log(response)
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
    getNameSub (id) {
      const sub = this.subjects.find((el) => {
        return el.id === id
      })

      return sub.name
    }
  }
}
</script>
