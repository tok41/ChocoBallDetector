<template lang="pug">
  #app
    page-header
    router-view
    footer
      b-navbar(fixed="bottom" variant="dark" type="dark")
        b-navbar-nav
          b-nav-text &copy; 2018 Tok41

        //-b-navbar-nav
          b-nav-item test
          b-nav-text hoge
          b-nav-text aho
        //-b-navbar-nav
          b-nav-item
            b-img(src="@/assets/hippyhikky.png" fluid rounded width="36px")
          b-nav-item
            b-link(href="https://twitter.com/yoichi_t" fluid rounded)
              b-img(src="@/assets/twitter.png" width="36px")
          b-nav-item
            b-link(href="https://github.com/tok41" fluid rounded)
              b-img(src="@/assets/github.png" width="36px")
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
