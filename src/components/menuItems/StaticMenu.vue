<script setup>

</script>

<template>
  <div class="container">
    <slot name="content"></slot>
  </div>
</template>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
  flex: auto;
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>