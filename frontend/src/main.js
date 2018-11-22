import '@babel/polyfill'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import PageHeader from './components/PageHeader.vue'

Vue.config.productionTip = false

Vue.component('page-header', PageHeader)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
