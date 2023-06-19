<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
</script>

<script>
import {message} from "ant-design-vue";
import {defineEmits} from 'vue'

export default {
  data() {
    return {
      tagsInfo: {},
      creationDate: "",
      description: "",
      isLoadingTagData: false,
      isLoadingRelatedProject: true,
      showDeleteDialog: false,
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
    },
    async deleteTag(tagName) {
      let result = await window.tags.deleteTag(tagName)
      if (result.status) {
        message.success('删除成功')
        this.$emit('onDeleteTag')
        // hide
        this.showDeleteDialog = !this.showDeleteDialog
        this.$router.push('/tags')
      }
      else {
        message.error('删除标签时出现错误')
      }
    },
    showDeleteWarningDialog() {
      this.showDeleteDialog = !this.showDeleteDialog
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
<header-content-view title="标签详情" :sub-title="$route.params.tagName + '的标签详情'">
  <h2>标签基本信息</h2>
  <a-spin :spinning="isLoadingTagData" tip="正在获取标签数据信息">
    <div class="row-display">
      <div><b>标签名称：</b></div> {{$route.params.tagName}}
    </div>
    <div class="row-display">
      <div><b>创建日期：</b></div> <div id="tagDetails:tagCreationDate"></div>
    </div>
    <div><b>简介：</b></div>
    <a-textarea placeholder="此项目暂时还没有简介" v-model:value="description" disabled></a-textarea>
    <div class="row-display">
      <router-link :to="'/tags/modify/'+$route.params.tagName">
        <a-button type="primary" class="inline-button">修改项目属性</a-button>
      </router-link>
      <a-button type="primary" class="inline-button" danger @click="showDeleteWarningDialog">删除标签</a-button>
    </div>
  </a-spin>
  <a-modal title="您确定要继续删除吗" :visible="showDeleteDialog" :closable="false">
    删除标签并不会删除您所属标签的项目，但是标签本身会被删除。您确定要继续吗？
    <template #footer>
      <a-button type="primary" danger @click="deleteTag($route.params.tagName)">继续删除</a-button>
      <a-button @click="showDeleteWarningDialog">取消</a-button>
    </template>
  </a-modal>
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
.inline-button {
  margin-right: 5px;
}
</style>