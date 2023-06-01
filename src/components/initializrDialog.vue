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
  <a-modal title="配置文件警告" :visible="displayModal" @cancel="handleCloseDialog()">
    <div class="column-box">
      <div>我们无法读取UnionOS的配置文件与项目元数据，但是您的项目数据不会丢失</div>
      <div>您可以选择重新导入这些项目，或者继续创建新的项目。</div>
      <div>若您经常或每一次都遇到这个问题，请提交Issue至我们的仓库！</div>
    </div>
    <template #footer>
      <a-button type="primary">初始化并导入数据</a-button>
      <a-button>初始化并继续</a-button>
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