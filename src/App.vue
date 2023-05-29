<template>
  <div class="app-main-view">
    <side-bar></side-bar>
    <div class="router-main-view">
      <router-view>

      </router-view>
    </div>
  </div>
</template>

<script>
import {defineComponent} from "vue";
import SideBar from "@/components/sideBar.vue";

export default defineComponent({
  components: {SideBar}
})

</script>

<style>
.app-main-view {
  display: flex;
  flex-direction: row;
  align-items: center;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
.router-main-view {
  flex: auto;
  height: 100%;
}
</style>
