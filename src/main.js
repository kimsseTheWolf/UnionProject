import { createApp } from 'vue'
import App from './App.vue'
import Antd from 'ant-design-vue'
import router from './router/index'
import 'ant-design-vue/dist/antd.less'

// hide electron default menu
// import electron from 'electron'
// const Menu = electron.Menu
// Menu.setApplicationMenu(null)

createApp(App).use(Antd).use(router).mount('#app')
