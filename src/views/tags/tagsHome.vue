<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";

</script>

<template>
  <split-content-view :content-absolute-center="true">
    <template #menu>
      <h1 style="margin-top: 20px">标签</h1>
      使用标签分类你的项目
      <router-link to="/tags/create">
        <menu-button type="primary">
          <img src="@/assets/icons/icon-add-white.svg" width="16">
          创建新标签
        </menu-button>
      </router-link>
      <div style="margin: 5px">
        <a-input-search placeholder="搜索标签名称"></a-input-search>
      </div>
      <link-menu content-list=""></link-menu>
    </template>
    <template #content>
      <router-view></router-view>
    </template>
  </split-content-view>
</template>

<style scoped>

</style>