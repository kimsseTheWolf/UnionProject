const unfs = require('../fs/basicFsHandler')
const config = require('../../config/config')
const path = require("path");
const resp = require('../respond/respondHandler')
const dateHandler = require('../date/dateHandler')

let tagsContent = unfs.readTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, 'tags.json'))

// Check tag existence
function checkTagExistence(tagName) {
    let targetInfo = tagsContent[tagName]
    return targetInfo !== undefined;

}

// Create a tag
async function createTag(tagName, tageColor, tagDescription) {
    return new Promise(async (res, rej) => {
        // modify the target object
        if (checkTagExistence(tagName)) {
            rej(resp.returnNewRespond(false, 'tagNameExisted'))
        }
        tagsContent[tagName] = {
            color: tageColor,
            description: tagDescription,
            creationDate: dateHandler.getCurrentDate()
        }
        // write the object
        try {
            let result = await unfs.writeTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, 'tags.json'))
            if (!result) {
                rej(resp.returnNewRespond(false, 'writeFileErr'))
            }
            res(resp.returnNewRespond(true, 'success'))
        }
        catch (e) {
            rej(resp.returnNewRespond(false, 'writeFileErr', e))
        }
    })
}

module.exports = {
    createTag
}