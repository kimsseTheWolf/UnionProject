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

module.exports = {
    readTargetFile,
    writeTargetFile,
}