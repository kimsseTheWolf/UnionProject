const {ipcMain} = require('electron')
const unfs = require('../lib/fs/basicFsHandler')
const tagHandler = require('../lib/tag/tagHandler')
const initializer = require('../config/configHandler')
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

    ipcMain.handle('config:initializeMetadata', async (event) => {
        let result = await initializer.InitializeConfigStructure()
        console.log("Already Triggered")
        console.log(result)
        return result
    })

    // Tags
    ipcMain.handle('tags:create', async (event, tagName, tageColor, tagDescription) => {
        let result = await tagHandler.createTag(tagName, tageColor, tagDescription)
        console.log(result)
        return result
    })
}

module.exports = {
    IPCHandler,
    GlobalConfigResult: globalConfigResult
}