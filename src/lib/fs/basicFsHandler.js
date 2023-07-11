const fs = require('fs')
const {dialog} = require('electron')

function readTargetFile(filePath) {
    return new Promise((res, rej) => {
        try {
            let returnContent = fs.readFileSync(filePath)
            res(returnContent.toString())
        }
        catch (Exception) {
            console.log(Exception)
            rej(Exception)
        }
    })
}

function writeTargetFile(filePath, fileContent) {
    return new Promise((res, rej) => {
        try {
            fs.writeFileSync(filePath, fileContent)
            res(true)
        }
        catch (Exception) {
            console.log(Exception)
            rej(false)
        }
    })
}

function readTargetJSONFile(filePath) {
    return new Promise(async (res, rej) => {
        try {
            let fileContent = await readTargetFile(filePath)
            let JSONObjectContent = JSON.parse(fileContent.toString())
            res(JSONObjectContent)
        }
        catch (Exception) {
            console.log(Exception)
            res(undefined)
        }
    })
}

function writeTargetJSONFile(filePath, JSONObject) {
    return new Promise(async (res, rej) => {
        try {
            let fileContent = JSON.stringify(JSONObject)
            let result = await writeTargetFile(filePath, fileContent)
            if (result) {
                res(true)
            }
            res(false)
        }
        catch (Exception) {
            console.log(Exception)
            res(false)
        }
    })
}

function openFolderDialog(allowMultiSelection = false, defaultPath = "", title = "Select a folder") {
    return new Promise((res, rej) => {
        let selectedItems = dialog.showOpenDialogSync({title: title, defaultPath:defaultPath, properties: ['openDirectory']})
        res(selectedItems)
    })
}

function openFileDialog(allowMultiSelection= true, defaultPath = "", title = "Select a file") {
    return new Promise((res, rej) => {
        let selectedItems = dialog.showOpenDialogSync({title: title, defaultPath:defaultPath, properties: ['openFile']})
        res(selectedItems)
    })
}

function checkDirectoryIsEmpty(dir) {
    return new Promise((res, rej) => {
        let result = fs.readdirSync(dir)
        if (result === undefined) {
            res(true)
        }
        if (result.length <= 0) {
            res(true)
        }
        res(false)
    })
}

module.exports = {
    readTargetFile,
    writeTargetFile,
    readTargetJSONFile,
    writeTargetJSONFile,
    openFolderDialog,
    openFileDialog,
    checkDirectoryIsEmpty
}