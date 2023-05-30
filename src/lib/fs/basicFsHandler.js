const fs = require('fs')

function readFile(filePath) {
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

module.exports = {
    readFile
}