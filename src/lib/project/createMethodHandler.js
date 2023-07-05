const path = require("path");
const config = require("../../config/config")
const fs = require("fs")
const unfs = require("../fs/basicFsHandler")

const createMethodLoc = path.join(__dirname, config.UnionProjectGlobalConfigData.createMethods)

async function getFunctionList() {
    // get all script files
    let fileList = fs.readdirSync(createMethodLoc)
    // read all friendly name according to the names
    let prettyList = []
    for (let i = 0; i < fileList.length; i++) {
        let fileContent = await unfs.readTargetJSONFile(path.join(createMethodLoc, fileList[i]))
        prettyList.push({file_name: fileList[i], friendly_name: fileContent["friendly_name"]})
    }
    // return the result
    return [prettyList, fileList]
}


module.exports = {
    getFunctionList
}