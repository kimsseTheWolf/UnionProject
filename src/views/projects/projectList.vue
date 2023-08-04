<script setup>

import SplitContentView from "@/components/splitViews/splitContentView.vue";
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {FormOutlined} from "@ant-design/icons-vue"
import {ref, unref} from "vue"

const tagsInfo = ref({})
const tagsNameList = ref([])

const panelActiveKeys = ref(['main'])

async function getTagsInfo() {
  tagsInfo.value = await window.tags.openMetadataFile()
  // Convert the tags name to the list
  for (let i in Object.keys(unref(tagsInfo))) {
    tagsNameList.value.push(Object.keys(unref(tagsInfo))[i])
  }
}

getTagsInfo()
</script>

<template>
  <header-content-view title="项目列表" sub-title="此处展示所有的项目">
    <a-input-search enter-button size="large" placeholder="搜索项目名称，标签名称 " style="margin-bottom: 15px"></a-input-search>
    <h2>全部项目</h2>
    <a-collapse v-model:active-key="panelActiveKeys">
      <a-collapse-panel key="main" header="所有项目">
        <a-empty/>
      </a-collapse-panel>
      <a-collapse-panel key="finished" header="已完成的项目">
        <a-empty/>
      </a-collapse-panel>
      <a-collapse-panel key="expired" header="已过期的项目">
        <a-empty/>
      </a-collapse-panel>
    </a-collapse>
    <a-divider/>
    <h2>按照标签分类</h2>
    <div style="margin-bottom: 5px">根据标签自定义分类</div>
    <a-collapse>
      <a-collapse-panel v-for="i in tagsNameList" :key="i" :header="i">
        <h3>与<a-tag :color="tagsInfo[i].color" style="margin: 5px">{{i}}</a-tag>相关的项目</h3>
        <router-link :to="'/tags/details/' + i">
          <a-button type="primary">
            <FormOutlined/>
            在标签管理器中查看此标签
          </a-button>
        </router-link>
        <a-empty/>
      </a-collapse-panel>
    </a-collapse>
  </header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.row-display .item{
  margin-right: 5px;
}
</style>