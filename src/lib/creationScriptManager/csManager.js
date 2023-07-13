const config = require("../../config/config")
const unfs = require("../fs/basicFsHandler")
const uuid = require("node-uuid")
const path = require("path");
const resp = require("../respond/respondHandler")
const fs = require("fs");

function importScript(scriptLocation) {
    return new Promise(async (res) => {
        try {
            let targetUUID = uuid.v4()
            await unfs.copyFile(scriptLocation, path.join(__dirname, config.UnionProjectGlobalConfigData.createMethods, targetUUID + ".json"))
            res(resp.returnNewRespond(true, "success", targetUUID))
        }
        catch (e) {
            console.log(e)
            res(resp.returnNewRespond(false, "Duplicate Error", e))
        }
    })
}

function saveScript(scriptID = "", content) {
    return new Promise(async (res) => {
        try {
            let sUUID = scriptID
            if (sUUID === "") {
                // regenerate a new uuid and save
                sUUID = uuid.v4()
            }
            let result = await unfs.writeTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.createMethods, sUUID + ".json"), content)
            if (!result) {
                res(resp.returnNewRespond(false, "readError"))
            }
            res(resp.returnNewRespond(true, "success", sUUID))
        }
        catch (e) {
            console.log(e)
            res(resp.returnNewRespond(false, "unhandledError", e))
        }
    })
}

function deleteScript(scriptID) {
    return new Promise(async (res) => {
        try {
            await unfs.deleteFile(path.join(__dirname, config.UnionProjectGlobalConfigData.createMethods, scriptID))
            res(resp.returnNewRespond(true, "success"))
        }
        catch (e) {
            console.log(e)
            res(resp.returnNewRespond(false, "Unhandled error", e))
        }
    })
}

function getScriptsList() {
    return new Promise(async (res) => {
        // get all script files
        let createMethodLoc = path.join(__dirname, config.UnionProjectGlobalConfigData.createMethods)
        let fileList = fs.readdirSync(createMethodLoc)
        // read all friendly name according to the names
        let prettyList = []
        for (let i = 0; i < fileList.length; i++) {
            let fileContent = await unfs.readTargetJSONFile(path.join(createMethodLoc, fileList[i]))
            prettyList.push({file_name: fileList[i], friendly_name: fileContent["friendly_name"]})
        }
        // return the result
        res([prettyList, fileList])
    })
}

function readScript(scriptID) {
    return new Promise(async (res) => {
        // read the target file
        try {
            console.log("Script ID HERE", scriptID)
            console.log(path.join(__dirname, config.UnionProjectGlobalConfigData.createMethods, scriptID))
            let fileContent = await unfs.readTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.createMethods, scriptID))
            res(resp.returnNewRespond(true, "success", fileContent))
        }
        catch (e) {
            console.log(e)
            res(resp.returnNewRespond(false, "unhandledError", e))
        }
    })
}

module.exports = {
    importScript,
    deleteScript,
    saveScript,
    getScriptsList,
    readScript
}