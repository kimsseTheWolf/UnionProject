<script setup>

</script>

<template>
  <div class="emptyPageFormat">
    <a-empty>
      <template #description>
        这里什么都没有呢……
      </template>
    </a-empty>
  </div>
</template>

<style scoped>
.emptyPageFormat{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0;
  padding: 5px;
  flex: auto;
  height: 100%;
}
</style>