const unfs = require('../fs/basicFsHandler')
const config = require('../../config/config')
const path = require("path");
const resp = require('../respond/respondHandler')
const dateHandler = require('../date/dateHandler')
const uuid = require('node-uuid')

let tagsContent = unfs.readTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, 'tags.json'))

// Check tag existence
function checkTagExistence(tagName) {
    let targetInfo = tagsContent[tagName]
    return targetInfo !== undefined;

}

// Write file
async function writeFile(content) {
    try {
        let result = await unfs.writeTargetJSONFile(path.join(__dirname, config.UnionProjectGlobalConfigData.metadata, 'tags.json'), content)
        if (!result) {
            return false
        }
        return true
    }
    catch (e) {
        return false
    }
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
            creationDate: dateHandler.getCurrentDate(),
            uuid: uuid.v1()
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

async function modifyTag(oldTagName, newTagName, newTagColor, newTagDescription) {
    return new Promise(async (res)=> {
        // check whether the new item is existed
        if (oldTagName !== newTagName && checkTagExistence(newTagName)) {
            res(resp.returnNewRespond(false, 'newNameExisted'))
        }
        // modify the tag info depends on different situation
        if (oldTagName === newTagName) {
            // modify with this method if the name does not affect
            tagsContent[oldTagName] = {
                color: newTagColor,
                description: newTagDescription,
                creationTime: dateHandler.getCurrentDate() // regenerate the generation time
                // No need to re-generate a new uuid
            }
        }
        else {
            // modify with this method if the name has already changed
            let targetUUID = ""
            for (let i = 0; i < Object.keys(tagsContent).length; i++) {
                // iterate the map, and record the uuid of the target item
                if (oldTagName === Object.keys(tagsContent)[i]) {
                    targetUUID = tagsContent[Object.keys(tagsContent)[i]].uuid
                    break
                }
            }
            // create a new tag with the metadata by keeping the same uuid
            tagsContent[newTagName] = {
                color: newTagColor,
                description: newTagDescription,
                creationTime: dateHandler.getCurrentDate(),
                uuid: targetUUID
            }
            // delete the old tag
            delete tagsContent[oldTagName]
        }
        // write file
        let wfResult = await writeFile(tagsContent)
        res(resp.returnNewRespond(wfResult, null))
    })
}

async function deleteTag(tagName) {
    return new Promise(async (res)=>{
        try {
            delete tagsContent[tagName]
            // override the file content!
            let wfResult = await writeFile(tagsContent)
            res(resp.returnNewRespond(wfResult, null))
        }
        catch (e) {
            res(resp.returnNewRespond(false, 'deleteError', e))
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
    openTagsMetadataFile,
    modifyTag,
    deleteTag
}