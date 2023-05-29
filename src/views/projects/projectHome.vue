<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";
import {ref} from "vue";


const targetProjectList = ref([
  {
    "url": "/1",
    "icon": "",
    "content": "测试项目1"
  },
  {
    "url": "/1",
    "icon": "",
    "content": "测试项目2"
  },
  {
    "url": "/1",
    "icon": "",
    "content": "测试项目3"
  },
])
</script>

<template>
  <split-content-view :content-absolute-center="true">
    <template #menu>
      <h1 style="margin-top: 20px">项目列表</h1>
      <div>您可以在这里创建并查看所有的项目</div>
      <menu-button type="primary">
        <img src="@/assets/icons/icon-add-white.svg" height="16">
        <div>创建一个新项目</div>
      </menu-button>
      <menu-button type="minor">
        <img src="@/assets/icons/icon-add-blue.svg" height="16">
        <div>从本地添加项目</div>
      </menu-button>
      <div style="margin: 5px">
        <a-input-search placeholder="搜索项目名称"></a-input-search>
      </div>
      <LinkMenu :content-list="targetProjectList">

      </LinkMenu>
      <div class="row-display">
        <menu-button type="minor" style="flex: 1">
          <img src="@/assets/icons/search-blue.svg" height="16">
          <div>高级搜索</div>
        </menu-button>
        <menu-button type="minor" style="flex: 1">
          <img src="@/assets/icons/search-blue.svg" height="16">
          <div>按标签查找</div>
        </menu-button>
      </div>
    </template>
    <template #content>在左侧点击一个项目条例以查看详细信息，若没有则创建一个新项目</template>
  </split-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: fit-content;
}
</style>