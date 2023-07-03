<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {ref} from "vue"
import FormLine from "@/components/form/form-line.vue";

const security_setting_options = ref({})


function switchTriggered() {
  // write the file
  let string_data = JSON.parse(JSON.stringify(security_setting_options.value))
  console.log(string_data)
  window.settings.set("security", string_data)
}

async function getSettingData() {
  security_setting_options.value = await window.settings.get("security")
  console.log(security_setting_options.value)
}

getSettingData()
</script>

<template>
  <header-content-view title="安全" sub-title="应用程序与软件安全性设置">
    <h3>安全模式</h3>
    <div>安全模式有助于您保护您的计算机并有效阻止计算机受到恶意代码的注入与攻击。</div>
    <form-line>
      <template #title>安全模式</template>
      <template #description>安全模式启用时，角色创建脚本将无法运行脚本文件与终端指令</template>
      <template #right-item>
        <a-switch v-model:checked="security_setting_options['safe_mode']" v-on:change="switchTriggered"></a-switch>
      </template>
    </form-line>
    <form-line>
      <template #title>允许运行外部脚本</template>
      <template #description>脚本允许调用与运行外部脚本（不安全）</template>
      <template #right-item>
        <a-switch v-model:checked="security_setting_options['allow_external_script_running']" v-model:disabled="security_setting_options['safe_mode']" v-on:click="switchTriggered"></a-switch>
      </template>
    </form-line>
    <form-line>
      <template #title>允许通过终端运行</template>
      <template #description>脚本允许调用终端以执行指令</template>
      <template #right-item>
        <a-switch v-model:checked="security_setting_options['allow_terminal']" v-model:disabled="security_setting_options['safe_mode']" v-on:click="switchTriggered"></a-switch>
      </template>
    </form-line>
    <form-line>
      <template #title>运行外部脚本或终端指令前提醒我</template>
      <template #description>当创建项目时需要在终端运行或者需要运行外部脚本前以弹窗的形式提醒我以让我确认（推荐）</template>
      <template #right-item>
        <a-switch v-model:checked="security_setting_options['external_script_notification']" v-model:disabled="security_setting_options['safe_mode']" v-on:click="switchTriggered"></a-switch>
      </template>
    </form-line>
  </header-content-view>
</template>

<style scoped>

</style>