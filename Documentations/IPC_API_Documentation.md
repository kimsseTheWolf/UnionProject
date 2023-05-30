# IPC通讯文档

## 前言
为了保证开发的统一性，在这里对全局所有的IPC通讯命名以及编写方式进行规范。请按照此文档来开发新的IPC通讯功能。

## 规范
1. 所有的Handler函数（`ipcMain.Handler()`）必须写在`/src/ipc/handler.js`中。
2. 钩子函数的命名必须为`包名:函数名`，并且保证之后编写时报名和函数名的统一性。

## IPC函数一览
你可以在这里查看我们是基于哪些后台函数来实现我们的功能的，你也可以依据这份文档来开发自己的新功能。

---

### 读取文件

```javascript
// 包函数
fs.readTargetFile(filePath)

// IPC钩子函数
ipcMain.handle('fs:openFile', async (event, filePath))
```
允许读取一个文件中的所有内容，返回一个Promise。

---

### 写入文件

```javascript
// 包函数
fs.writeTargetFile(filePath, content)

// IPC钩子函数
ipcMain.handle('fs:writeFile', async (event, filePath, content))
```
允许对某个文件写入特定的内容，返回一个包含布尔类型的Promise。

---

### 读取JSON文件

```javascript
// 包函数
fs.readTargetJSONFile(filePath)
```
允许读取一个JSON文件，并且返回值为包含读取到的JSON对象的Promise。

---

### 写入JSON文件

```javascript
// 包函数
fs.writeTargetJSONFile(filePath, jsonObject)
```
允许像目标文件写入一个JSON对象，需要一个JSON对象作为参数，返回一个带有布尔类型的Promise。