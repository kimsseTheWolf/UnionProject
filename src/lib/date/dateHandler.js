function getCurrentDate() {
    let currentTime = new Date()
    return currentTime.getFullYear() + "/" + currentTime.getMonth() + "/" + currentTime.getDate() + " " + currentTime.getHours() + ":" + currentTime.getMinutes()
}

module.exports = {
    getCurrentDate
}