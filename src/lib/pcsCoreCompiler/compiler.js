const unfs = require("../fs/basicFsHandler")
const clog = require("./logger")
const respond = require("../respond/respondHandler")
const project = require("../project/projectCreateHandler")


const TOP_LEVEL = 0

let variableHeap = []

let PROJ_NAME = ""
let PROJ_DESCRIPTION = ""
let PROJ_TAGS = []
let PROJ_LOC = ""
let PROJ_START_DATE = ""
let PROJ_END_DATE = ""

async function compileScriptV1(scriptLocation, affectLevel, skipBasicInfoChecking = false) {
    // record the level first to initialize the var library
    let currentLevel = affectLevel
    variableHeap.push({})

    // open and get the content of the file
    let fileContent = {}
    try {
        fileContent = await unfs.readTargetJSONFile(scriptLocation)
        clog.info("Target file found")

        // verify script version
        if (fileContent["version"] === "v1") {
            clog.info("Script version verified to v1! Continue the compile process.")
        }
        else {
            clog.error("Script version does not match the compiler version, and no other compiler version found. Cannot continue execution.")
            return respond.returnNewRespond(false, "versionDoesNotMatch")
        }

        // check basic information
        if (!skipBasicInfoChecking) {
            // fetch basic project information
            PROJ_NAME = fileContent["project_name"]
            PROJ_DESCRIPTION = fileContent["project_description"]
            PROJ_TAGS = fileContent["tags"]
            PROJ_LOC = fileContent["store_location"]
            PROJ_START_DATE = fileContent["start_date"]
            PROJ_END_DATE = fileContent["end_date"]
            if ([PROJ_TAGS, PROJ_DESCRIPTION, PROJ_NAME, PROJ_LOC, PROJ_START_DATE].indexOf(undefined) !== -1) {
                // One or more basic information is missing.
                clog.error("One or more basic information is missing. Declare the basic information first")
            }
            else {
                clog.info("Basic information found. Continue compiling.")
            }
        }

        // Start to create the folder for the project and add the item to the target.
        let result = await project.createProjectFolder(PROJ_NAME, PROJ_DESCRIPTION, PROJ_LOC, false)
        if (!result) {
            clog.error("Error occur while creating index and folder. Falling back and exit...")
        }
        clog.info("Success")
        return respond.returnNewRespond(true, "Success")
    }
    catch (e) {
        clog.error("Script has a syntax error that compiler cannot handle. Rolling back and quitting...")
        clog.error(e)
        return respond.returnNewRespond(false, "fileNotFoundErr")
    }
}

module.exports = {
    TOP_LEVEL,
    compileScriptV1
}