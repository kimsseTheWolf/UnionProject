<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import FormColorSelector from "@/components/colorSelector/formColorSelector.vue";
import {ref, defineEmits} from "vue";
import {message} from "ant-design-vue";
import {useRouter} from "vue-router";

const newTagName = ref("")
const newTagColor = ref("")
const newTagDescription = ref("")
const router = useRouter()

const emits = defineEmits(['onCreateTag'])

async function createNewTag() {
  // check input validation
  if (newTagName.value === "") {
    message.warn('需要标签名称')
    return
  }
  if (newTagColor.value === "") {
    newTagColor.value = 'default'
  }

  // create a new tag
  let result = await window.tags.createNewTag(newTagName.value, newTagColor.value, newTagDescription.value)
  if (result.status === false) {
    message.error('创建新标签时出现错误')
    return
  }
  message.success('新标签创建成功')
  emits('onCreateTag')
  await router.push('/tags/details/' + newTagName.value)
}
</script>

<template>
<HeaderContentView title="创建新的标签" sub-title="创建新标签以分类项目">
  标签名称
  <a-input placeholder="标签名称" v-model:value="newTagName"></a-input>
  标签颜色
  <form-color-selector @onSelect="(color)=>{newTagColor = color}"></form-color-selector>
  标签描述
  <a-textarea v-model:value="newTagDescription"></a-textarea>
  <div class="row-display">
    <a-button type="primary" class="inline-button" @click="createNewTag">创建标签</a-button>
    <a-button class="inline-button" @click="$router.go(-1)">取消</a-button>
  </div>
</HeaderContentView>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 5px;
}
.inline-button {
  margin-right: 5px;
}
</style>