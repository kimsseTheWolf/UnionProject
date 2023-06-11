<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {ref} from "vue";
import FormColorSelector from "@/components/colorSelector/formColorSelector.vue";

const selectableColors = ref([])

selectableColors.value = [
  {color: "red", tagIcon: "red.svg", displayName: "红"},
  {color: "orange", tagIcon: "orange.svg", displayName: "橙"},
  {color: "yellow", tagIcon: "yellow.svg", displayName: "黄"},
  {color: "green", tagIcon: "green.svg", displayName: "绿"},
  {color: "indigo", tagIcon: "indigo.svg", displayName: "青"},
  {color: "blue", tagIcon: "blue.svg", displayName: "蓝"},
  {color: "violet", tagIcon: "violet.svg", displayName: "紫"},
  {color: "black", tagIcon: "black.svg", displayName: "黑"},
]
</script>

<template>
<HeaderContentView title="创建新的标签" sub-title="创建新标签以分类项目">
  标签名称
  <a-input placeholder="标签名称"></a-input>
  标签颜色
  <form-color-selector></form-color-selector>
  标签描述
  <a-textarea></a-textarea>
</HeaderContentView>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>