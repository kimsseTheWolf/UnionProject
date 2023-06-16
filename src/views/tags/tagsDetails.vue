<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {ref} from "vue";

const tagsInfo = ref({})

async function getTagInfo() {
  return new Promise(async (res)=> {
    let targetTagsInfo = await window.tags.openMetadataFile()
    tagsInfo.value = targetTagsInfo
    console.log('triggered')
    console.log(targetTagsInfo)
    res(targetTagsInfo)
  })
}

async function getCreationDate(tagName) {
  let targetTagsInfo = await getTagInfo()
  return targetTagsInfo[tagName].creationDate
}

async function getDescription(tagName) {
  let targetTagsInfo = await getTagInfo()
  return targetTagsInfo[tagName].description
}

console.log(getCreationDate(`another test`))

</script>

<template>
<header-content-view :title="$route.params.tagName" sub-title="标签详情">
  <h2>标签基本信息</h2>
  <div class="row-display">
    <div><b>标签名称：</b></div> {{$route.params.tagName}}
  </div>
  <div class="row-display">
    <div><b>创建日期：</b></div> {{getCreationDate($route.params.tagName)}}
  </div>
  <div><b>简介：</b></div> {{getDescription($route.params.tagName)}}
  <a-divider></a-divider>
  <h2>关联项目</h2>
</header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
}
</style>