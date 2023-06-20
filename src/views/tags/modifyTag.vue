<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import FormColorSelector from "@/components/colorSelector/formColorSelector.vue";
</script>

<script>
import {message} from "ant-design-vue";

export default {
  data() {
    return {
      newTagColor: "",
      newTagDescription: "",
      newTagName: ""
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
    getTagColor(tagName) {
      this.getTagInfo().then(result=>{
        this.newTagColor = result[tagName].color
      })
    },
    getDescription(tagName) {
      this.getTagInfo().then(result => {
        this.newTagDescription = result[tagName].description
      })
    },
    getTagName() {
      this.newTagName = this.$route.params.targetTagName
    },
    async modifyTag() {
      // identify the validation of input
      if (this.newTagName === "") {
        message.warn("您必须提供一个标签名")
        return
      }
      if (this.newTagColor === "") {
        this.newTagColor = 'default'
      }

      // modify the target tag
      let result = await window.tags.modifyTag(this.$route.params.targetTagName, this.newTagName, this.newTagColor, this.newTagDescription)
      if (!result.status) {
        message.error('标签修改失败')
      }
      else {
        message.success('修改成功')
        this.$emit('onModify')
        this.$router.push('/tags/details/'+this.newTagName)
      }
    }
  },
  watch: {
    $route: {
      immediate: true,
      handler() {
        if (this.$route.params.targetTagName) {
          this.getTagName()
          this.getDescription(this.$route.params.targetTagName)
          this.getTagColor(this.$route.params.targetTagName)
          console.log(this.newTagColor)
        }
      }
    }
  }
}
</script>

<template>
<header-content-view title="修改标签" :sub-title="$route.params.targetTagName">
  标签名称
  <a-input placeholder="标签名称" v-model:value="newTagName"></a-input>
  标签颜色
  <form-color-selector @onSelect="(color)=>{newTagColor = color}" v-model:color="newTagColor"></form-color-selector>
  标签描述
  <a-textarea v-model:value="newTagDescription"></a-textarea>
  <div class="row-display">
    <a-button type="primary" class="inline-button" @click="modifyTag()">修改标签</a-button>
    <a-button class="inline-button" @click="$router.go(-1)">取消</a-button>
  </div>
</header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 5px;
}
.inline-button {
  margin-right: 5px;
}
</style>