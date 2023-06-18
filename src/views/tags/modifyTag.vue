<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import FormColorSelector from "@/components/colorSelector/formColorSelector.vue";

import {ref} from "vue";

const newTagColor = ref("")
const newTagDescription = ref("")
</script>

<template>
<header-content-view title="修改标签" :sub-title="$route.params.targetTagName">
  标签名称
  <a-input placeholder="标签名称" v-model:value="$route.params.targetTagName"></a-input>
  标签颜色
  <form-color-selector @onSelect="(color)=>{newTagColor = color}"></form-color-selector>
  标签描述
  <a-textarea v-model:value="newTagDescription"></a-textarea>
  <div class="row-display">
    <a-button type="primary" class="inline-button">修改标签</a-button>
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