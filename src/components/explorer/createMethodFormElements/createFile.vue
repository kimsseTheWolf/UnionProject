<script setup>
const props = defineProps({
  filePath: String
})
</script>

<template>
<div class="main-box">
  <div class="title">
    创建文件
  </div>
  <div class="description">
    在项目根目录中创建一个文件
  </div>
</div>
</template>

<style scoped>
.main-box {
  display: flex;
  flex-direction: column;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.1s;
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
</style>