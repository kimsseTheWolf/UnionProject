<script setup>
// eslint-disable-next-line no-undef
const props = defineProps({
  "type": String
})
</script>

<template>
  <div class="menu-button" :id="props.type">
    <slot></slot>
  </div>
</template>

<style scoped>
.menu-button {
  display: flex;
  flex-direction: row;
  align-items: center;
  border-radius: 5px;
  margin: 5px;
  padding: 5px;
  cursor: pointer;
  transition: all 0.1s;
}

#primary {
  background-color: dodgerblue;
  color: white;
}
#primary:hover {
  background-color: #1a71c9;
}

#borderless {
  background-color: rgba(0,0,0,0);
  color: black;
}
#borderless:hover {
  background-color: rgba(30, 144, 255, 0.15);
  color: dodgerblue;
}

#minor {
  background-color: rgba(0,0,0,0.05);
  color: black;
}
#minor:hover {
  background-color: rgba(30, 144, 255, 0.15);
  color: dodgerblue;
}
</style>