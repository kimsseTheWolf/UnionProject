<script setup>
import MenuButton from "@/components/buttons/MenuButton.vue";

// eslint-disable-next-line no-undef
const props = defineProps({
  "url": String,
  "icon": String
})
</script>

<template>
  <router-link :to="props.url">
    <MenuButton type="borderless">
      <img :src="icon" v-if="icon.length !== 0" width="16px">
      <div>
        <slot></slot>
      </div>
    </MenuButton>
  </router-link>
</template>

<style scoped>

</style>