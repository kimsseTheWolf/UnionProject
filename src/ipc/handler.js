const fsIPC = require('./fs')

function handleIPCHandler() {
    fsIPC.ProvideFsIPC()
}

module.exports = {
    handleIPCHandler
}