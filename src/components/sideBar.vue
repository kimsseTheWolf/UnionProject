<template>
  <div class="side-bar">
    <router-link to="/project">
      <sidebar-button>
        <template #icon>
          <img src="@/assets/icons/Projects.svg" width="32">
        </template>
        <template #content>
          项目
        </template>
      </sidebar-button>
    </router-link>

    <router-link to="/tags">
      <sidebar-button>
        <template #icon>
          <img src="@/assets/icons/tags.svg" width="32">
        </template>
        <template #content>
          标签
        </template>
      </sidebar-button>
    </router-link>

    <router-link to="/dashboard">
      <sidebar-button>
        <template #icon>
          <img src="@/assets/icons/Dashboard.svg" width="32">
        </template>
        <template #content>
          看板
        </template>
      </sidebar-button>
    </router-link>

    <router-link to="/todo">
      <sidebar-button>
        <template #icon>
          <img src="@/assets/icons/Todos.svg" width="32">
        </template>
        <template #content>
          代办
        </template>
      </sidebar-button>
    </router-link>

    <router-link to="/settings">
      <sidebar-button>
        <template #icon>
          <img src="@/assets/icons/Settings.svg" width="32">
        </template>
        <template #content>
          设置
        </template>
      </sidebar-button>
    </router-link>
  </div>
</template>

<script setup>

import SidebarButton from "@/components/buttons/SidebarButton.vue";
</script>

<style scoped>
.side-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: fit-content;
  height: 100%;
  margin: 0;
  padding: 7px;
  background-color: dodgerblue;
  color: white;
}
</style>