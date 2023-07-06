<script setup>
defineProps({
  fileName: String,
  index: Number
})

defineEmits(['update:folderName', 'onclick:deleteOperation', 'onclick:switchUp', 'onclick:switchDown'])
</script>

<template>
<div class="main-box">
  <div class="title">
    创建文件夹
  </div>
  <div class="description">
    在项目目录中创建一个文件夹
  </div>
  <a-input placeholder="文件夹名" v-bind:value="fileName" v-on:input="$emit('update:folderName', $event.target.value)"></a-input>

  <div class="row-display" id="button-list">
    <a-button type="primary" danger class="row-item" @click="$emit('onclick:deleteOperation', $event.target.value)">删除</a-button>
    <a-button class="row-item" @click="$emit('onclick:switchUp', $event.target.value)">上移</a-button>
    <a-button class="row-item" @click="$emit('onclick:switchDown', $event.target.value)">下移</a-button>
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
.main-box #button-list {
  display: none;
}
.main-box:hover #button-list {
  display: flex;
}
</style>