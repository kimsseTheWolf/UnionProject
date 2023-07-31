const {ipcMain} = require('electron')
const unfs = require('../lib/fs/basicFsHandler')
const tagHandler = require('../lib/tag/tagHandler')
const settingsHandler = require('../lib/settings/settingsHandler')
const initializer = require('../config/configHandler')
const createMethodHandler = require('../lib/project/createMethodHandler')
const csManager = require('../lib/creationScriptManager/csManager')
const compiler = require("../lib/pcsCoreCompiler/compiler")
const {all} = require("core-js/internals/document-all");
const {template} = require("@babel/core");
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
    ipcMain.handle('fs:openFileDialog', async (event, allowMultiSelection = false, defaultPath = "", title = "Choose a file") => {
        let result = await unfs.openFileDialog(allowMultiSelection, defaultPath, title)
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

    // Projects
    ipcMain.handle('project:getMethods', async (event) => {
        let result = await createMethodHandler.getFunctionList()
        console.log(result)
        return result
    })
    ipcMain.handle('project:compileScriptV1', async (event, location) => {
        let result = await compiler.compileScriptV1(location, compiler.TOP_LEVEL, false)
        console.log(result)
        return result
    })

    // Create Methods
    ipcMain.handle('cs:import', async (event, scriptLocation) => {
        let result = await csManager.importScript(scriptLocation)
        console.log(result)
        return result
    })
    ipcMain.handle('cs:save', async (event, scriptID, content) => {
        let result = await csManager.saveScript(scriptID, content)
        console.log(result)
        return result
    })
    ipcMain.handle('cs:delete', async (event, scriptID) => {
        let result = await csManager.deleteScript(scriptID)
        console.log(result)
        return result
    })
    ipcMain.handle('cs:getList', async (event) => {
        let result = await csManager.getScriptsList()
        console.log(result)
        return result
    })
    ipcMain.handle('cs:readScript', async (event, scriptID) => {
        let result = await csManager.readScript(scriptID)
        console.log(result)
        return result
    })
    ipcMain.handle('cs:generateScript', async (event, name, description, tags, start_date, end_date, store_location, templateID, enableGitRepo) => {
        let result = await csManager.generateScript(name, description, tags, start_date, end_date, store_location, templateID, enableGitRepo)
        console.log(result)
        return result
    })
}

module.exports = {
    IPCHandler,
    GlobalConfigResult: globalConfigResult
}