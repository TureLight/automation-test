const CryptoJS = require('crypto-js')

/**
 * @method n位随机数生成
 * @param {int} n 位数
 * @return {string}
 * */
export function randomNum(n) {
  let sString = ''
  const strings = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  for (let i = 0; i < n; i++) {
    const ind = Math.floor(Math.random() * strings.length)
    sString += strings.charAt(ind)
  }
  return sString
}

/**
 * @method AES加密
 * @param {string} txt 明文字符串
 * @param {string} key 密钥
 * @return {string} 加密后的字符串
 */
export function aesEncrypt(txt, key) {
  const uTxt = CryptoJS.enc.Utf8.parse(txt)
  const uKey = CryptoJS.enc.Utf8.parse(key)
  const iv = CryptoJS.enc.Utf8.parse(CryptoJS.MD5(key).toString().substring(0, 16))
  const aesOption = {
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
  }
  const result = CryptoJS.AES.encrypt(uTxt, uKey, aesOption)
  return result.toString()
}
/**
 * @method AES解密
 * @param {array} byteArray 密文二进制流
 * @param {string} key 密钥
 * @return {string} 解密后的字符串
 */
export function aesDecrypt(byteArray, key) {
  const uTxt = CryptoJS.lib.WordArray.create(byteArray)
  const uKey = CryptoJS.enc.Utf8.parse(key)
  const iv = CryptoJS.enc.Utf8.parse(CryptoJS.MD5(key).toString().substring(0, 16))
  const aesOption = {
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
  }
  const bytes = CryptoJS.AES.decrypt({ ciphertext: uTxt }, uKey, aesOption)
  const result = CryptoJS.enc.Utf8.stringify(bytes).toString()
  return result
}
