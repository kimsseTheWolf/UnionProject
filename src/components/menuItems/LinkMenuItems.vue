<script setup>
import MenuButton from "@/components/buttons/MenuButton.vue";
import Red from "../../../public/assets/icons/colorTags/red.vue";
import Orange from "../../../public/assets/icons/colorTags/orange.vue";
import Yellow from "../../../public/assets/icons/colorTags/yellow.vue";
import Green from "../../../public/assets/icons/colorTags/green.vue";
import Indigo from "../../../public/assets/icons/colorTags/indigo.vue";
import Blue from "../../../public/assets/icons/colorTags/blue.vue";
import Violet from "../../../public/assets/icons/colorTags/violet.vue";
import Black from "../../../public/assets/icons/colorTags/black.vue";

// eslint-disable-next-line no-undef
const props = defineProps({
  "url": String,
  "icon": String
})
</script>

<template>
  <router-link :to="props.url">
    <MenuButton type="borderless">
      <div style="margin-right: 5px">
        <Red v-if="icon === 'red'"></Red>
        <Orange v-if="icon === 'orange'"></Orange>
        <Yellow v-if="icon === 'yellow'"></Yellow>
        <Green v-if="icon === 'green'"></Green>
        <Indigo v-if="icon === 'indigo'"></Indigo>
        <Blue v-if="icon === 'blue'"></Blue>
        <Violet v-if="icon === 'violet'"></Violet>
        <Black v-if="icon === 'black'"></Black>
      </div>
      <div>
        <slot></slot>
      </div>
    </MenuButton>
  </router-link>
</template>

<style scoped>

</style>