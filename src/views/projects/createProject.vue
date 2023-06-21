<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {ref} from "vue";
import {useRouter} from "vue-router";
import CreateTag from "@/views/tags/createTag.vue";

const router = useRouter()

const projectName = ref("")
const projectDescription = ref("")
const projectTags = ref([])
const availableTagsNames = ref([])
const availableTagsInfo = ref({})

const tagMenuSelectedItem = ref([])

const displayCreateTagPage = ref(false)

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

// Init process
getTagsData()
</script>

<template>
  <header-content-view title="创建新项目" sub-title="设置您希望如何创建这个新项目">
    <h2>项目基本信息</h2>
    <div>项目名称</div>
    <a-input v-model:value="projectName"></a-input>
    <div class="column-item">项目简介</div>
    <a-textarea v-model:value="projectDescription"></a-textarea>
    <div class="column-item">项目标签</div>
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
    <h2>项目预设</h2>
    您可以通过项目预设来快速创建含有内容的项目


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
.column-item {
  margin-top: 5px;
}
</style>