const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
      less: {
        lessOptions: {
          modifyVars: {
            'border-radius-base': '5px',
          },
          javascriptEnabled: true
        }
      }
    }
  },
  lintOnSave: false
})
