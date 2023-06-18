<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
</script>

<script>
export default {
  data() {
    return {
      tagsInfo: {},
      creationDate: "",
      description: "",
      isLoadingTagData: false,
      isLoadingRelatedProject: true,
    }
  },
  methods: {
    async getTagInfo() {
      let targetTagsInfo = await window.tags.openMetadataFile()
      this.tagsInfo = targetTagsInfo
      console.log('triggered')
      console.log(targetTagsInfo)
      console.log(this.tagsInfo)
      return targetTagsInfo
    },
    getCreationDate(tagName) {
      this.getTagInfo().then(result=>{
        document.getElementById('tagDetails:tagCreationDate').innerText = result[tagName].creationDate
      })
    },
    getDescription(tagName) {
      this.getTagInfo().then(result => {
        this.description = result[tagName].description
      })
    }
  },
  watch: {
    $route: {
      immediate: true,
      handler() {
        if (this.$route.params.tagName) {
          this.getCreationDate(this.$route.params.tagName)
          this.getDescription(this.$route.params.tagName)
        }
      }
    }
  }
}
</script>

<template>
<header-content-view :title="$route.params.tagName" sub-title="标签详情">
  <h2>标签基本信息</h2>
  <a-spin :indicator="Loading" :spinning="isLoadingTagData" tip="正在获取标签数据信息">
    <div class="row-display">
      <div><b>标签名称：</b></div> {{$route.params.tagName}}
    </div>
    <div class="row-display">
      <div><b>创建日期：</b></div> <div id="tagDetails:tagCreationDate"></div>
    </div>
    <div><b>简介：</b></div>
    <a-textarea placeholder="此项目暂时还没有简介" v-model:value="description" disabled></a-textarea>
    <div class="row-display">
      <a-button type="primary">修改项目属性</a-button>
    </div>
  </a-spin>
  <a-divider></a-divider>
  <h2>关联项目</h2>
  相关联的项目将会全部显示在此处
  <a-spin :spinning="isLoadingRelatedProject" tip="正在获取相关项目信息"></a-spin>
</header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  margin-top: 5px;
}
</style>