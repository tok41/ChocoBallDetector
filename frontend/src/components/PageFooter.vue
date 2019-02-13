<template lang="pug">
  div
    .spacer
    .footer.fixed-bottom.bg-dark.align-middle
        p.m-3.text-muted
          | &copy; 2018 Tok41, powerd by ABEJA Platform
          b-link(href="https://abejainc.com/platform/" target="_blank")
            b-img.abeja-logo.mx-2(src="@/assets/abejaplatform_y_posi.png" width="128px" style="background-color:#ffffff" rounded=true)
</template>

<script>
</script>

<style scoped>
.spacer {
  margin-top: 60px;
}

.footer {
  bottom: 0;
  height: 60px;
  width: 100%;
};
</style>
