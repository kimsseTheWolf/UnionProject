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
            res(resp.returnNewRespond(false, 'tagNameExisted'))
        }
        tagsContent[tagName] = {
            color: tageColor,
            description: tagDescription,
            creationDate: dateHandler.getCurrentDate()
        }
        // write the object
        try {
            let result = await unfs.writeTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, 'tags.json'), tagsContent)
            if (!result) {
                res(resp.returnNewRespond(false, 'writeFileErr'))
            }
            res(resp.returnNewRespond(true, 'success'))
        }
        catch (e) {
            res(resp.returnNewRespond(false, 'writeFileErr', e))
        }
    })
}

async function openTagsMetadataFile() {
    return new Promise(async (res) => {
        // open and return the file
        try {
            let tagsData = await unfs.readTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, 'tags.json'))
            res(tagsData)
        }
        catch (e) {
            console.log(e)
            res(undefined)
        }
    })
}

module.exports = {
    createTag,
    openTagsMetadataFile
}