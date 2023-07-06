<script setup>
import SplitContentView from "@/components/splitViews/splitContentView.vue";
import {ref} from "vue";

const treeInfo = ref([
  {
    title: "项目根目录",
    key: "root",
    children: [
      { title: '导入的文件', key: '0-0-0-1' },
      { title: 'leaf', key: '0-0-0-2' },
    ]
  }
])
</script>

<template>
<split-content-view :content-absolute-center="false">
  <template #menu>
    <h1 style="margin-top: 20px">模板编辑器</h1>
    <a-dropdown>
      <template #overlay>
        <a-menu>
          <a-menu-item key="createFile">创建文件</a-menu-item>
          <a-menu-item key="createFile">创建文件夹</a-menu-item>
          <a-menu-item key="createFile">导入文件</a-menu-item>
        </a-menu>
      </template>
      <a-button type="primary" style="margin-top: 5px">添加……</a-button>
    </a-dropdown>
    <div class="auto-flex-box">
      <a-tree v-model:tree-data="treeInfo" show-line></a-tree>
    </div>
    <div class="row-display">
      <a-button type="primary" class="row-item">保存并退出</a-button>
      <a-button type="default" danger class="row-item">直接退出</a-button>
    </div>
  </template>
</split-content-view>
</template>

<style scoped>
.auto-flex-box {
  display: flex;
  flex-direction: column;
  flex: auto;
  margin-top: 10px;
  margin-bottom: 5px;
}
.row-display {
  display: flex;
  flex-direction: row;
}
.row-item {
  margin: 5px;
  flex: auto;
}
</style>