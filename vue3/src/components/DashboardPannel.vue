<template lang="pug">
div.card
  p テナントID: &nbsp; {{ tenantId }}
div.card
  span 期間
  select(v-model="selected")
    option(v-for="item in items" :value="item.value") {{ item.text }}
div.card
  p 質問回数: &nbsp; {{ queryCount }}
div.card
  p 新規登録ファイル数: &nbsp; {{ newFilesCount }}
div.card
  p 新規登録ファイル容量: &nbsp; {{ newFilesSize }}
div.card
  p ストレージ容量: &nbsp; {{ totalStorageCapacity }}
</template>

<script setup lang="ts">
import { ref } from 'vue'

const tenantId = ref<string>('12345')
const queryCount = ref<number>(0)
const newFilesCount = ref<number>(0)
const newFilesSize = ref<number>(0)
const totalStorageCapacity = ref<number>(0)

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
