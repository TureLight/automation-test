<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.file_name" placeholder="用例名称" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.module_name" placeholder="模块名称" clearable style="width: 200px" class="filter-item">
        <el-option v-for="item in moduleNameOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.tester_name" placeholder="负责人" clearable class="filter-item" style="width: 130px">
        <el-option v-for="item in testerNameOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.case_state" placeholder="用例状态" clearable class="filter-item" style="width: 130px">
        <el-option v-for="item in caseStateOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" style="margin-left: 8px" @click="handleFilter">
        搜索
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        新增
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
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
      <el-table-column label="用例数量" width="90px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.total }}</span>
        </template>
      </el-table-column>
      <el-table-column label="模块名称" width="90px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.module_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文件名" min-width="150px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.file_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="相对路径" min-width="150px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.file_path }}</span>
        </template>
      </el-table-column>
      <el-table-column label="作者" width="90px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.author }}</span>
        </template>
      </el-table-column>
      <el-table-column label="版本控制" width="90px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.version }}</span>
        </template>
      </el-table-column>
      <el-table-column label="状态" class-name="status-col" width="90px">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter">
            {{ row.status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="230px" class-name="small-padding fixed-width">
        <template slot-scope="{row,$index}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            编辑
          </el-button>
          <el-button v-if="row.status!=='done'" size="mini" type="success" @click="handleModifyStatus(row,'done')">
            已完成
          </el-button>
          <el-button v-if="row.status!=='coding'" size="mini" @click="handleModifyStatus(row,'coding')">
            编写中
          </el-button>
          <el-button v-if="row.status!=='deleted'" size="mini" type="danger" @click="handleDelete(row,$index)">
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
        <el-form-item label="用例数量" prop="total">
          <el-input v-model="temp.total" />
        </el-form-item>
        <el-form-item label="模块名称" prop="module_name">
          <el-input v-model="temp.module_name" />
        </el-form-item>
        <el-form-item label="文件名" prop="file_name">
          <el-input v-model="temp.file_name" />
        </el-form-item>
        <el-form-item label="相对路径" prop="file_path">
          <el-input v-model="temp.file_path" />
        </el-form-item>
        <el-form-item label="作者" prop="author">
          <el-select v-model="temp.author" class="filter-item" placeholder="请选择作者">
            <el-option v-for="item in testerNameOptions" :key="item" :label="item" :value="item" />
          </el-select>
        </el-form-item>
        <el-form-item label="版本控制" prop="version">
          <el-input v-model="temp.version" />
        </el-form-item>
        <el-form-item label="状态">
          <el-select v-model="temp.status" class="filter-item" placeholder="请选择状态">
            <el-option v-for="item in statusOptions" :key="item" :label="item" :value="item" />
          </el-select>
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
import { fetchList, createCaseInfo, updateCaseInfo, updateCaseStatus, deleteCase } from '@/api/test_management/case_management'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

let moment = require("moment") // 引入

export default {
  name: 'ComplexTable',
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        done: 'success',
        coding: 'info',
        deleted: 'danger'
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
        module_name: null,
        file_name: null,
        tester_name: null,
        case_state: null,
        sort: '+id'
      },
      moduleNameOptions: ['宏观概览', '宏观框架', '指标中心'],
      testerNameOptions: ['谭文景', '常欣怡', '周春花', '李伦鑫', '张信'],
      caseStateOptions: ['已完成', '编写中'],
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['done', 'coding'],
      showReviewer: false,
      temp: {
        id: undefined,
        module_name: 1,
        file_name: '',
        update_time: new Date(),
        // update_time: null,
        file_path: '',
        author: '',
        version: '',
        'total': null,
        status: 'done'
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
        module_name: [{ required: true, message: '模块名称是必填项', trigger: 'blur' }],
        update_time: [{ required: true, message: '更新时间是必填项', trigger: 'blur' }],
        file_name: [{ required: true, message: '文件名是必填项', trigger: 'blur' }],
        file_path: [{ required: true, message: '文件路径是必填项', trigger: 'blur' }],
        author: [{ required: true, message: '作者是必填项', trigger: 'blur' }],
        status: [{ required: true, message: '状态是必填项', trigger: 'change' }]
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
    handleModifyStatus(row, status) {
      const updateForm = { 'id': row.id, 'status': status }
      updateCaseStatus(updateForm).then(response => {
        this.$message({
          message: response.message,
          type: 'success'
        })
        row.status = status
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
        module_name: '',
        file_name: '',
        update_time: new Date(),
        // update_time: null,
        file_path: '',
        author: '',
        'total': null,
        version: '',
        status: 'done'
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = this.last_index + 1
          this.temp.update_time = moment(this.temp.update_time).format('YYYY-MM-DD HH:mm')
          createCaseInfo(this.temp).then(response => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: '操作成功',
              message: response.message,
              type: 'success',
              duration: 2000
            })
            // this.getList()
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
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          // tempData.update_time = +new Date(tempData.update_time) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          tempData.update_time = moment(tempData.update_time).format('YYYY-MM-DD HH:mm')
          updateCaseInfo(tempData).then(response => {
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
          // this.getList()
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
        deleteCase(del_id).then(response => {
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
