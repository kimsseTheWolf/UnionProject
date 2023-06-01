<script setup>
import {ref} from "vue";

const displayModal = ref(false)
async function checkInitializeStatus() {
  let result = await window.config.checkGlobalConfigInitialization()
  console.log(result)
  if (!result.status) {
    displayModal.value = true
  }
}

function handleCloseDialog() {
  displayModal.value = false
}

checkInitializeStatus()
</script>

<template>
  <a-modal title="初始化警告" :visible="displayModal" @cancel="handleCloseDialog()">
    <div class="column-box">
      <div>Union Project 在初始化项目列表时出现了一些问题，这些问题<b>不会</b>导致你的项目在你的本地丢失。您可以选择一个选项来设置初始化选项。</div>
      <div>您可以让系统自动使用默认值，或者手动选择一个项目元数据存放地址。</div>
    </div>
    <template #footer>
      <a-button type="primary">打开设置</a-button>
      <a-button>使用默认值</a-button>
    </template>
  </a-modal>
</template>

<style scoped>
.column-box{
  display: flex;
  flex-direction: column;
  width: auto;
  height: fit-content;
}
</style>