<template>
  <v-container fluid>
    <v-row>
      <v-col class="shedule__params" cols="3" style="background: red">
        <div>
          <router-link :to="{name: 'home'}">
            Звонки
          </router-link>
        </div>
        <router-link :to="{name: 'home'}">
          Звонки
        </router-link>
      </v-col>
      <v-col cols="9" style="background: blue">
        Параметры
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {

}
</script>
