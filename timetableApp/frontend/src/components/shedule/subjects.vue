<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="subjects"
          :items-per-page="5"
          class="elevation-1"
        ></v-data-table>
        <v-row no-gutters justify="end">
          <div style="margin-top: 10px;">
            <v-btn>Добавить предмет</v-btn>
          </div>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>


<script>
export default {
  data: () => ({
    headers: [
      {
        text: 'Название класса',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Количество учеников', value: 'count' },
    ],
    classes: [
      {
        name: '1a',
        count: '20',
      },
      {
        name: '1б',
        count: '20',
      },
      {
        name: '1в',
        count: '20',
      },
      {
        name: '2a',
        count: '20',
      },

    ]
  }),
}
</script>
