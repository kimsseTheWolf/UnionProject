<script setup>
import {ref} from "vue";
import {Modal} from "ant-design-vue";

const displayModal = ref(false)
async function checkInitializeStatus() {
  let result = await window.config.checkGlobalConfigInitialization()
  console.log(result)
  if (result === undefined) {
    displayModal.value = true
  }
}

function createSuccessDialog() {
  Modal.success({
    'title': '初始化成功',
    'content': '请重新启动应用程序来应用本次更改',
    onOk() {
      console.log('exit')
    }
  })
}

async function reinitializeMetadata() {
  createSuccessDialog()
}

function handleCloseDialog() {
  displayModal.value = false
}

checkInitializeStatus()
</script>

<template>
  <a-modal title="配置文件警告" :visible="displayModal" @cancel="handleCloseDialog()">
    <div class="column-box">
      <div>我们无法读取Union Project的配置文件与项目元数据，但是您的项目数据不会丢失</div>
      <div>您可以选择重新导入这些项目，或者继续创建新的项目。</div>
      <div>若您经常或每一次都遇到这个问题，请提交Issue至我们的仓库！</div>
    </div>
    <template #footer>
      <a-button type="primary">初始化并导入数据</a-button>
      <a-button @click="reinitializeMetadata()">初始化并继续</a-button>
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