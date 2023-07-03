
function info(content) {
    console.log("[PCS_Compiler #INFO] " + content)
}

function warning(content) {
    console.log("\x1B[33m[PCS_Compiler #WARNING] " + content + "\x1B[0m")
}

function error(content) {
    console.log("\x1B[31m[PCS_Compiler #ERROR] " + content + "\x1B[0m")
}

module.exports = {
    info,
    warning,
    error
}