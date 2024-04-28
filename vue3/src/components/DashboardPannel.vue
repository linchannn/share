<template lang="pug">
v-container(fluid)
  div.dashboard-pannel
    v-row
      v-col
        v-card
          p テナントID
      v-col(cols="9", align="right")
        v-card
          p aaa
    v-row
      v-col
        v-card
          p 質問回数
      v-col
        v-card
          p 新規登録ファイル数
      v-col
        v-card
          p 新規登録ファイル容量
      v-col
        v-card
          p ストレージ容量
</template>

<script setup lang="ts"></script>

<style scoped>
.dashboard-pannel {
  background-color: gray;
}
.dashboard-card {
  background-color: white;
}
</style>
