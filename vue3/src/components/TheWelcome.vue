<script setup lang="ts">
import {ref} from 'vue'
import { VBtn } from 'vuetify/components/VBtn'
import DashboardPannel from './DashboardPannel.vue'
import DashboardTable from './DashboardTable.vue'

const dt = ref<string>('2024/4/26 16:50')


const fetch = () => {
  window.alert("ふぇっ")
}
</script>

<template lang="pug">
v-container(fluid)
  v-row
    v-col
      h1 だんだんだーん
    v-col
      h3 {{ dt }} &nbsp; 現在
    v-col
      v-btn(depressed, @click="fetch()") 取得
  v-row
    v-col(cols="7")
      dashboard-pannel
  v-row
    v-col(cols="7")
      dashboard-table
</template>
<style scoped></style>
