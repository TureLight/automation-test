<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of timeline" :key="index" :timestamp="item.timestamp" placement="top">
        <el-card>
          <h4>{{ item.title }}</h4>
          <p>{{ item.content }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timeline: [
        {
          timestamp: '2021/3/26',
          title: '此处应为标题',
          content: '发生了什么事... 2021/3/26 20:46'
        },
        {
          timestamp: '2021/3/26',
          title: '此处应为标题',
          content: '发生了什么事... 2021/3/26 20:46'
        },
        {
          timestamp: '2021/3/26',
          title: '此处应为标题',
          content: '发生了什么事... 2021/3/26 20:46'
        },
        {
          timestamp: '2021/3/26',
          title: '此处应为标题',
          content: '发生了什么事... 2021/3/26 20:46'
        },
      ]
    }
  }
}
</script>
