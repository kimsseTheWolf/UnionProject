const unfs = require("../fs/basicFsHandler")
const config = require("../../config/config")
const path = require("path");
const respond = require("../respond/respondHandler")

const OVERALL_METADATA_FILE = path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, "projects.json")

async function readProjectOverallMetadata() {
    let fileContent = await unfs.readTargetJSONFile(OVERALL_METADATA_FILE)
    return respond.returnNewRespond(true, "Success", fileContent)
}

async function readProjectDetailsMetadata(projectID) {
    try {
        let overAllMetadata = await readProjectOverallMetadata()
        for (let i = 0; i < overAllMetadata.data.length; i++) {
            // iterate to find data
            if (overAllMetadata.data[i].project_id === projectID) {
                // open the location and read the details information
                let detailsData = await unfs.readTargetJSONFile(path.join(overAllMetadata.data[i].location), "metadata.json")
                return respond.returnNewRespond(true, "Success", detailsData)
            }
        }
        return respond.returnNewRespond(false, "NoIndicatedProjectFound")
    }
    catch (e) {
        console.log(e)
        return respond.returnNewRespond(false, "systemError", e)
    }
}

async function readProjectsFullData() {
    try {
        // read the overall information first
        let overallInfo = await readProjectOverallMetadata()
        let returnInfo = []
        for (let i = 0; i < overallInfo.data.length; i++) {
            let singleUnit = overallInfo.data[i]
            let j = await readProjectDetailsMetadata(overallInfo.data[i].project_id);
            if ( !j.status ) {
                continue;
            }
            singleUnit["metadata"] = j.data
            returnInfo.push(singleUnit)
        }
        return respond.returnNewRespond(true, "Success", returnInfo)
    }
    catch (e) {
        return respond.returnNewRespond(false, "SystemError", e)
    }
}

module.exports = {
    readProjectOverallMetadata,
    readProjectDetailsMetadata,
    readProjectsFullData
}