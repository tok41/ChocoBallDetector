<template lang="pug">
  #header
    b-navbar(toggleable variant="dark" type="dark")
      b-navbar-brand(href="#")
        b-img(src="@/assets/kyoro.png" width="48px")
        span.mx-2 Chocoball Detector
      b-navbar-toggle(target="nav_collapse")
      b-collapse#nav_collapse(is-nav)
        b-navbar-nav
          b-nav-item(to="/") Home
          b-nav-item(to="/gallary") Gallary
          b-nav-item(to="/About") About
</template>

<script>
export default {
    name: 'page-header',
    data () {
	return {
	    msg: 'Welcome to Your Vue.js App',
	    value: 'default value'
	}
    }
}
</script>

<style scoped>
</style>
