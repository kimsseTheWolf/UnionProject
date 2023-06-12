const globalConfig = require('./config')
const unfs = require('../lib/fs/basicFsHandler')
const fs = require('fs')
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
                let content = await unfs.readTargetJSONFile(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.metadata, "tags.json"))
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
                let content = await unfs.readTargetJSONFile(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.createMethods, "emptyProject.json"))
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

// Re-Initialize the metadata structure
async function InitializeConfigStructure() {
    return new Promise(async (res, rej) => {
        // create folder in the local
        try {
            fs.mkdirSync(path.join(__dirname, 'config'))
            console.log("Config Folder Re-created")
            res(true)
        } catch (e) {
            console.log("Config Folder already created")
            res(false)
        }

        // create sub-folders in the local
        try {
            fs.mkdirSync(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.metadata))
            console.log("Metadata folder created")
            res(true)
        } catch (e) {
            console.log("Metadata folder created")
            res(false)
        }
        try {
            fs.mkdirSync(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.createMethods))
            console.log("CreateMethods folder created")
            res(true)
        } catch (e) {
            console.log("CreateMethods folder created")
            res(false)
        }

        // create files
        try {
            // fs.mkdirSync(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.metadata, 'tags.json'))
            await unfs.writeTargetJSONFile(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.metadata, 'tags.json'), {})
            console.log("Metadata folder created")
            res(true)
        } catch (e) {
            console.log("Metadata folder created")
            res(false)
        }
        try {
            // fs.mkdirSync(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.createMethods))
            await unfs.writeTargetJSONFile(path.join(__dirname, globalConfig.UnionProjectGlobalConfigData.createMethods, 'emptyProject.json'), {})
            console.log("CreateMethods folder created")
            res(true)
        } catch (e) {
            console.log("CreateMethods folder created")
            res(false)
        }
    })
}

module.exports = {
    CheckGlobalConfig,
    InitializeConfigStructure,
}