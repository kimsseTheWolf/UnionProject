<script setup>
import {ref} from "vue";

// const emits = defineEmits(['onSelect'])
const selectedColorValue = ref("")

// function sendSelectedColor() {
//   emits('onSelect', selectedColorValue.value)
//   console.log("Event Triggered")
// }
</script>

<template>
  <a-select v-model:value="selectedColorValue" @change="$emit('onSelect', selectedColorValue)">
    <a-select-option value="red">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/red.svg">
        </div>
        <div>红色</div>
      </div>
    </a-select-option>
    <a-select-option value="orange">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/orange.svg">
        </div>
        <div>橙色</div>
      </div>
    </a-select-option>
    <a-select-option value="yellow">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/yellow.svg">
        </div>
        <div>黄色</div>
      </div>
    </a-select-option>
    <a-select-option value="green">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/green.svg">
        </div>
        <div>绿色</div>
      </div>
    </a-select-option>
    <a-select-option value="indigo">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/indigo.svg">
        </div>
        <div>青色</div>
      </div>
    </a-select-option>
    <a-select-option value="blue">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/blue.svg">
        </div>
        <div>蓝色</div>
      </div>
    </a-select-option>
    <a-select-option value="violet">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/violet.svg">
        </div>
        <div>紫色</div>
      </div>
    </a-select-option>
    <a-select-option value="black">
      <div class="row-display">
        <div style="margin-left: 5px; margin-right: 5px">
          <img src="@/assets/icons/colorTags/black.svg">
        </div>
        <div>黑色</div>
      </div>
    </a-select-option>
  </a-select>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
}
</style>