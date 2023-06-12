<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import FormColorSelector from "@/components/colorSelector/formColorSelector.vue";
</script>

<template>
<HeaderContentView title="创建新的标签" sub-title="创建新标签以分类项目">
  标签名称
  <a-input placeholder="标签名称"></a-input>
  标签颜色
  <form-color-selector></form-color-selector>
  标签描述
  <a-textarea></a-textarea>
  <div class="row-display">
    <a-button type="primary" class="inline-button">创建标签</a-button>
    <a-button class="inline-button">取消</a-button>
  </div>
</HeaderContentView>
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