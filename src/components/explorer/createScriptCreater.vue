<script setup>
import {ref} from "vue";
import CreateFile from "@/components/explorer/createMethodFormElements/createFile.vue";
const file_content = ref([])
const method_name = ref("")
const method_description = ref("")

function appendOperation(operationName) {
  if (operationName === "createFile") {
    file_content.value.push({
      method: "create",
      type: "file",
      name: ""
    })
  }
}
</script>

<template>
  <div class="column-display">
    <div class="column-item">
      <h2>创建模板语法</h2>
      <div>通过创建模板可以告诉应用你想如何创建一个项目</div>
    </div>

    <div class="column-item">
      <a-input placeholder="模板名称" v-model:value="method_name" class="column-item"></a-input>
      <a-textarea placeholder="模板描述" v-model:value="method_description" class="column-item"></a-textarea>
    </div>

    <div class="column-item">
      <a-empty description="目前还没有操作可以执行" v-if="file_content.length === 0"></a-empty>
    </div>

    <!--  Write the iteration hierarchy here -->
    <div class="column-item" v-for="i in file_content">
      <create-file v-model="i.name"></create-file>
    </div>

    <a-dropdown>
      <a-button type="dashed" class="column-item">添加操作</a-button>
      <template #overlay>
        <a-menu>
          <a-menu-item key="createFile" @click="appendOperation('createFile')">创建文件</a-menu-item>
          <a-menu-item key="createFolder">创建文件</a-menu-item>
          <a-menu-item key="writeFile">写入文件</a-menu-item>
          <a-menu-item key="copyFile">复制文件</a-menu-item>
          <a-menu-item key="deleteFile">删除文件</a-menu-item>
          <a-menu-item key="runCommand">执行指令</a-menu-item>
        </a-menu>
      </template>
    </a-dropdown>
  </div>
</template>

<style scoped>
.column-display {
  display: flex;
  flex-direction: column;
}

.column-item {
  margin-top: 5px;
}

.row-display {
  display: flex;
  flex-direction: row;
  margin-top: 5px;
}
.row-item {
  margin-right: 5px;
}
</style>