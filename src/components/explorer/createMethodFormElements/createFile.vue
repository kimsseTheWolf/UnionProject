<script setup>
const props = defineProps({
  fileName: String
})

defineEmits(['update:fileName'])
</script>

<template>
<div class="main-box">
  <div class="title">
    创建文件
  </div>
  <div class="description">
    在项目根目录中创建一个文件
  </div>
  <a-input placeholder="文件名" v-model:value="props.fileName" v-on:input="$emit('update:fileName', $event.target.value)"></a-input>

  <div class="row-display">
    <a-button type="primary" danger class="row-item">删除</a-button>
    <a-button class="row-item">上移</a-button>
    <a-button class="row-item">下移</a-button>
  </div>
</div>
</template>

<style scoped>
.main-box {
  display: flex;
  flex-direction: column;
  margin-top: 5px;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.1s;
  background-color: rgb(250, 250, 250);
}
.main-box:hover {
  background-color: rgba(30, 144, 255, 0.15);
}

.main-box .title {
  margin-bottom: 5px;
  font-weight: bolder;
}
.main-box .description {
  margin-bottom: 5px;
  color: gray;
  font-size: small;
}
.column-item {
  margin-top: 5px;
}
.row-display {
  display: flex;
  flex-direction: row;
  margin-top: 5px;
}
.row-item {
  margin-right: 5px;
}
</style>