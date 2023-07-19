<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";
import InitializrDialog from "@/components/initializrDialog.vue";
import StaticMenu from "@/components/menuItems/StaticMenu.vue";
import {ContainerOutlined, SearchOutlined, SettingOutlined} from "@ant-design/icons-vue"


</script>

<template>
  <split-content-view :content-absolute-center="true">
    <template #menu>
      <h1 style="margin-top: 20px">项目列表</h1>
      <div>您可以在这里创建并查看所有的项目</div>
      <router-link to="/project/create">
        <menu-button type="primary">
          <template #icon>
            <img src="@/assets/icons/icon-add-white.svg" height="16">
          </template>
          <template #content>
            <div>创建一个新项目</div>
          </template>
        </menu-button>
      </router-link>
      <menu-button type="minor">
        <template #icon>
          <img src="@/assets/icons/icon-add-blue.svg" height="16">
        </template>
        <template #content>
          <div>从本地添加项目</div>
        </template>
      </menu-button>
      <a-divider style="margin: 5px"/>
      <static-menu>
        <template #content>
          <router-link to="/project/">
            <menu-button type="minor">
              <template #icon>
                <ContainerOutlined/>
              </template>
              <template #content>
                项目列表
              </template>
            </menu-button>
          </router-link>
          <menu-button type="minor">
            <template #icon>
              <SearchOutlined/>
            </template>
            <template #content>
              全局搜索
            </template>
          </menu-button>
          <router-link to="/settings/creationScript">
            <menu-button type="minor">
              <template #icon>
                <SettingOutlined/>
              </template>
              <template #content>
                模板设置
              </template>
            </menu-button>
          </router-link>
        </template>
      </static-menu>
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