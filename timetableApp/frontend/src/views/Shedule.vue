<template>
  <v-container fluid>
    <v-row>
      <v-col class="shedule__params" cols="3">
        <v-list>
          <v-subheader>Параметры</v-subheader>
          <v-list-item-group color="primary">
            <v-list-item
              v-for="(param, i) in params"
              :key="i"
            >
              <v-list-item-content>
                <router-link :to="param.link">
                  <v-list-item-title class="params__text">
                    {{ param.text }}
                  </v-list-item-title>
                </router-link>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
      <v-col cols="9">
        <bell-ring v-if="false"></bell-ring>
        <classes></classes>
      </v-col>
    </v-row>
    <v-row>
      <v-btn @click="getShedules">Получить расписания для текущего пользователя</v-btn>
      <div>
        <pre>{{ this.shedule }}</pre>
      </div>

      <v-btn @click="addShedule">Добавить расписание</v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    params: [
      {
        link: {
          name: 'home'
        },
        text: 'Звонки'
      },
      {
        link: {
          name: 'home'
        },
        text: 'Классы'
      },
      {
        link: {
          name: 'home'
        },
        text: 'Предметы'
      },
      {
        link: {
          name: 'home'
        },
        text: 'Нагрузка класса по предметам'
      },
      {
        link: {
          name: 'home'
        },
        text: 'Учителя'
      },
      {
        link: {
          name: 'home'
        },
        text: 'Кабинеты'
      },
      {
        link: {
          name: 'home'
        },
        text: 'Настройки расписания'
      }
    ],
    shedule: null
  }),
  components: {
    bellRing: () => import('../components/shedule/bellRing'),
    classes: () => import('../components/shedule/classes')
  },
  methods: {
  }
}
</script>

<style>
  .shedule__params .router-link-active {
    text-decoration: none;
  }

  .params__text{
    font-size: 18px;
    color: #000;
    text-decoration: none;
  }
</style>
