<script setup>
// eslint-disable-next-line no-undef
const props = defineProps({
  title: String,
  subTitle: String
})
</script>

<template>
  <div class="box">
    <a-page-header :title="props.title" :sub-title="props.subTitle"></a-page-header>
    <div class="content-box">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.box {
  display: flex;
  flex-direction: column;
  margin: 10px;
  padding: 5px;
  width: 100%;
  height: 100%;
}
.content-box {
  display: flex;
  flex-direction: column;
  padding: 0 24px 24px;
  overflow-y: scroll;
}
</style>