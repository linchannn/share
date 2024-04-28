<template lang="pug">
v-container(fluid)
  div.dashboard-pannel
    v-row
      v-col
        v-card(color="white")
          p テナントID
      v-col(cols="9", align="right")
        v-card(color="white")
          p aaa
    v-row
      v-col
        v-card(color="white")
          p 質問回数
      v-col
        v-card(color="white")
          p 新規登録ファイル数
      v-col
        v-card(color="white")
          p 新規登録ファイル容量
      v-col
        v-card(color: "white")
          p ストレージ容量
</template>

<script setup lang="ts"></script>

<style scoped>
.dashboard-pannel {
  background-color: gray;
}
</style>
