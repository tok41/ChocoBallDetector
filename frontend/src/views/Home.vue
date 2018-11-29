<template lang="pug">
div
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
  .loading-overlay.bg-dark(v-if="detecting")
    .loading-spinner
      ring-loader.m-2(color="#C9CCD4" size=120)
      p.m-2.text-white.text-center 検出中...
  b-modal(title="検出結果" ref="modalResult" ok-only)
    p {{ countResult }} 個のチョコボールが検出されました。
    p 処理時間: {{ elapsedTime | msToSec }}



</template>

<script>
import axios from 'axios'
import { RingLoader } from '@saeris/vue-spinners'
export default {
name: 'home',
  components: {
    RingLoader
  },
  data () {
    return {
      file: '',
      imgaeSelected: false,
      imagePreview: require('@/assets/photo.png'),
      imageResult: require('@/assets/question.png'),
      countResult: 0,
      detected: false,
      detecting: false,
      elapsedTime: 0.0
    }

  },
  methods: {
    submitFile () {
      let formData = new FormData()
      formData.append('file', this.file)

      this.detecting = true
      let start = new Date().getTime()
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
          this.elapsedTime = (new Date().getTime() - start)
          this.$refs.modalResult.show()
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

      reader.onload = (e) => {
        this.imgaeSelected = true
        this.imagePreview = e.target.result
      }
      if (file) {
        this.imgaeSelected = false
        this.imageResult = require('@/assets/question.png')
        if (/\.(jpe?g|png|gif)$/i.test(file.name)) {
          reader.readAsDataURL(file)
        }
      }
    }
  },
  filters: {
    msToSec: (ms) => (ms / 1000).toString() + "[sec]"
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

.loading-overlay {
  position: absolute;
  z-index: 100;
  overflow: show;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  opacity: 0.7;
}

.loading-spinner {
  position: absolute;
  z-index: 101;
  top: 45%;
  left: 45%;
}
</style>
