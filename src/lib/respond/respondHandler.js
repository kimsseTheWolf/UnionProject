
function returnNewRespond(status, message, data=null) {
    return {
        status: status,
        msg: message,
        data: data
    }
}

module.exports = {
    returnNewRespond
}