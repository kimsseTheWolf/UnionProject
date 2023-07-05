const path = require("path")

let UnionProjectGlobalConfig = {
    language: "zh_cn",
    createMethods: "../config/createMethods",
    metadata: "../config/metadata",
    project: "../project",
    defaultMetadataLocation: path.join(__dirname, '/createMethods'),
    publicResources: "../public_resources",
    settings: "../config/settings.json"
}

module.exports = {
    UnionProjectGlobalConfigData: UnionProjectGlobalConfig
}
