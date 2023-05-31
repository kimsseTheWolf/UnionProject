const globalConfig = require('./config')
const unfs = require('../lib/fs/basicFsHandler')
const path = require("path");

function returnNewCheckRespond(status, errCode){
    return {status: status, errCode: errCode}
}

// InitializeGlobalConfig will check whether there will be invalid values. If yes the system will ask users and create the folders in the local.
function CheckGlobalConfig() {
    return new Promise(async (res, rej)=> {
        // check metadata validation
        if (globalConfig.UnionProjectGlobalConfigData.metadata !== "") {
            // check folder is valid
            try {
                let content = await unfs.readTargetJSONFile(path.join(globalConfig.UnionProjectGlobalConfigData.metadata, "tags.json"))
                if (content === undefined){
                    rej(returnNewCheckRespond(false, "metadataNotFound"))
                }
                console.log("Metadata found")
            }
            catch (e) {
                console.log(e)
                rej(returnNewCheckRespond(false, "metadataNotFound"))
            }
        }
        else {
            rej(returnNewCheckRespond(false, "metadataNotFound"))
        }

        // check createMethods validation
        if (globalConfig.UnionProjectGlobalConfigData.createMethods !== "") {
            // check folder is valid
            try {
                let content = await unfs.readTargetJSONFile(path.join(globalConfig.UnionProjectGlobalConfigData.createMethods, "emptyProject.json"))
                if (content === undefined) {
                    rej(returnNewCheckRespond(false, "createMethodsNotFound"))
                }
                console.log("CreateMethods Found")
            }
            catch (e) {
                console.log(e)
                rej(returnNewCheckRespond(false, "createMethodsNotFound"))
            }
        }
        else {
            rej(returnNewCheckRespond(false, "createMethodsNotFound"))
        }

        // check success
        res(returnNewCheckRespond(true, undefined))
    })
}

module.exports = {
    CheckGlobalConfig
}