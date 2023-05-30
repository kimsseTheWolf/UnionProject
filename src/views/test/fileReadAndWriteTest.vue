<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {ref} from "vue";
import {message} from "ant-design-vue"

const fileContent = ref("")
const fileLocation = ref("")
async function triggerReadFile(fileLocation){
  fileContent.value = await window.fs.openFile(fileLocation)
  if (fileContent.value === "") {
    message.warning("读取文件失败")
  }
  message.success("读取成功，请检查是否已在文本框内显示！")
}

async function triggerWriteFile(fileLocation, fileContent) {
  let result = await window.fs.writeFile(fileLocation, fileContent)
  if (result) {
    message.success("文件写入成功，请查看源文件")
  }
  else {
    message.warning("文件写入失败")
  }
}
</script>

<template>
  <HeaderContentView title="文件读写测试" sub-title="测试文件API是否正常">
    文件地址
    <div style="display: flex; flex-direction: row">
      <a-input placeholder="输入文件地址" v-model:value="fileLocation"></a-input>
      <a-button type="primary" @click="triggerReadFile(fileLocation)">打开文件</a-button>
    </div>
    文件内容
    <a-textarea style="flex: auto" v-model:value="fileContent">
    </a-textarea>
    <div style="display: flex; flex-direction: row">
      <a-button type="primary" @click="triggerWriteFile(fileLocation, fileContent)">写入</a-button>
    </div>
  </HeaderContentView>
</template>

<style scoped>

</style>