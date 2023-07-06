<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";
import {ref} from 'vue'

const objectsList = ref([
  {
    "url": "/settings/security",
    "icon": "",
    "content": "安全"
  },
  {
    "url": "/settings/creationScript",
    "icon": "",
    "content": "项目创建"
  }
])

</script>

<template>
  <split-content-view :content-absolute-center="true">
    <template #menu>
      <h1 style="margin-top: 20px">设置</h1>
      <div>设置与配置Union Project</div>
      <link-menu :content-list="objectsList"></link-menu>
    </template>
    <template #content>
      <router-view></router-view>
    </template>
  </split-content-view>
</template>

<style scoped>

</style>