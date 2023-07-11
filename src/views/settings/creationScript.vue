<script setup>

import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import FormLine from "@/components/form/form-line.vue";
</script>

<template>
  <header-content-view title="项目模板" sub-title="管理与编辑项目模板">
    <h3>管理所有模板</h3>
    <div>在此处查看与管理所有的模板</div>
    <div class="row-display">
      <a-button type="primary">添加方法</a-button>
    </div>
    <a-divider></a-divider>
    <h3>自定义项目模板</h3>
    <div>您可以创建自己的项目模板，在以后创建项目时可以直接选择。</div>
    <form-line>
      <template #title>创建一个新的自定义项目模板</template>
      <template #description>在项目模板中打开一个模板项目以编辑自定义模板</template>
      <template #right-item>
        <router-link to="/explorer/createScriptEditor">
          <a-button type="primary">打开模板编辑器</a-button>
        </router-link>
      </template>
    </form-line>
  </header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  margin-top: 5px;
}
.row-item {
  margin-right: 5px;
}
</style>