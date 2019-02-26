import '@babel/polyfill'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import PageHeader from './components/PageHeader.vue'
import PageFooter from './components/PageFooter.vue'
import VueAnalytics from 'vue-analytics'

Vue.config.productionTip = false

Vue.component('page-header', PageHeader)
Vue.component('page-footer', PageFooter)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

Vue.use(VueAnalytics, {
    id: 'UA-110494059-4', 
    router
})
