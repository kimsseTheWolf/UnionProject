const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('fs', {
    openFile: (filePath) => ipcRenderer.invoke('fs:openFile', filePath),
    writeFile: (filePath, content) => ipcRenderer.invoke('fs:writeFile', filePath, content),
    openJSONFile: (filePath) => ipcRenderer.invoke('fs:readJSONFile', filePath),
    writeJSONFile: (filePath, content) => ipcRenderer.invoke('fs:writeJSONFile', filePath, content),
    openFolderDialog: (allowMultiSelection = false, defaultPath = "", title = "Choose a folder") => ipcRenderer.invoke('fs:openDirectoryDialog', allowMultiSelection, defaultPath, title),
    openFileDialog: (allowMultiSelection = false, defaultPath = "", title = "Choose a file") => ipcRenderer.invoke('fs:openFileDialog', allowMultiSelection, defaultPath, title),
    checkDirectoryIsEmpty: (dir) => ipcRenderer.invoke('fs:checkDirectoryIsEmpty', dir)
})

contextBridge.exposeInMainWorld('config', {
    checkGlobalConfigInitialization: ()=>ipcRenderer.invoke('config:getInitResult'),
    initializeConfiguration: ()=>ipcRenderer.invoke('config:initializeMetadata')
})

contextBridge.exposeInMainWorld('tags', {
    createNewTag: (tagName, tageColor, tagDescription)=>ipcRenderer.invoke('tags:create', tagName, tageColor, tagDescription),
    openMetadataFile: () => ipcRenderer.invoke('tags:openMetadataFile'),
    modifyTag: (oldTagName, newTagName, newTagColor, newTagDescription) => ipcRenderer.invoke('tags:modify', oldTagName, newTagName, newTagColor, newTagDescription),
    deleteTag: (tagName) => ipcRenderer.invoke('tags:delete', tagName)
})

contextBridge.exposeInMainWorld('settings', {
    get: (componentName) => ipcRenderer.invoke('settings:get', componentName),
    set: (componentName, fullContent) => ipcRenderer.invoke('settings:set', componentName, fullContent)
})

contextBridge.exposeInMainWorld('project', {
    getCreateMethods: () => ipcRenderer.invoke('project:getMethods'),
    compileScriptV1: (location) => ipcRenderer.invoke("project:compileScriptV1", location)
})

contextBridge.exposeInMainWorld('createMethod', {
    importScript: (scriptLocation) => ipcRenderer.invoke('cs:import', scriptLocation),
    saveScript: (scriptID="", content) => ipcRenderer.invoke('cs:save', scriptID, content),
    deleteScript: (scriptID) => ipcRenderer.invoke('cs:delete', scriptID),
    getList: () => ipcRenderer.invoke("cs:getList"),
    readScript: (scriptID) => ipcRenderer.invoke("cs:readScript", scriptID),
    generateScript: (name, description, tags, start_date, end_date, store_location, templateID, enableGitRepo) => ipcRenderer.invoke("cs:generateScript", name, description, tags, start_date, end_date, store_location, templateID, enableGitRepo)
})