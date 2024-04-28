<template lang="pug">
v-container(fluid)
  div.dashboard-pannel
    v-row
      v-col
        v-card.pa-4(outlined)
          v-card-title.subtitle-1 テナントID
          v-card-text
            v-label.body-1 sample
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
/* 背景色を白に設定 */
.v-card {
  background-color: white;
}

/* カードタイトルのフォントサイズを小さく設定 */
.v-card-title {
  font-size: 0.875rem; /* 14px */
}

/* カードコンテンツのフォントサイズを通常に設定 */
.v-label {
  font-size: 1rem; /* 16px */
}
</style>
