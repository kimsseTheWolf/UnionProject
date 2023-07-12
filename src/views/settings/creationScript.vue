<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import FormLine from "@/components/form/form-line.vue";
import {SyncOutlined, DeleteOutlined, EditOutlined} from "@ant-design/icons-vue";
import {ref} from "vue";

const createMethodsList = ref([])

async function getMethods() {
  // apply the list
  createMethodsList.value = await window.createMethod.getList()
  console.log(createMethodsList.value)
}

getMethods()
</script>

<template>
  <header-content-view title="项目模板" sub-title="管理与编辑项目模板">
    <h3>管理所有模板</h3>
    <div>在此处查看与管理所有的模板</div>
    <form-line>
      <template #title>导入新的模板</template>
      <template #description>从本地导入一个已经存在的模板</template>
      <template #right-item>
        <a-button type="primary">导入</a-button>
      </template>
    </form-line>
    <form-line>
      <template #title>重新扫描</template>
      <template #description>重新扫描模板存放目录</template>
      <template #right-item>
        <a-button type="primary" @click="getMethods()">
          <sync-outlined></sync-outlined>
          重新扫描
        </a-button>
      </template>
    </form-line>
    <a-collapse style="margin: 5px">
      <a-collapse-panel key="1" header="所有项目">
        <div v-for="i in createMethodsList[0]">
          <form-line>
            <template #title>{{i.friendly_name}}</template>
            <template #description>{{i.file_name}}</template>
            <template #right-item>
              <div class="row-display">
                <a-button type="primary" danger class="row-item" :disabled="i.file_name === 'emptyProject.json'">
                  <delete-outlined/>
                </a-button>
                <a-button class="row-item" :disabled="i.file_name === 'emptyProject.json'">
                  <edit-outlined/>
                </a-button>
              </div>
            </template>
          </form-line>
        </div>
      </a-collapse-panel>
    </a-collapse>
    <a-divider></a-divider>
    <h3>自定义项目模板</h3>
    <div>您可以创建自己的项目模板，在以后创建项目时可以直接选择。</div>
    <form-line>
      <template #title>创建一个新的自定义项目模板</template>
      <template #description>在项目模板中打开一个模板项目以编辑自定义模板</template>
      <template #right-item>
        <router-link to="/explorer/createScriptEditor/newDocument">
          <a-button type="primary">打开模板编辑器</a-button>
        </router-link>
      </template>
    </form-line>
  </header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
  margin-top: 5px;
}
.row-item {
  margin-right: 5px;
}
</style>