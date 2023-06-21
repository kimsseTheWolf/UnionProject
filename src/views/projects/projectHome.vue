<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";
import InitializrDialog from "@/components/initializrDialog.vue";


</script>

<template>
  <split-content-view :content-absolute-center="true">
    <template #menu>
      <h1 style="margin-top: 20px">项目列表</h1>
      <div>您可以在这里创建并查看所有的项目</div>
      <router-link to="/project/create">
        <menu-button type="primary">
          <img src="@/assets/icons/icon-add-white.svg" height="16">
          <div>创建一个新项目</div>
        </menu-button>
      </router-link>
      <menu-button type="minor">
        <img src="@/assets/icons/icon-add-blue.svg" height="16">
        <div>从本地添加项目</div>
      </menu-button>
      <div style="margin: 5px">
        <a-input-search placeholder="搜索项目名称"></a-input-search>
      </div>
      <LinkMenu content-list="">

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
    <template #content>
      <router-view></router-view>
    </template>
  </split-content-view>
  <initializr-dialog></initializr-dialog>
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