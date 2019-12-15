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
                <router-link :to="{
                  name: 'shedule',
                  params: {
                    id: sheduleId,
                    component: param.link.name
                  }
                }">
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
        <bell-ring
          v-if="isCurComp('times')"
          :idShedule="sheduleId">
        </bell-ring>
        <classes
          v-if="isCurComp('classes')"
          :idShedule="sheduleId">
        </classes>
        <subjects
          v-if="isCurComp('subjects')"
          :idShedule="sheduleId">
        </subjects>
        <teachers
          v-if="isCurComp('teachers')"
          :idShedule="sheduleId">
        </teachers>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    params: [
      {
        link: {
          name: 'times'
        },
        text: 'Звонки'
      },
      {
        link: {
          name: 'classes'
        },
        text: 'Классы'
      },
      {
        link: {
          name: 'subjects'
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
          name: 'teachers'
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
    classes: () => import('../components/shedule/classes'),
    subjects: () => import('../components/shedule/subjects'),
    teachers: () => import('../components/shedule/teachers')

  },
  computed: {
    sheduleId () {
      return this.$route.params.id
    }
  },
  methods: {
    isCurComp (name) {
      return this.$route.params.component === name
    }
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
