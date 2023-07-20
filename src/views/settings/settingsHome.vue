<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";
import {ref} from 'vue'
import StaticMenu from "@/components/menuItems/StaticMenu.vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import {SafetyCertificateOutlined, AppstoreOutlined, GlobalOutlined, InfoCircleOutlined} from "@ant-design/icons-vue"

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
      <static-menu>
        <template #content>
          <router-link to="/settings/security">
            <menu-button type="minor">
              <template #icon>
                <safetyCertificateOutlined/>
              </template>
              <template #content>
                安全
              </template>
            </menu-button>
          </router-link>
          <router-link to="/settings/creationScript">
            <menu-button type="minor">
              <template #icon>
                <AppstoreOutlined/>
              </template>
              <template #content>
                项目模板与管理
              </template>
            </menu-button>
          </router-link>
          <menu-button type="minor">
            <template #icon>
              <GlobalOutlined/>
            </template>
            <template #content>
              语言与地区
            </template>
          </menu-button>
          <router-link to="/settings/about">
            <menu-button type="minor">
              <template #icon>
                <InfoCircleOutlined/>
              </template>
              <template #content>
                关于 Union Project
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
</template>

<style scoped>

</style>