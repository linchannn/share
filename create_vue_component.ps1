param([string]$fileName)
# create empty .vue file
New-Item -Path "$fileName" -ItemType "file" -Force | Out-Null

# write the vue component template into the file created
@"
<script setup lang="ts"></script>

<template></template>

<style scoped>/* 共通スタイル */</style>
"@ | Set-Content -Path "$fileName"
