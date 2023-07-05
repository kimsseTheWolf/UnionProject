import * as path from "path";
import unfs from "../lib/fs/basicFsHandler"

let UnionProjectGlobalConfig = {
    language: "zh_cn",
    createMethods: "../config/createMethods",
    metadata: "../config/metadata",
    project: "../project",
    defaultMetadataLocation: path.join(__dirname, '/createMethods'),
    publicResources: "../public_resources",
    settings: "../config/settings.json"
}

export let UnionProjectGlobalConfigData = UnionProjectGlobalConfig;
