<script setup>
import LinkMenuItems from "@/components/menuItems/LinkMenuItems.vue";
import EmptyOccupation from "@/views/emptyOccupation.vue";

// eslint-disable-next-line no-undef
const props = defineProps({
  "contentList": Array
})
</script>

<template>
  <!-- By using link list, you need to give the element an array with the following content: -->
  <!-- url / iconLocation(icon) / content -->
 <div class="overflow-bg">
   <LinkMenuItems v-for="i in props.contentList" :url="i.url" :icon="i.icon" v-bind:key="i">
     {{i.content}}
   </LinkMenuItems>
   <empty-occupation v-if="props.contentList.length === 0">

   </empty-occupation>
 </div>
</template>

<style scoped>
.overflow-bg {
  display: flex;
  flex-direction: column;
  margin: 5px;
  padding: 5px;
  overflow-y: auto;
  flex: auto;
}
</style>