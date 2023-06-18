const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('fs', {
    openFile: (filePath) => ipcRenderer.invoke('fs:openFile', filePath),
    writeFile: (filePath, content) => ipcRenderer.invoke('fs:writeFile', filePath, content),
    openJSONFile: (filePath) => ipcRenderer.invoke('fs:readJSONFile', filePath),
    writeJSONFile: (filePath, content) => ipcRenderer.invoke('fs:writeJSONFile', filePath, content)
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