<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.suite_name" placeholder="计划名称" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.tester" placeholder="负责人" clearable class="filter-item" style="width: 130px">
        <el-option v-for="item in testerNameOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" style="margin-left: 8px" @click="handleFilter">
        搜索
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        新增
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" disabled icon="el-icon-download" @click="handleDownload">
        导出
      </el-button>
    </div>
    <el-row>
      <el-col :span="15">
        <div class="left-container">
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
            <el-table-column label="更新时间" sortable width="160px" align="center">
              <template slot-scope="{row}">
                <span>{{ row.update_time }}</span>
              </template>
            </el-table-column>
            <el-table-column label="用例数量" width="90px" align="center">
              <template slot-scope="{row}">
                <span class="link-type" @click="handleUpdate(row)">{{ row.total }}</span>
              </template>
            </el-table-column>
            <el-table-column label="计划名称" min-width="120px">
              <template slot-scope="{row}">
                <span class="link-type" @click="handleUpdate(row)">{{ row.suite_name }}</span>
              </template>
            </el-table-column>
            <el-table-column label="编制人" width="90px" align="center">
              <template slot-scope="{row}">
                <span>{{ row.tester }}</span>
              </template>
            </el-table-column>
            <el-table-column label="提测版本" width="90px" align="center">
              <template slot-scope="{row}">
                <span>{{ row.version }}</span>
              </template>
            </el-table-column>
            <el-table-column label="操作" align="center" width="300px" class-name="small-padding fixed-width">
              <template slot-scope="{row,$index}">
                <el-button type="primary" size="mini" @click="handleUpdate(row)">
                  修改
                </el-button>
                <el-button type="primary" size="mini" @click="handleInsert(row)">
                  编制
                </el-button>
                <el-button type="success" size="mini" @click="handleDetails(row)">
                  查看
                </el-button>
                <el-button size="mini" type="danger" @click="handleDelete(row,$index)">
                  删除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
      </el-col>
      <el-col :span="1">
        <div class="split_div">
          <div class="line_div">
          </div>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="right-container">
          <el-table
            :key="tableKey"
            v-loading="listLoading"
            :data="suite_list"
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
            <el-table-column label="用例名称" min-width="150px">
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
          </el-table>
        </div>
      </el-col>
    </el-row>
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="90px" style="width: 400px; margin-left:50px;">
        <el-form-item label="计划名称" prop="suite_name">
          <el-input v-model="temp.suite_name" />
        </el-form-item>
        <el-form-item label="编制人" prop="tester">
          <el-select v-model="temp.tester" class="filter-item" placeholder="请选择编制人">
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

    <el-dialog :visible.sync="dialogSuiteItemsVisible" title="测试集合编制">
<!--      <div class="editor-container">-->
<!--        <dnd-list :list1="beSelected" :list2="readySelect" :list1-title="i_suite_title" list2-title="用例池" />-->
<!--      </div>-->

      <el-transfer
        v-model="t_value"
        :data="t_data"
        :titles="[i_suite_title, '用例池']"
        filter-placeholder="请输入模块名称"
        :format="{noChecked: '${total}',hasChecked: '${checked}/${total}'}"
      />

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogSuiteItemsVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="handleInsertSuite()">
          确定
        </el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { getSuite, updateSuite, createSuite, deleteSuite, insertSuiteItems, getDetails, getPool, getDiffItems } from '@/api/test_management/test_project'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import DndList from '@/components/DndList'

let moment = require("moment") // 引入

export default {
  name: 'TestSuite',
  components: { Pagination, DndList },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      suite_list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        suite_name: null,
        tester: null,
        sort: '+id'
      },
      testerNameOptions: ['谭文景', '常欣怡', '周春花', '李伦鑫', '张信'],
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['done', 'running', 'waiting'],
      temp: {
        id: undefined,
        update_time: new Date(),
        suite_name: '',
        tester: '',
        version: '',
        total: null
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: '修改',
        create: '新建'
      },
      dialogSuiteItemsVisible: false,
      pvData: [],
      rules: {
        suite_name: [{ required: true, message: '用例集名称是必填项', trigger: 'blur' }],
        tester: [{ required: true, message: '编制人是必填项', trigger: 'blur' }],
        version: [{ required: true, message: '提测版本是必填项', trigger: 'blur' }]
      },
      downloadLoading: false,
      last_index: null,
      i_suite_title: null,
      m_name: null,
      i_p_key: null,
      t_data: [],
      t_value: [],
      readySelect: [],
      beSelected: []
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getSuite(this.listQuery).then(response => {
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
      updateSuite(updateForm).then(response => {
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
        update_time: new Date(),
        suite_name: '',
        tester: '',
        version: '',
        total: null
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
          createSuite(this.temp).then(response => {
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
      this.temp.p_key = row.p_key
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
          tempData.update_time = moment(tempData.update_time).format('YYYY-MM-DD HH:mm')
          updateSuite(tempData).then(response => {
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
      const p_key = row.p_key
      const res = await this.$confirm('此操作会永久删除该记录，是否继续？', '提示',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).catch(err => err)
      if (res === 'confirm') {
        deleteSuite(p_key).then(response => {
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
    // suite dialog
    handleInsert(row) {
      this.beSelected = []
      this.readySelect = []
      this.t_value = []
      this.t_data = []
      this.i_p_key = row.p_key
      this.i_suite_title = row.suite_name

      // getItems(row.p_key).then(response => {
      //   this.beSelected = response.data
      //   this.beSelected.forEach((item) => {
      //     this.t_data.push(item['p_key'])
      //   })
      //   const q_data = { 'nin_list': this.t_data }
      //   getPool(q_data).then(response => {
      //     this.readySelect = response.data
      //   })
      // })

      const q_data = { 'nin_list': [] }
      getPool(q_data).then(response => {
        response.data.forEach((item) => {
          const temp_d = {
            key: item.id,
            label: item.id + ' - ' + item.module_name + ' - ' + item.file_name + ' - ' + item.auhtor
          }
          this.t_data.push(temp_d)
        })
        getDiffItems(row.p_key).then(response => {
          this.t_value = response.data
          this.readySelect = response.data
        })
      })
      this.dialogSuiteItemsVisible = true
    },
    handleInsertSuite() {
      // 这个是拖拽方法使用的
      // const temp_suit_list = []
      // for (let i = 0; i < this.beSelected.length; i++) {
      //   temp_suit_list.push(this.beSelected[i].p_key)
      // }
      const postData = {
        p_key: this.i_p_key,
        case_keys: this.t_value
      }
      insertSuiteItems(postData).then(response => {
        this.dialogSuiteItemsVisible = false
        this.t_data = []
        this.t_value = []
        this.$notify({
          title: '操作成功',
          message: response.message,
          type: 'success',
          duration: 2000
        })
      })
    },
    handleDetails(row) {
      getDetails(row.p_key).then(response => {
        this.suite_list = response.data
      })
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
<style  scoped>
.left-container {
  background-color: #81e6f3;
  max-height: 700px;
}

.right-container {
  background-color: #81e6f3;
  max-height: 700px;
}

.split_div {
  height: 100%;
}

.line_div {
  width: 0;
  min-height: 350px;
  border-left: 5px solid #5aacd7;
  position: center;
  margin-left: 30px;
  margin-top: 50px;
}
</style>

<style scoped>
.el-transfer ::v-deep.el-transfer-panel {
  border: 1px solid #EBEEF5;
  border-radius: 4px;
  overflow: hidden;
  background: #FFF;
  display: inline-block;
  vertical-align: middle;
  width: 500px;
  min-height: 500px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  position: relative;
}
.el-transfer ::v-deep.el-checkbox .el-transfer-panel__item{
  border-bottom: 1px solid #ccc;
}
.el-transfer ::v-deep.el-transfer-panel__list.is-filterable {
  min-height: 300px;
  padding-top: 0;
}
.el-transfer ::v-deep.el-checkbox {
  color: #606266;
  font-weight: 500;
  font-size: 14px;
  cursor: pointer;
  user-select: none;
  /* margin-right: 30px; */
}
.el-transfer ::v-deep.el-transfer-panel{
  margin-left: 15px;
  width: calc(100% / 2 - 105px / 2);
}
.el-transfer ::v-deep.el-transfer-panel__filter .el-input__inner {
  height: 32px;
  font-size: 12px;
  display: inline-block;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  padding-right: 10px;
  padding-left: 30px;
}
.el-transfer ::v-deep.el-transfer-panel__filter {
  text-align: center;
  margin: 5px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  display: block;
  width: 272px;
}
.el-transfer ::v-deep.el-transfer-panel__body {
  min-height: 500px;
}
.el-transfer ::v-deep.el-checkbox-group.el-transfer-panel__list {
  min-height: 500px;
}
.el-transfer ::v-deep.el-transfer__button:first-child {
 margin-left: -20px;
}
.el-transfer ::v-deep  .el-transfer__buttons{
  width: 20px;
}
.el-transfer ::v-deep  .el-button+.el-button{
  margin-left: -20px;
}
.radio{
  position: absolute;
  top: 60px;
  left: 520px;
}
/* .el-transfer ::v-deep.el-transfer-panel__filter .el-input .el-input--small .el-input--prefix{
  display: none !important;
} */
.el-transfer ::v-deep .el-transfer-panel__filter .el-input__inner {
  height: 32px;
  width: 100%;
  font-size: 12px;
  display: inline-block;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  padding-right: 10px;
  border-radius: 0px;
  padding-left: 30px;
}
</style>
