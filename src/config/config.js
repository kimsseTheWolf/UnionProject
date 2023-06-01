import * as path from "path";

let UnionProjectGlobalConfig = {
    language: "zh_cn",
    createMethods: "./config/createMethods",
    metadata: "./config/metadata",
    defaultMetadataLocation: path.join(__dirname, '/createMethods')
}

export let UnionProjectGlobalConfigData = UnionProjectGlobalConfig;