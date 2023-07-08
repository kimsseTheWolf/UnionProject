<script setup>
import SplitContentView from "@/components/splitViews/splitContentView.vue";
import {ref} from "vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {message} from "ant-design-vue";

const treeInfo = ref([
  {
    title: "项目根目录",
    key: "/root",
    type: "folder",
    children: [

    ],
    isLeaf: false
  }
])
const treeKeyList = ref(["/root"])

const selectedObject = ref([])

const displayCreateFolderDialog = ref(false)
const newFolderName = ref("")
const displayCreateFileDialog = ref(false)
const newFileName = ref("")


let treeQueue = []
let convertTreeInfo = {}
async function appendChild(targetNode, targetKey, appendObj) {
  if (targetNode === undefined) {
    return
  }
  else {
    if (targetNode.key === targetKey) {
      // append the object to the children
      targetNode.children.push(appendObj)
      treeKeyList.value.push(appendObj.key)
      return
    }
    if (targetNode.children !== undefined) {
      for (let i = 0; i < targetNode.children.length; i++) {
        await appendChild(targetNode.children[i], targetKey, appendObj)
      }
    }
    return
  }
}

async function checkSameObj(objectKeyName) {
  return treeKeyList.value.indexOf(objectKeyName) !== -1;

}

async function appendFolder(selectedKeyName, folderName) {
  // check whether has the exact same object
  let result = await checkSameObj(selectedKeyName + "/" + folderName)
  // iterate the tree and find the children of the key node
  console.log(result)
  if (!result) {
    await appendChild(treeInfo.value[0], selectedKeyName, {
      title: folderName,
      key: selectedKeyName + "/" + folderName,
      type: "folder",
      children: [],
      isLeaf: false
    })
    displayCreateFolderDialog.value = false
    newFolderName.value = ""
  }
  else {
    message.warn("此名称已存在")
  }
}

async function appendFile(selectedKeyName, fileName) {
  // check whether has the exact same object
  let result = await checkSameObj(selectedKeyName + "/" + fileName)
  // iterate the tree and find the children of the key node
  console.log(result)
  if (!result) {
    await appendChild(treeInfo.value[0], selectedKeyName, {
      title: fileName,
      key: selectedKeyName + "/" + fileName,
      type: "file",
      children: [],
      isLeaf: true
    })
    displayCreateFileDialog.value = false
    newFileName.value = ""
  }
  else {
    message.warn("此名称已存在")
  }
}


</script>

<template>
<split-content-view :content-absolute-center="false" menu-style="white-menu">
  <template #menu>
    <h1 style="margin-top: 20px">模板编辑器</h1>
    <a-dropdown>
      <template #overlay>
        <a-menu>
          <a-menu-item key="createFile"  @click="displayCreateFileDialog = !displayCreateFileDialog">创建文件</a-menu-item>
          <a-menu-item key="createFile" @click="displayCreateFolderDialog = !displayCreateFolderDialog">创建文件夹</a-menu-item>
          <a-menu-item key="importFile">导入文件</a-menu-item>
        </a-menu>
      </template>
      <menu-button type="primary" style="margin-top: 5px">添加……</menu-button>
    </a-dropdown>
    <div class="auto-flex-box">
      <a-directory-tree v-model:tree-data="treeInfo" v-model:selected-keys="selectedObject" block-node style="background: rgba(255,255,255,0) !important;" :draggable="true"></a-directory-tree>
    </div>
    <div class="row-display">
      <menu-button type="minor" class="row-item">保存并退出</menu-button>
      <menu-button type="minor" class="row-item">直接退出</menu-button>
    </div>
  </template>
  <template #content>
    <header-content-view title="创建行为预览" sub-title="编辑并管理模板的创建行为">
      <a-button>Test</a-button>
    </header-content-view>
  </template>
</split-content-view>

  <a-modal title="创建文件夹" v-model:visible="displayCreateFolderDialog">
    <div class="column-display">
      <div class="column-item">输入文件夹名称</div>
      <a-input class="column-item" v-model:value="newFolderName"></a-input>
    </div>
    <template #footer>
      <a-button type="primary" class="row-item" @click="appendFolder(selectedObject[0], newFolderName)">创建文件夹</a-button>
      <a-button @click="displayCreateFolderDialog = !displayCreateFolderDialog">关闭</a-button>
    </template>
  </a-modal>

  <a-modal title="创建文件" v-model:visible="displayCreateFileDialog">
    <div class="column-display">
      <div class="column-item">输入文件名称</div>
      <a-input class="column-item" v-model:value="newFileName"></a-input>
    </div>
    <template #footer>
      <a-button type="primary" class="row-item" @click="appendFile(selectedObject[0], newFileName)">创建文件</a-button>
      <a-button @click="displayCreateFileDialog = !displayCreateFileDialog">关闭</a-button>
    </template>
  </a-modal>
</template>

<style scoped>
.auto-flex-box {
  display: flex;
  flex-direction: column;
  flex: auto;
  margin: 10px;
}
.row-display {
  display: flex;
  flex-direction: row;
}
.row-item {
  margin: 5px;
  flex: auto;
}
.column-display {
  display: flex;
  flex-direction: column;
}
.column-display .column-item {
  margin-bottom: 5px;
}
</style>