<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {computed, ref} from "vue";
import {useRouter} from "vue-router";
import CreateTag from "@/views/tags/createTag.vue";
import CreateScriptCreater from "@/components/explorer/createScriptCreater.vue";
import {message} from "ant-design-vue";

const router = useRouter()

const projectName = ref("")
const projectDescription = ref("")
const projectTags = ref([])
const availableTagsNames = ref([])
const availableCreationMethods = ref([])
const availableTagsInfo = ref({})
const storeMethod = ref("inApp")
const projectStoreLocation = ref("")
const selectedMethodName = ref("notSelected")

const tagMenuSelectedItem = ref([])

const displayCreateTagPage = ref(false)
const displayDirUnsafeWarning = ref(false)

const stepCount = ref(1)

const okayToCreate = computed(()=>{

})

async function getTagsData() {
  // hide the modal
  displayCreateTagPage.value = false
  // read and apply tags metadata to react value
  let tagsName = await window.tags.openMetadataFile()
  availableTagsInfo.value = tagsName
  // apply the keys to the list
  availableTagsNames.value = Object.keys(tagsName)
}

function handleTagMenuOnselect() {
  if (tagMenuSelectedItem.value.indexOf('unionProject:createNewTag') !== -1) {
    handleCreateTagPage()
  }
}

function handleCreateTagPage() {
  displayCreateTagPage.value = !displayCreateTagPage.value
}

function handleTagSelected(tagName) {
  // identify whether the item has already added to the list
  if (projectTags.value.indexOf(tagName) !== -1) {
    return
  }
  // add the name of the tag to the selected list
  projectTags.value.push(tagName)
}

function handleTagDeleted(tagName) {
  // identify whether the tag is existed in the list
  if (projectTags.value.indexOf(tagName) === -1) {
    return
  }
  // remove the tag from the list using the tag name
  let targetIndex = projectTags.value.indexOf(tagName)
  projectTags.value.splice(targetIndex, 1)
}

async function checkDirIsSafe(dir) {
  let result = await window.fs.checkDirectoryIsEmpty(dir)
  if (!result) {
    displayDirUnsafeWarning.value = true
    return
  }
  displayDirUnsafeWarning.value = false
}

async function triggerOpenFolderSelection() {
  let result = await window.fs.openFolderDialog(false, "", "选择一个文件夹")
  // apply the store location to the app
  if (result === undefined) {
    projectStoreLocation.value = ""
    return
  }
  projectStoreLocation.value = result[0]
  await checkDirIsSafe(projectStoreLocation.value)
}

async function getCreateMethods() {
  let result = await window.project.getCreateMethods()
  availableCreationMethods.value = result[0]
}

// Init process
getTagsData()
getCreateMethods()
</script>

<template>
  <header-content-view title="创建新项目" sub-title="设置您希望如何创建这个新项目">

    <div v-if="stepCount === 1">
      <h2>项目基本信息</h2>
      <div><b>项目名称</b></div>
      <a-input v-model:value="projectName"></a-input>
      <div class="column-item"><b>项目简介</b></div>
      <a-textarea v-model:value="projectDescription"></a-textarea>
      <div class="column-item"><b>项目标签</b></div>
      <div class="row-display">
        <a-tag v-for="tag in projectTags" :key="tag" :closable="true" @close="handleTagDeleted(tag)" :color="availableTagsInfo[tag].color">{{tag}}</a-tag>
      </div>
      <a-dropdown class="column-item">
        <template #overlay>
          <a-menu>
            <a-menu-item-group>
              <template #title>使用现有的标签</template>
              <a-menu-item v-for="tagName in availableTagsNames" :key="tagName" @click="handleTagSelected(tagName)">
                {{tagName}}
              </a-menu-item>
            </a-menu-item-group>
            <a-menu-item-group>
              <template #title>没有想要的标签？</template>
              <a-menu-item key="unionProject:createNewTag" @click="handleCreateTagPage">
                创建一个新的标签
              </a-menu-item>
            </a-menu-item-group>
          </a-menu>
        </template>
        <a-button>添加新的标签</a-button>
      </a-dropdown>
      <a-divider></a-divider>

      <h2>项目存储方式</h2>
      <div>选择您想要如何存储项目的相关文件</div>
      <div class="column-item"><b>存放方式</b></div>
      <a-select v-model:value="storeMethod">
        <a-select-option value="inApp">将项目数据存储在应用程序内</a-select-option>
        <a-select-option value="local">将项目数据存储在本地的其他位置上</a-select-option>
      </a-select>
      <div class="column-item" id="description" v-if="storeMethod === 'inApp'">此方法将会把你的所有项目相关文件（元数据文件与文档）存储在Union Project的运行目录下。</div>
      <div class="column-item" id="description" v-if="storeMethod === 'local'">此方法将会把你的所有项目相关文件（元数据文件与文档）存储在您指定的目录下</div>
      <div class="column-item" v-if="storeMethod === 'local'">
        <div><b>选择本地存储位置</b></div>
        <div class="row-display">
          <a-input placeholder="选择文件位置" class="row-item" v-model:value="projectStoreLocation"></a-input>
          <a-button type="primary" @click="triggerOpenFolderSelection">选择文件位置</a-button>
        </div>
        <a-alert message="此目录非空" type="warning" v-if="displayDirUnsafeWarning" class="column-item">
          <template #description>
            这个目录里还有其他文件和文件夹，创建新项目的操作会覆写此文件夹中所有的数据，请妥善处理并及时备份！
          </template>
        </a-alert>
      </div>
    </div>

    <div v-if="stepCount === 2">
      <h2>使用脚本预设</h2>
      您可以选择一个脚本预设来快速创建项目。
      <div class="column-display" style="margin-top: 5px">
        <div><b>选择一个预设</b></div>
        <a-select v-model:value="selectedMethodName" class="column-item">
          <a-select-option value="notSelected">选择模板</a-select-option>
          <a-select-option v-for="i in availableCreationMethods" :value="i.file_name" :index="i">{{i.friendly_name}}</a-select-option>
          <a-select-option value="createNewScript">创建自定义模板</a-select-option>
        </a-select>
        <a-divider></a-divider>
<!--        <create-script-creater v-if="selectedMethodName === 'createNewScript'"></create-script-creater>-->
        <a-button type="primary" v-if="selectedMethodName === 'createNewScript'" @click="message.info('此功能还未上线，尽请期待！')">打开项目模板编辑器</a-button>
        <a-divider></a-divider>
      </div>
    </div>

    <div style="margin-top: 10px" class="row-display">
      <a-button type="primary" :disabled="stepCount >= 2" class="row-item" v-on:click="stepCount++">下一步</a-button>
      <a-button :disabled="stepCount <= 1" class="row-item" v-on:click="stepCount--">上一步</a-button>
    </div>


    <a-modal title="创建一个新的标签" :visible="displayCreateTagPage">
      <create-tag @on-create-tag="getTagsData"></create-tag>
      <template #footer>
        <a-button @click="handleCreateTagPage">取消</a-button>
      </template>
    </a-modal>
  </header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
}
.row-item {
  margin-right: 5px;
}
.column-display {
  display: flex;
  flex-direction: column;
}
.column-item {
  margin-top: 5px;
}
#description {
  color: gray;
}
</style>