const unfs = require('../fs/basicFsHandler')
const path = require("path");
const resp = require("../respond/respondHandler")

const settingsFilePath = path.join(__dirname, "/config/settings.json")

async function compareInputSettingContent(componentName, fullComponentContent) {
    // get the source file from the local
    let settingSourceContent = await unfs.readTargetJSONFile(path.join(__dirname, "/config/settings.json"))
    // compare the keys
    let sourceFileKeys = Object.keys(settingSourceContent[componentName])
    let incomeFileKeys = Object.keys(fullComponentContent)
    return sourceFileKeys === incomeFileKeys;

}

async function getSettingsFileComponent(componentName) {
    let settingSchema = await unfs.readTargetJSONFile(path.join(__dirname, "/config/settings.json"))
    return settingSchema[componentName]
}

async function writeSettingsFileContent(componentName, fullComponentContent) {
    // check whether the input is safe to write in
    if (await compareInputSettingContent(componentName, fullComponentContent)) {
        // read the file and get the content first
        let content = await unfs.readTargetJSONFile(settingsFilePath)
        // modify
        content[componentName] = fullComponentContent
        // write the file
        await unfs.writeTargetJSONFile(settingsFilePath, content)
        // return
        return resp.returnNewRespond(true, "success")
    }
    else {
        //return false
        return resp.returnNewRespond(false, "unsameStructErr")
    }
}

module.exports = {
    getSettingsFileComponent,
    writeSettingsFileContent
}