<template lang="pug">
b-container.about
  b-row.m-2
      h1 ギャラリー
  b-row.m-2
    b-col
      chocoball-result(:img_src="targetImage" :result="resultToObj(targetResult)" :showResult="showResult" :filename="targetName")
  b-row.m-2
    b-container.p-4.bg-dark(fluid)
      b-row
        b-col.p-2(v-for="(s,idx) in samples" cols=3 :key="idx")
          b-img.gallery(thumbnail fluid :src="s.image" @click="clickImage(idx)" :class="{ 'active-image': s.active }")
</template>

<script>
import ChocoballResult from '../components/ChocoballResult'
export default {
  name: 'gallery',
  data () {
    return {
      showresult: true,
      activeImageIndex: -1,
      samples: [
        { 
          filename: 'img_2822.jpg',
          image: require('@/assets/samples/IMG_2822.jpg'),
          result: require("@/assets/samples/IMG_2822.json"),
          active: false,
        },
        {
          filename: 'IMG_2283.jpg',
          image: require('@/assets/samples/IMG_2283.jpg'),
          result: require("@/assets/samples/IMG_2283.json"),
          active: false,
        },
        {
          filename: 'IMG_2303.jpg',
          image: require('@/assets/samples/IMG_2303.jpg'),
          result: require("@/assets/samples/IMG_2303.json"),
          active: false,
        },
        {
          filename: 'IMG_2548.jpg',
          image: require('@/assets/samples/IMG_2548.jpg'),
          result: require("@/assets/samples/IMG_2548.json"),
          active: false,
        },
        {
          filename: 'IMG_2716.jpg',
          image: require('@/assets/samples/IMG_2716.jpg'),
          result: require("@/assets/samples/IMG_2716.json"),
          active: false,
        },
        {
          filename: 'IMG_2729.jpg',
          image: require('@/assets/samples/IMG_2729.jpg'),
          result: require("@/assets/samples/IMG_2729.json"),
          active: false,
        },
        {
          filename: 'IMG_2731.jpg',
          image: require('@/assets/samples/IMG_2731.jpg'),
          result: require("@/assets/samples/IMG_2731.json"),
          active: false,
        },
        {
          filename: 'IMG_2810.jpg',
          image: require('@/assets/samples/IMG_2810.jpg'),
          result: require("@/assets/samples/IMG_2810.json"),
          active: false,
        },
        {
          filename: 'IMG_2889.jpg',
          image: require('@/assets/samples/IMG_2889.jpg'),
          result: require("@/assets/samples/IMG_2889.json"),
          active: false,
        },
        {
          filename: 'IMG_2907.jpg',
          image: require('@/assets/samples/IMG_2907.jpg'),
          result: require("@/assets/samples/IMG_2907.json"),
          active: false,
        },
        {
          filename: 'IMG_2909.jpg',
          image: require('@/assets/samples/IMG_2909.jpg'),
          result: require("@/assets/samples/IMG_2909.json"),
          active: false,
        },
        {
          filename: 'IMG_2915.jpg',
          image: require('@/assets/samples/IMG_2915.jpg'),
          result: require("@/assets/samples/IMG_2915.json"),
          active: false,
        },
      ]
    }

  },
  computed: {
    showResult: function() {
      return (this.activeImageIndex >= 0)
    },
    targetName: function() {
      let idx = this.activeImageIndex
      if (idx >= 0) {
        return this.samples[idx].filename
      } else {
        return null
      }
    },
    targetImage: function() {
      let idx = this.activeImageIndex
      if (idx >= 0) {
        return this.samples[idx].image
      } else {
        return null
      }
    },
    targetResult: function() {
      let idx = this.activeImageIndex
      if (idx >= 0) {
        return this.samples[idx].result
      } else {
        return null
      }
    }
  },
  methods: {
    isActiveImage: function(index) {
      return (this.activeImage === index)
    },
    resultToObj: function(result) {
      let ret = []
      if (result == null) {
        return ret
      }
      result.box.forEach((b, idx) => {
        let w = b[2] - b[0]
        let h = b[3] - b[1]
        let o = {
          id: idx,
          score: result.score[idx],
          x: b[0],
          y: b[1],
          w: w,
          h: h,
        }
        ret.push(o)
      })
      return ret
    },
    clickImage: function(idx) {
      if (this.activeImageIndex >= 0) {
        this.samples[this.activeImageIndex].active = false
        this.activeImageIndex = -1
      }
      this.activeImageIndex = idx
      this.samples[this.activeImageIndex].active = true
    }
  },
  components: {
    ChocoballResult
  },
}
</script>

<style scoped>
.gallery:hover {
  transform: scale(1.1);
  z-index: 100;
}
.active-image {
  border: solid 4px red;
}

</style>
