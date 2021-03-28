<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.task_name" disabled placeholder="任务名称" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-button v-waves class="filter-item" disabled type="primary" icon="el-icon-search" style="margin-left: 8px" @click="handleFilter">
        搜索
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        新增
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" disabled type="primary" icon="el-icon-download" @click="handleDownload">
        导出
      </el-button>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      max-height="600"
      @sort-change="sortChange"
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80px" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="更新时间" sortable width="180px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.update_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="用例数量" width="90px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.total }}</span>
        </template>
      </el-table-column>
      <el-table-column label="任务名称" min-width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.task_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="关联集合" min-width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.suite_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="执行人" width="90px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.operator }}</span>
        </template>
      </el-table-column>
      <el-table-column label="提测版本" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.version }}</span>
        </template>
      </el-table-column>
      <el-table-column label="任务状态" class-name="status-col" width="120px" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter">
            {{ row.status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="350px" class-name="small-padding fixed-width">
        <template slot-scope="{row,$index}">
          <template v-if="row.status === 'running'">
            <el-button type="primary" size="mini" disabled @click="handleTask(row)">
              {{ row.status | handleFilter }}
            </el-button>
            <el-button type="warning" size="mini" disabled @click="handleUpdate(row)">
              编辑
            </el-button>
          </template>
          <template v-if="row.status === 'idle'">
            <el-button type="primary" size="mini" @click="handleTask(row)">
              {{ row.status | handleFilter }}
            </el-button>
            <el-button type="warning" size="mini" @click="handleUpdate(row)">
              编辑
            </el-button>
          </template>
          <template v-else>
            <el-button type="primary" size="mini" @click="handleTask(row)">
              {{ row.status | handleFilter }}
            </el-button>
            <el-button type="warning" size="mini" disabled @click="handleUpdate(row)">
              编辑
            </el-button>
          </template>
          <el-button type="success" size="mini" disabled @click="handleOpen(row)">
            查看报告
          </el-button>
          <el-button v-if="row.status!=='deleted'" size="mini" type="danger" disabled @click="handleDelete(row,$index)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="90px" style="width: 400px; margin-left:50px;">
        <el-form-item label="更新时间" prop="update_time">
          <el-date-picker v-model="temp.update_time" type="datetime" placeholder="请选择时间" />
        </el-form-item>
        <el-form-item label="任务名称" prop="module_name">
          <el-input v-model="temp.task_name" />
        </el-form-item>
        <el-form-item label="关联集合" prop="file_name">
          <el-select v-model="temp.suite_name" class="filter-item" placeholder="请选择集合">
            <el-option v-for="item in suiteOptions" :key="item.id" :label="item.name" :value="item.p_key" />
          </el-select>
        </el-form-item>
        <el-form-item label="执行人" prop="author">
          <el-select v-model="temp.operator" class="filter-item" placeholder="请选择执行人">
            <el-option v-for="item in testerNameOptions" :key="item" :label="item" :value="item" />
          </el-select>
        </el-form-item>
        <el-form-item label="提测版本" prop="version">
          <el-input v-model="temp.version" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          确定
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
      <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
        <el-table-column prop="key" label="Channel" />
        <el-table-column prop="pv" label="Pv" />
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogPvVisible = false">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { fetchList, createTask, updateTask, deleteTask, operatorTask, getSuite } from '@/api/task_management/task_schedule'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
let moment = require("moment") // 引入

export default {
  name: 'TaskScheduling',
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        done: 'success',
        idle: 'danger',
        waiting: 'warning',
        running: 'primary'
      }
      return statusMap[status]
    },
    handleFilter(status) {
      const statusMap = {
        done: '加入队列',
        idle: '加入队列',
        waiting: '退出队列',
        running: '请误操作'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        task_name: null,
        sort: '+id'
      },
      moduleNameOptions: ['宏观概览', '宏观框架', '指标中心'],
      testerNameOptions: ['谭文景', '常欣怡', '周春花', '李伦鑫', '张信'],
      suiteOptions: [],
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      temp: {
        id: undefined,
        update_time: new Date(),
        task_name: '',
        suite_name: '',
        total: null,
        operator: '',
        version: '',
        status: ''
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: '编辑',
        create: '新建'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        task_name: [{ required: true, message: '任务名称是必填项', trigger: 'blur' }],
        suite_name: [{ required: true, message: '用例集合是必选项', trigger: 'blur' }],
        operator: [{ required: true, message: '操作人是必填项', trigger: 'blur' }],
        version: [{ required: true, message: '提测版本是必填项', trigger: 'blur' }]
      },
      downloadLoading: false,
      last_index: null
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        this.list = response.data.list
        this.total = response.data.total
        this.last_index = this.list[this.list.length - 1]['id']
        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleTask(row) {
      this.listLoading = true
      const new_status = (row.status === 'waiting') ? 'idle' : 'waiting'
      const updateForm = { 'id': row.id, 'status': new_status }
      operatorTask(updateForm).then(response => {
        this.$message({
          message: response.message,
          type: 'success'
        })
        row.status = new_status
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },
    resetTemp() {
      this.temp = {
        id: undefined,
        update_time: new Date(),
        task_name: '',
        suite_name: '',
        total: null,
        operator: '',
        version: '',
        status: ''
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
      getSuite().then(response => {
        this.suiteOptions = response.data
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = this.last_index + 1
          this.temp.update_time = moment(this.temp.update_time).format('YYYY-MM-DD HH:mm')
          createTask(this.temp).then(response => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: '操作成功',
              message: response.message,
              type: 'success',
              duration: 2000
            })
            this.getList()
          })
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.temp.timestamp = new Date(this.temp.timestamp)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
      getSuite().then(response => {
        this.suiteOptions = response.data
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          // tempData.update_time = +new Date(tempData.update_time) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          tempData.update_time = moment(tempData.update_time).format('YYYY-MM-DD HH:mm')
          updateTask(tempData).then(response => {
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: '操作成功',
              message: response.message,
              type: 'success',
              duration: 2000
            })
          })
          this.getList()
        }
      })
    },
    async handleDelete(row, index) {
      const del_id = row.id
      const res = await this.$confirm('此操作会永久删除该记录，是否继续？', '提示',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).catch(err => err)
      if (res === 'confirm') {
        deleteTask(del_id).then(response => {
          this.$notify({
            title: '操作成功',
            message: response.message,
            type: 'success',
            duration: 2000
          })
          this.list.splice(index, 1)
        })
      } else {
        this.$message.info('已取消删除')
      }
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['update_time', 'module_name', 'file_name', 'file_path', 'author', 'version', 'status']
        const filterVal = ['update_time', 'module_name', 'file_name', 'file_path', 'author', 'version', 'status']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'table-list'
        })
        this.downloadLoading = false
      })
    },
    formatJson(filterVal) {
      return this.list.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    },
    getSortClass: function(key) {
      const sort = this.listQuery.sort
      return sort === `+${key}` ? 'ascending' : 'descending'
    }
  }
}
</script>
