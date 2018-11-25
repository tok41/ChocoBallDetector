<template lang="pug">
  b-container
    b-row.my-2
      b-col
        h1 チョコボール自動検出器
    b-row
      b-col
        p チョコボール検出を実行したい写真を選択してください。
    b-row.my-2
      b-col.text-center(cols="10" offset="1")
        b-form-group
          b-form-file(
            id="uploadFile"
            v-model="file"
            ref="fileupload"
            @change="handleFileSelect")
        b-button.mx-1(@click="submitFile" variant="primary" :disabled="!imgaeSelected") 検出実行
        b-button.mx-1(@click="resetForm") リセット
    b-row.my-3
      b-col.m-2.text-center.my-auto
        p 選択画像
        b-img(
          :src="imagePreview"
          rounded
          center
          fluid
          height="300px"
          )
      b-col.m-2.text-center.my-auto(cols="5")
        p 検出結果
        b-img(
          :src="imageResult"
          rounded
          center
          fluid
          height="300px"
          )


</template>

<script>
export default {
name: 'home',
  data () {
    return {
      file: '',
      imgaeSelected: false,
      imagePreview: require('@/assets/photo.png'),
      imageResult: require('@/assets/question.png'),
    }

  },
  methods: {
    submitFile () {
    },

    resetForm () {
      this.$refs.fileupload.reset()
      this.file = ''
      this.imgaeSelected = false
      this.imagePreview = require('@/assets/photo.png')
      this.imageResult = require('@/assets/question.png')
    },

    handleFileSelect (e) {
      let file = e.target.files[0]
      let reader = new FileReader()

      this.imgaeSelected = false
      reader.onload = (e) => {
        this.imgaeSelected = true
        this.imagePreview = e.target.result
      }
      if (file) {
        if (/\.(jpe?g|png|gif)$/i.test(file.name)) {
          reader.readAsDataURL(file)
        }
      }
    }
  }
}
</script>

<style scoped>
.row-space{
  margin-top: 100px;
}
.table-result {
  text-align: center;
  width: 100%;
  border: 1px gray;
}
.before-after {
  width: 45%;
}
</style>
