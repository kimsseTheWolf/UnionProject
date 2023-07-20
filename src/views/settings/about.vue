<script setup>
import FormLine from "@/components/form/form-line.vue";
import {BuildOutlined, CodeOutlined, FileTextOutlined, ExclamationOutlined, GithubFilled} from "@ant-design/icons-vue"
import MenuButton from "@/components/buttons/MenuButton.vue";
</script>

<template>
  <div class="main-box">
    <img src="@/assets/unpjLogo.png" width="100" alt=""/>
    <h2>Union Project 2</h2>
    <a-tag color="blue" style="margin-bottom: 5px">预览版 v2.0.0-pre1</a-tag>
    <div>Union Project 是一款免费，开源，强大的本地项目与文件管理器。我致力于将强大的工具带给所有人。</div>
    <div class="button-panel">
      <menu-button type="primary" style="width: 50vh">
        <template #icon>
          <BuildOutlined/>
        </template>
        <template #content>
          检查更新并下载最新版本
        </template>
      </menu-button>
      <menu-button type="primary">
        <template #icon>
          <ExclamationOutlined/>
        </template>
        <template #content>
          遇到问题了？提交一个Issue吧！
        </template>
      </menu-button>
      <menu-button type="minor">
        <template #icon>
          <CodeOutlined/>
        </template>
        <template #content>
          查看源代码
        </template>
      </menu-button>
      <menu-button type="minor">
        <template #icon>
          <FileTextOutlined/>
        </template>
        <template #content>
          查看使用到的开源代码与项目
        </template>
      </menu-button>
      <menu-button type="minor">
        <template #icon>
          <GithubFilled/>
        </template>
        <template #content>
          前往傻狼的GitHub主页
        </template>
      </menu-button>
    </div>
  </div>
</template>

<style scoped>
.main-box{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex: auto;
}
.row-display{
  display: flex;
  flex-direction: row;
}
.button-panel {
  margin-top: 10px;
  margin-left: 20px;
  margin-right: 20px;
}
</style>