const {ipcMain} = require('electron')
const unfs = require('../lib/fs/basicFsHandler')
const tagHandler = require('../lib/tag/tagHandler')
const settingsHandler = require('../lib/settings/settingsHandler')
const initializer = require('../config/configHandler')
const {all} = require("core-js/internals/document-all");
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

    ipcMain.handle('fs:readJSONFile', async (event, filePath) => {
        let result = await unfs.readTargetJSONFile(filePath)
        console.log(result)
        return result
    })

    ipcMain.handle('fs:writeJSONFile', async (event, filePath, content) => {
        let result = await unfs.writeTargetJSONFile(filePath, content)
        console.log(result)
        return result
    })
    ipcMain.handle('fs:openDirectoryDialog', async (event, allowMultiSelection = false, defaultPath = "", title = "Choose a file") => {
        let result = await unfs.openFolderDialog(allowMultiSelection, defaultPath, title)
        console.log(result)
        return result
    })
    ipcMain.handle('fs:checkDirectoryIsEmpty', async (event, dir) => {
        let result = await unfs.checkDirectoryIsEmpty(dir)
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
    ipcMain.handle('tags:openMetadataFile', async (event) => {
        let tagsData = await tagHandler.openTagsMetadataFile()
        console.log(tagsData)
        return tagsData
    })
    ipcMain.handle('tags:modify', async (event, oldTagName, newTagName, newTagColor, newTagDescription) => {
        let result = await tagHandler.modifyTag(oldTagName, newTagName, newTagColor, newTagDescription)
        console.log(result)
        return result
    })
    ipcMain.handle('tags:delete', async (event, tagName)=>{
        let result = await tagHandler.deleteTag(tagName)
        console.log(result)
        return result
    })

    // Settings
    ipcMain.handle('settings:get', async (event, componentName) => {
        let result = await settingsHandler.getSettingsFileComponent(componentName)
        console.log(result)
        return result
    })
    ipcMain.handle('settings:set', async (event, componentName, fullContent) => {
        let result = await settingsHandler.writeSettingsFileContent(componentName, fullContent)
        console.log(result)
        return result
    })
}

module.exports = {
    IPCHandler,
    GlobalConfigResult: globalConfigResult
}