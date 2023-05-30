const {ipcMain} = require('electron')
const unfs = require('../lib/fs/basicFsHandler')

function IPCHandler(){
    ipcMain.handle('fs:openFile', async (event, filePath) => {
        let result = await unfs.readTargetFile(filePath)
        console.log(result)
        return result
    })
}

module.exports = {
    IPCHandler
}