const fs = require('fs')
const {dialog} = require('electron')
const path = require("path");
const resp = require('../respond/respondHandler')

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

function copyFile(src, dst) {
    return new Promise((res)=>{
        fs.copyFileSync(src, dst)
    })
}

function deleteFile(dst) {
    return new Promise((res) => {
        fs.rmSync(dst)
    })
}

// delete everything within this dir
async function clearDir(dirDirection) {
    return new Promise(async (res) => {
        try {
            let fileList = []
            let dirList = []
            // obtain structure info
            let items = fs.readdirSync(dirDirection)
            for (let i = 0; i < items.length; i++) {
                const itemPath = path.join(dirDirection, items[i])
                const itemStat = fs.statSync(itemPath)
                if (itemStat.isDirectory()) {
                    dirList.push(items[i])
                }
                else {
                    fileList.push(items[i])
                }
            }
            // delete all files
            for (let i = 0; i < fileList; i++) {
                await deleteFile(path.join(dirDirection, fileList[i]))
            }
            // delete all folders recursively
            for (let i = 0; i < dirList; i++) {
                if (fs.readdirSync(path.join(dirDirection, dirList[i])).length !== 0) {
                    await clearDir(path.join(dirDirection, dirList[i]))
                }
                // directly delete this folder
                fs.rmdirSync(path.join(dirDirection, dirList[i]))
            }
            res(resp.returnNewRespond(true, "success"))
        }
        catch (e) {
            console.log(e)
            res(resp.returnNewRespond(false, "internalErr", e))
        }
    })
}

module.exports = {
    readTargetFile,
    writeTargetFile,
    readTargetJSONFile,
    writeTargetJSONFile,
    openFolderDialog,
    openFileDialog,
    checkDirectoryIsEmpty,
    copyFile,
    deleteFile,
    clearDir
}