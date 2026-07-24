import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { useI18n } from './i18n'

const app = createApp(App)
const i18n = useI18n()

app.config.globalProperties.t = i18n.t
app.config.globalProperties.toggleLang = i18n.toggleLang
app.config.globalProperties.l = i18n.l
app.config.globalProperties.locale = i18n.locale

app.provide('i18n', i18n)
app.provide('t', i18n.t)
app.provide('l', i18n.l)

app.use(router)
app.mount('#app')