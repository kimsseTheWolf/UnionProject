<script setup>
// eslint-disable-next-line no-undef
const emit = defineEmits(['onclick'])

function triggerOnClick(){
  emit('onclick')
}
</script>

<template>
<div class="side-bar-button-container" @click="triggerOnClick">
  <div>
    <slot name="icon"></slot>
  </div>
  <div>
    <slot name="content"></slot>
  </div>
</div>
</template>

<style scoped>
.side-bar-button-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 7vh;
  height: fit-content;
  border-radius: 5px;
  cursor: pointer;
  color: white;
  transition: all 0.1s;
  margin: 5px;
}
.side-bar-button-container:hover {
  background-color: rgba(255,255,255,0.15);
}
</style>