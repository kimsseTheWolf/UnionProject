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

async function generateScript(name, description, tags, start_date, end_date, store_location, templateID, enableGitRepo) {
    let scriptContent = {
        version: "v1",
        project_name: name,
        project_description: description,
        tags: tags,
        store_location: store_location,
        start_date: start_date,
        end_date: end_date,
        use_auto_config_git: enableGitRepo,
        script: []
    }

    // read the target script
    console.log("Generating scripts from template location or ID: ", templateID)
    let templateContent = await readScript(templateID)
    scriptContent.script = templateContent.data.createScript

    // write the script into the temp folder and return the location
    await unfs.writeTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.tempFolder, "tempCreateScript.json"), scriptContent)
    return path.join(__dirname, config.UnionProjectGlobalConfigData.tempFolder, "tempCreateScript.json")
}

module.exports = {
    importScript,
    deleteScript,
    saveScript,
    getScriptsList,
    readScript,
    generateScript
}