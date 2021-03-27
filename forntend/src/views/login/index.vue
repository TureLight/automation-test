<template>
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" autocomplete="on" label-position="left">

      <div class="title-container">
        <h3 class="title">自动化测试</h3>
      </div>

      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="用户名"
          name="username"
          type="text"
          tabindex="1"
          autocomplete="on"
        />
      </el-form-item>

      <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
        <el-form-item prop="password">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="loginForm.password"
            :type="passwordType"
            placeholder="密码"
            name="password"
            tabindex="2"
            autocomplete="on"
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false"
            @keyup.enter.native="handleLogin"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span>
        </el-form-item>
      </el-tooltip>

      <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">登录</el-button>
      <el-button :loading="loading" type="warning" style="width:100%;margin-top: -10px;margin-bottom:20px;margin-left: -1px" @click="registerBoxVisible=true">注册</el-button>

      <div style="position:relative">
        <div class="tips">
          <span>连续登录错误,账号会被锁定...</span>
        </div>
        <el-button class="thirdparty-button" type="primary" @click="showDialog=true">
          第三方登录
        </el-button>
      </div>
    </el-form>

    <el-dialog title="第三方登录" :visible.sync="showDialog" width="480px">
      服务端未开启端口...
      <br>
      <br>
      <br>
      <social-sign />
    </el-dialog>

    <!-- 对话框-注册用户 -->
    <div class="register-container">
      <el-dialog class="register-dialog" :visible.sync="registerBoxVisible" width="560px" @close="registeredBoxVisibleClosed">
        <el-form ref="registerForm" :model="registerForm" :rules="registerRules">
          <div class="title-container">
            <h1 class="title">注册用户</h1>
          </div>
          <el-form-item label=" 用户名 " prop="username">
            <el-col :span="8">
              <el-input v-model="registerForm.username" class="input-color" />
            </el-col>
          </el-form-item>

          <el-form-item label="输入密码" prop="password">
            <el-col :span="8">
              <el-input
                v-model="registerForm.password"
                type="password"
              />
            </el-col>
          </el-form-item>

          <el-form-item label="重复密码" prop="password2">
            <el-col :span="8">
              <el-input v-model="registerForm.password2" type="password" />
            </el-col>
          </el-form-item>
          <el-form-item label="输入昵称" prop="fullName">
            <el-col :span="8">
              <el-input v-model="registerForm.fullName" />
            </el-col>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer" style="margin-top: -30px">
          <el-button @click="registerBoxVisible=false">取 消</el-button>
          <el-button type="primary" @click.native.prevent="handleRegister">确 定</el-button>
        </div>
      </el-dialog>
    </div>

  </div>
</template>

<script>
import { aesEncrypt, randomNum } from '@/utils/cryptoAES'
import SocialSign from './components/SocialSignin'
import { register } from '@/api/user'

export default {
  name: 'Login',
  components: { SocialSign },
  data() {
    const validateUsername = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('用户名必须大于6位!'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码必须大于6位!'))
      } else {
        callback()
      }
    }
    const validatePassword2 = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码必须大于6位!'))
      } else {
        callback()
      }
    }
    const validateFullName = (rule, value, callback) => {
      if (value.length < 2) {
        callback(new Error('用户昵称必须大于2位!'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: '',
        password: ''
      },
      registerForm: {
        username: '',
        password: '',
        password2: '',
        fullName: ''
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      registerRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }],
        password2: [{ required: true, trigger: 'blur', validator: validatePassword2 }],
        fullName: [{ required: true, trigger: 'blur', validator: validateFullName }]
      },
      loading: false,
      registerBoxVisible: false,
      capsTooltip: false,
      showDialog: false,
      passwordType: 'password',
      redirect: undefined,
      otherQuery: {}
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        const query = route.query
        if (query) {
          this.redirect = query.redirect
          this.otherQuery = this.getOtherQuery(query)
        }
      },
      immediate: true
    }
  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && (key >= 'A' && key <= 'Z')
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          const KEY = randomNum(16)
          const ciphertext = aesEncrypt(this.loginForm.password, KEY)
          const loginData = {
            username: this.loginForm.username,
            password: ciphertext,
            verify_key: KEY
          }
          this.$store.dispatch('user/login', loginData)
            .then(() => {
              this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
              this.loading = false
            })
            .catch(() => {
              this.loading = false
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    handleRegister() {
      this.$refs.registerForm.validate(valid => {
        if (valid) {
          if (this.registerForm.password !== this.registerForm.password2) {
            this.$message.error('两次密码不一致,请重新输入!')
          } else {
            this.loading = true
            const KEY = randomNum(16)
            const ciphertext = aesEncrypt(this.registerForm.password, KEY)
            // console.log(ciphertext)
            const registerData = {
              username: this.registerForm.username,
              password: ciphertext,
              verify_key: KEY,
              full_name: this.registerForm.fullName
            }
            // console.log(loginData)
            register(registerData).then(response => {
              this.$message.success(response.message)
              this.loading = false
              this.registerBoxVisible = false
            })
          }
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    // 监听对话框关闭并重置
    registeredBoxVisibleClosed() {
      this.$refs.registerForm.resetFields()
    },

    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    }
    // afterQRScan() {
    //   if (e.key === 'x-admin-oauth-code') {
    //     const code = getQueryObject(e.newValue)
    //     const codeMap = {
    //       wechat: 'code',
    //       tencent: 'code'
    //     }
    //     const type = codeMap[this.auth_type]
    //     const codeName = code[type]
    //     if (codeName) {
    //       this.$store.dispatch('LoginByThirdparty', codeName).then(() => {
    //         this.$router.push({ path: this.redirect || '/' })
    //       })
    //     } else {
    //       alert('第三方登录失败')
    //     }
    //   }
    // }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray: #3e7eca;
$cursor: #289fee;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }

  .thirdparty-button {
    position: relative;
    left: 335px;
    bottom: 26px;
  }

  @media only screen and (max-width: 150px) {
    .thirdparty-button {
      display: none;
    }
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray: #2d9ccd;

.register-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .register-dialog{
    .login-form {
      position: relative;
      width: 520px;
      max-width: 100%;
      padding: 10px 10px 0;
      margin: 0 auto;
      overflow: hidden;
    }
    .title-container {
      position: relative;

      .title {
        font-size: 26px;
        color: $light_gray;
        margin: 0px auto 40px auto;
        text-align: center;
        font-weight: bold;
      }
    }
  }
}
</style>
