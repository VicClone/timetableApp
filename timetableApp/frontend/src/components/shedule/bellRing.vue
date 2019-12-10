<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="times"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
export default {
  data: () => ({
    headers: [
      {
        text: '№ урока',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Начало', value: 'start' },
      { text: 'Окончание', value: 'end' },
    ],
    times: [
      {
        name: 'Урок 1',
        start: '8:00',
        end: '8:45',
      },
      {
        name: 'Урок 2',
        start: '9:00',
        end: '9:45',
      },
      {
        name: 'Урок 3',
        start: '10:00',
        end: '10:45',
      },
      {
        name: 'Урок 4',
        start: '11:00',
        end: '11:45',
      },
    ]
  }),
}
</script>
