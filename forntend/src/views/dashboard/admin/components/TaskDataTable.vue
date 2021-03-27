<template>
  <el-table :data="table_list" style="width: 100%;padding-top: 15px;">
    <el-table-column label="任务名称" min-width="200">
      <template slot-scope="scope">
        {{ scope.row.task_name }}
      </template>
    </el-table-column>
    <el-table-column label="提交时间" width="195" align="center">
      <template slot-scope="scope">
        {{ scope.row.submit_time }}
      </template>
    </el-table-column>
    <el-table-column label="运行时长" width="195" align="center">
      <template slot-scope="scope">
        {{ scope.row.run_time }}
      </template>
    </el-table-column>
    <el-table-column label="状态" width="100" align="center">
      <template slot-scope="{row}">
        <el-tag :type="row.status | statusFilter">
          {{ row.status }}
        </el-tag>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { taskDataList } from '@/api/dashboard/data_search'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        done: 'success',
        running: 'primary',
        waiting: 'warning'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      table_list: []
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      taskDataList().then(response => {
        this.table_list = response.data
      })
    }
  }
}
</script>
