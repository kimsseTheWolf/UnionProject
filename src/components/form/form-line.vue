<script setup>

</script>

<template>
  <div class="form-line">
    <div class="title">
      <div>
        <slot name="title"></slot>
      </div>
      <div class="description">
        <slot name="description"></slot>
      </div>
    </div>
    <slot name="right-item"></slot>
  </div>
</template>

<style scoped>
.form-line {
  display: flex;
  flex-direction: row;
  margin-top: 5px;
  padding: 10px;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  border-radius: 5px;
  transition: all 0.1s;
}
.form-line:hover {
  background-color: rgba(30, 144, 255, 0.15);
}
.form-line .title {
  font-weight: bolder;
  display: flex;
  flex-direction: column;
}
.form-line .title .description {
  color: gray;
  font-weight: normal;
  font-size: small;
}
</style>