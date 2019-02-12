<template lang="pug">
b-container.about
  b-row.m-2
    b-col
      h1 What's this service?
  b-row.m-2
    b-col
      p 
        | このページはチョコボールの個数を自動で計測するサービスを提供します。
        | 以下のブログを参考にしてください。
      b-button(href="http://chocolate-ball.hatenablog.com/" variant="primary") チョコボール統計
    b-col.m-2
      b-img(src="@/assets/kyoro.png" fluid rounded="circle")
  .space-row
  b-row.m-2
    b-col
      h1 Who am I?
  b-row.m-2
    b-col
      p Name: Tok41
      b-img(src="@/assets/hippyhikky.png" fluid rounded)
      table
        tr
          td
            b-link(href="https://twitter.com/yoichi_t" fluid rounded)
              b-img.m-1(src="@/assets/twitter.png" width="36px")
          td
            b-link(href="https://github.com/tok41" fluid rounded)
              b-img.m-1(src="@/assets/github.png" width="36px")
</template>

<style scoped>
.space-row {
  margin-top: 100px;
}

</style>
