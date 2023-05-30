const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('fs', {
    openFile: (filePath) => ipcRenderer.invoke('fs.openFile', filePath)
})