<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'
import { barChartList } from '@/api/dashboard/data_search'

const animationDuration = 6000

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '300px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')

      this.chart.setOption({
        title: {
          text: 'BUG等级',
          left: 'center',
          top: 0,
          textStyle: {
            color: '#3e81b5'
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          top: 10,
          left: '2%',
          right: '2%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          data: ['致命', '严重', '普通', '微小', '建议'],
          axisTick: {
            alignWithLabel: true
          }
        }],
        yAxis: [{
          type: 'value',
          axisTick: {
            show: false
          }
        }],
        series: [{
          name: '成功',
          type: 'bar',
          stack: 'vistors',
          barWidth: '60%',
          data: [],
          animationDuration,
          itemStyle: {
            normal: { color:'#79e076' }
          }
        }, {
          name: '失败',
          type: 'bar',
          stack: 'vistors',
          barWidth: '60%',
          data: [],
          animationDuration,
          itemStyle: {
            normal: { color:'#ea5555' }
          }
        }, {
          name: '错误',
          type: 'bar',
          stack: 'vistors',
          barWidth: '60%',
          data: [],
          animationDuration,
          itemStyle: {
            normal: { color:'#ea8f40' }
          }
        }, {
          name: '跳过',
          type: 'bar',
          stack: 'vistors',
          barWidth: '60%',
          data: [],
          animationDuration,
          itemStyle: {
            normal: { color:'#a1a1a4' }
          }
        }]
      })
      barChartList().then(response => {
        this.chart.setOption({
          series: [
            {
              data: response.data.success_list
            },
            {
              data: response.data.failed_list
            },
            {
              data: response.data.error_list
            },
            {
              data: response.data.skip_list
            }
          ]
        })
      })
    }
  }
}
</script>
