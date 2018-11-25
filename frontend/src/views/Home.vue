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
      b-col.text-center.my-auto
        p 選択画像
        b-img(
          :src="imagePreview"
          rounded
          center
          fluid
          height="500px"
          )
      b-col.text-center.my-auto
        p 検出結果
        b-img(
          :src="imageResult"
          rounded
          center
          fluid
          height="500px"
          )
    b-row.my-3
      b-col.text-center.my-auto
        span(v-if="detected") {{ countResult }} 個のチョコボールが検出されました。


</template>

<script>
import axios from 'axios'
export default {
name: 'home',
  data () {
    return {
      file: '',
      imgaeSelected: false,
      imagePreview: require('@/assets/photo.png'),
      imageResult: require('@/assets/question.png'),
      countResult: 0,
      detected: false,
      detecting: false
    }

  },
  methods: {
    submitFile () {
      let formData = new FormData()
      formData.append('file', this.file)

      this.detecting = true
      axios.post('/chocoball3',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          onUploadProgress: function (progressEvent) {
            this.uploadPercentage = parseInt(Math.round((progressEvent.loaded * 100) / progressEvent.total))
          }.bind(this)
        }).then((result) => {
          console.log('SUCCESS!!')
          this.imageResult = result.data.result_image
          this.countResult = result.data.num
          console.log(result)
          this.detecting = false
          this.detected = true
        }).catch(() => {
          console.log('FAILURE!!')
          this.detecting = false
        })
    },

    resetForm () {
      this.$refs.fileupload.reset()
      this.file = ''
      this.imgaeSelected = false
      this.imagePreview = require('@/assets/photo.png')
      this.imageResult = require('@/assets/question.png')
      this.detected = false
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
