<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";
import {ref} from "vue";

const contentList = ref([
  {
    "url": "/test/fs",
    "icon": "",
    "content": "文件读写测试"
  },
])
</script>

<template>
  <split-content-view :content-absolute-center="true">
    <template #menu>
      <h1 style="margin-top: 20px">测试页面</h1>
      所有测试功能的可视化测试部分
      <LinkMenu :content-list="contentList"></LinkMenu>
    </template>
    <template #content>
      <router-view>

      </router-view>
    </template>
  </split-content-view>
</template>

<style scoped>

</style>