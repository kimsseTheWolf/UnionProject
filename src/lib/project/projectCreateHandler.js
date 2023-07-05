const fs = require('fs')
const unfs = require('../fs/basicFsHandler')
const respond = require('../respond/respondHandler')
const path = require("path");
const uuid = require('node-uuid')
const date = require("../date/dateHandler")
const config = require("../../config/config")

const PROJECT_INDEX_FILE = path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, "/project.json")

function generateProjectMetadata(name, description, location, isArchived = false) {
    return {
        name: name,
        project_id: uuid.v4(),
        description: description,
        location: location,
        creation_date: date.getCurrentDate(),
        isArchived: isArchived
    }
}

async function createProjectFolder(name, description, targetLocation, isArchived) {
    // detect whether the target location is existed, if not then create the folder
    try {
        let testContent = fs.readdirSync(targetLocation)
    }
    catch (e) {
        // create the folder for the project
        fs.mkdirSync(targetLocation)
    }

    // add the index to the index file
    let indexFileContent = await unfs.readTargetJSONFile(PROJECT_INDEX_FILE)
    let projectMetadata = generateProjectMetadata(name, description, targetLocation, isArchived)
    indexFileContent.push(projectMetadata)
    await unfs.writeTargetJSONFile(PROJECT_INDEX_FILE, indexFileContent)

    // announce success status
    return respond.returnNewRespond(true, "success", {uuid: projectMetadata.project_id})

}

async function removeProject(projectUUID) {
    let targetProjectLocation = ""
    // get project location from the meta file
    let indexFileContent = await unfs.readTargetJSONFile(PROJECT_INDEX_FILE)
    for (let i = 0; i < indexFileContent.length; i++) {
        if (indexFileContent[i].project_id === projectUUID) {
            // record the location
            targetProjectLocation = indexFileContent[i].location
            // delete and exit the iteration
            indexFileContent.splice(i, 1)
            break
        }
    }
    // delete the folder according to the location
    try {
        fs.rmdirSync(targetProjectLocation)
        return respond.returnNewRespond(true, "success")
    }
    catch (e) {
        console.log(e)
        return respond.returnNewRespond(false, "dirNotFoundErr")
    }
}

module.exports = {
    createProjectFolder,
    removeProject
}