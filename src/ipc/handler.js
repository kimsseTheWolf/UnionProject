const {ipcMain} = require('electron')
const unfs = require('../lib/fs/basicFsHandler')

function IPCHandler(){
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
}

module.exports = {
    IPCHandler
}