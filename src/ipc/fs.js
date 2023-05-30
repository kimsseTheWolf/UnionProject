const {ipcMain} = require('electron')
const fs = require('../lib/fs/basicFsHandler')


async function ProvideFsIPC() {
    ipcMain.on('fs.openFile', async (event, filePath) => {
        let result = await fs.readFile(filePath)
        console.log(result)
        return result
    })
}

module.exports = {
    ProvideFsIPC
}