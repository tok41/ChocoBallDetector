<template lang="pug">
b-container.bg-gray
  b-row.m-2
    b-col.m-2
      svg.hoge.m-2(:width="drawWidth" :height="drawHeight")
        transition(name="fade")
          image(:xlink:href="img_src" :width="orgWidth*imageScale" :height="orgHeight*imageScale" :key="img_src")
        rect(
          v-for="item in result"
          v-if="orgImage != null"
          :key="img_src+item.id"
          :x="item.y*boxScale" :y="item.x*boxScale"
          :width="item.h*boxScale" :height="item.w*boxScale"
          :class="currentRect == item.id ? 'active-rect' : 'result-rect'")
        //-=:stroke="currentRect == item.id ? 'red' : 'black'" fill="none")

      table.m-2.table.table-small.table-bordered
        tr
          th filename
          td {{filename}}
        tr
          th original resolution
          td ({{ orgWidth }}, {{orgHeight }})
        tr(v-if="showResult")
          th num of chocoballs
          td {{ this.result.length - 1 /* ugh! */ }}

    b-col
      transition(name="scoretable")
        div( v-if="showResult")
          b-table(
            :items="result"
            :fields="fields"
            small
            hover
            @row-hovered="rowEvent"
        )

</template>

<script>
var floatFormatter2 = (f) => f.toFixed(2)
var floatFormatter3 = (f) => f.toFixed(3)

export default {
  name: 'chocoball-reuslt',
  data () {
    return {
      fields: [
        {key: 'score', sortable:true, formatter: floatFormatter3 },
        {key: 'y', sortable:true,  label: 'X', formatter: floatFormatter2 },
        {key: 'x', sortable:true, label: 'Y', formatter: floatFormatter2 },
        {key: 'h', sortable:true, label: 'Width', formatter: floatFormatter2 },
        {key: 'w', sortable:true, label: 'Height', formatter: floatFormatter2 },
      ],
      orgImage: null,
      currentRect: -1,
      orgWidth: 1.0,
      orgHeight: 1.0,
      drawWidth: 394.0,
      maxImgRes: 500, // size of MAX_WIDTH in chocoball_counter.py
      drawHeight:394.0,
    }
  },
  computed: {
    imageScale: function() {
      if (this.orgWidth > this.orgHeight) {
        return this.drawWidth / this.orgWidth
      } else {
        return this.drawHeight / this.orgHeight
      }
    },
    boxScale: function() {
      if (this.orgWidth > this.maxImgRes) {
        if (this.orgWidth > this.orgHeight) {
          return this.drawWidth / this.maxImgRes
        } else {
          return this.maxImgRes / this.orgHeight
        }
      } else {
        return this.imageScale
      }
    },
  },
  methods: {
    rowEvent: function(item) {
      this.currentRect = item.id
    },
    showResultRect: function() {
      let readImage = this.orgImage != null
      return this.showResult && readImage
    },
    readImage: function() {
      const image = new Image()
      image.onload = () => {
        this.orgImage = image
        this.orgWidth = image.width
        this.orgHeight = image.height
      }
      image.src = this.img_src
    }
  },
  props: {
    filename: {
      type: String,
      default: ''
    },
    result: {
      type: Array,
      deafult: [],
    },
    showResult:{
      type: Boolean,
      default: true,
    },
    img_src: String
  },
  watch: {
    img_src: function(newVal) {
      this.readImage(newVal)
    }
  },
  mounted() {
    if (this.img_src != null) {
      const image = new Image()
      image.onload = () => {
        this.orgImage = image
        this.orgWidth = image.width
        this.orgHeight = image.height
      }
      image.src = this.img_src
    }
  },
}
</script>

<style scoped>
.hoge {
  border-radius: 0.5em;
  border: solid 1px;
}

.fade-enter-active, .fade-leave-active {
  transition: all 1s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

.scoretable-enter-active, .scoretable-leave-active {
  transition: all 0.5s;
}

.scoretable-enter, .scoretable-leave-to {
/*  transform: translateX(-100%);*/
  opacity: 0;
}

.result-rect {
  stroke: #0F8226;
  stroke-width: 3;
  fill: none;
  opacity: 0.8;
  transition: all .8s;
}
.active-rect {
  stroke: #FF0000;
  stroke-width: 6;
  fill: none;
}
</style>
