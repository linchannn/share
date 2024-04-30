<template lang="pug">
div.card
  p テナントID
  p gg
div.card
  span 期間
  select(v-model="selected")
    option(v-for="item in items" :value="item.value") {{ item.text }}
div.card
  p 質問回数
div.card
  p 新規登録ファイル数
div.card
  p 新規登録ファイル容量
div.card
  p ストレージ容量
</template>

<script setup lang="ts">
import { ref } from 'vue'
const selected = ref()
const items = [
  // セレクトボックスのオプション
  { value: 'option1', text: 'オプション1' },
  { value: 'option2', text: 'オプション2' }
  // 他のオプション...
]
</script>

<style scoped>
.card {
  border: solid;
}
</style>
