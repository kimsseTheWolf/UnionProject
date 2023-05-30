const fs = require('fs')

function readTargetFile(filePath) {
    return new Promise((res, rej) => {
        try {
            console.log(filePath)
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
            console.log(JSONObjectContent)
            res(JSONObjectContent)
        }
        catch (Exception) {
            console.log(Exception)
            rej(undefined)
        }
    })
}

module.exports = {
    readTargetFile,
    writeTargetFile,
}