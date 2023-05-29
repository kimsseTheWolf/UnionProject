<script setup>
// eslint-disable-next-line no-undef
const props = defineProps({
  "contentAbsoluteCenter": Boolean
})
</script>

<template>
  <div class="split-window">
    <div class="split-menu">
      <slot name="menu"></slot>
    </div>
    <div class="split-content" :id="props.contentAbsoluteCenter">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<style scoped>
.split-window {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.split-menu {
  display: flex;
  flex-direction: column;
  flex: 1;
  background-color: rgb(250, 250, 250);
  height: 100%;
  justify-content: center;
  padding: 7px;
}
.split-content {
  display: flex;
  flex-direction: column;
  flex: 3;
  background-color: white;
  height: 100%;
  padding: 7px;
}
#true{
  justify-content: center;
  align-items: center;
}
</style>