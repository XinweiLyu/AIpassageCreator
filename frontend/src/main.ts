import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import Antd from 'ant-design-vue'
import zhCN from 'ant-design-vue/es/locale/zh_CN'
import 'ant-design-vue/dist/reset.css'
import 'dayjs/locale/zh-cn'

import '@/assets/access' // 全局权限校验

const app = createApp(App)

app.use(createPinia()) // Pinia 是 Vue 的状态管理库, 用于管理应用的状态.
app.use(router) // Vue 的官方路由库, 用于管理应用的路由.
app.use(Antd) // Ant Design 是 Vue 的组件库, 用于管理应用的组件.

// 全局配置 Ant Design 中文语言
app.provide('locale', zhCN) // 全局配置 Ant Design 中文语言.

app.mount('#app') // 挂载应用到 #app 元素.
