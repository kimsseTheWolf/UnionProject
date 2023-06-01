const {ipcMain} = require('electron')
const unfs = require('../lib/fs/basicFsHandler')
let globalConfigResult = {}

function IPCHandler(GlobalConfigResult){
    // Apply initialization result
    globalConfigResult = GlobalConfigResult
    console.log("Initialized: ", globalConfigResult)
    // fs
    ipcMain.handle('fs:openFile', async (event, filePath) => {
        let result = await unfs.readTargetFile(filePath)
        console.log(result)
        return result
    })

    ipcMain.handle('fs:writeFile', async (event, filePath, content) => {
        let result = await unfs.writeTargetFile(filePath, content)
        console.log(result)
        return result
    })

    // Initialization and Configurations
    ipcMain.handle('config:getInitResult', (event) => {
        console.log(globalConfigResult)
        return globalConfigResult
    })
}

module.exports = {
    IPCHandler,
    GlobalConfigResult: globalConfigResult
}