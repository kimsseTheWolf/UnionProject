<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import LinkMenu from "@/components/menuItems/LinkMenu.vue";
import {ref} from "vue";

const tagsList = ref([]) // The list to store all the tags from the file
const publicPath = ref(process.env.BASE_URL)

async function getTagsFromMetaFile() {
  // clear the list first
  tagsList.value = []
  // read data from file
  let tagsInfo = await window.tags.openMetadataFile()
  let keysList = Object.keys(tagsInfo)
  // generate single units and append
  for (let i = 0; i < keysList.length; i++) {
    let singleUnitObject = {}
    singleUnitObject['url'] = "/tags/details/" + keysList[i]
    singleUnitObject['icon'] = tagsInfo[keysList[i]]["color"]
    singleUnitObject['content'] = keysList[i]
    // append
    tagsList.value.push(singleUnitObject)
  }
  console.log(tagsList.value)
}

getTagsFromMetaFile()

</script>

<template>
  <split-content-view :content-absolute-center="true">
    <template #menu>
      <h1 style="margin-top: 20px">标签</h1>
      使用标签分类你的项目
      <router-link to="/tags/create">
        <menu-button type="primary">
          <img src="@/assets/icons/icon-add-white.svg" width="16">
          创建新标签
        </menu-button>
      </router-link>
      <div style="margin: 5px">
        <a-input-search placeholder="搜索标签名称"></a-input-search>
      </div>
      <link-menu :content-list="tagsList"></link-menu>
    </template>
    <template #content>
      <router-view @onCreateTag="getTagsFromMetaFile" @onDeleteTag="getTagsFromMetaFile"></router-view>
    </template>
  </split-content-view>
</template>

<style scoped>

</style>