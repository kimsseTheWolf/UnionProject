<script setup>
import SplitContentView from "@/components/splitViews/splitContentView.vue";
import {ref, toRaw, unref} from "vue";
import MenuButton from "@/components/buttons/MenuButton.vue";
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {message} from "ant-design-vue";
import {FileAddOutlined, FolderAddOutlined, PlusCircleOutlined, SyncOutlined, FileTextOutlined, CodeOutlined, CopyOutlined, EditOutlined} from "@ant-design/icons-vue"
import textEditor from "@/components/input/textEditor.vue";
import {useRoute, useRouter} from "vue-router";
import FormLine from "@/components/form/form-line.vue";

const treeInfo = ref([
  {
    title: "项目根目录",
    key: "/root",
    type: "folder",
    children: [

    ],
    isLeaf: false
  }
])
const treeKeyList = ref(["/root"])

const selectedObject = ref(["/root"])

const displayCreateFolderDialog = ref(false)
const newFolderName = ref("")
const displayCreateFileDialog = ref(false)
const newFileName = ref("")
const displayImportFileDialog = ref(false)
const displayImportLocalFileDialog = ref(false)
const importFileName = ref("")
const importType = ref("")
const importLocation = ref("")
const importFileExtension = ref("")
const displayRenameDialog = ref(false)
const newObjectName = ref("")
const displayTextEditorDialog = ref(false)
const textEditorContent = ref("")
const textEditorTargetObject = ref("")
const displayCommandPanelDialog = ref(false)


const rightClickInfo = ref({})
const rightClickFullInfo = ref({})

const route = useRoute()
const router = useRouter()
const creationScriptName = ref("")
const createScriptDescription = ref("")
const generatedCreateSteps = ref([])
const finalListSteps = ref([])
const customSteps = ref([])
const creationScriptContent = ref({})


async function loadFileContent() {
  let fileName = route.params.scriptName
  if (fileName === "newDocument") {
    creationScriptName.value = "New Document"
  }
  else {
    // loadFileContent
    let result = await window.createMethod.readScript(fileName)
    if (result.status) {
      creationScriptContent.value = result.data
      console.log(creationScriptContent.value)
      creationScriptName.value = creationScriptContent.value["friendly_name"]
      treeInfo.value = creationScriptContent.value["tree_map"]
      generatedCreateSteps.value = creationScriptContent.value["create_script"]
    }
    else {
      message.error("无法读取目标模板：", result.data)
    }
  }
}

async function saveFileContent() {
  // check requirements
  if (creationScriptName.value === "") {
    message.warn("您需要提供模板名称")
    return
  }

  // generate the metadata
  let fileContent = {
    version: "v1",
    friendly_name: toRaw(creationScriptName.value),
    description: toRaw(createScriptDescription.value),
    properties: [],
    createScript: toRaw(finalListSteps.value),
    tree_map: toRaw(treeInfo.value)
  }

  // save the file
  let scriptID
  if (route.params.scriptName === "newDocument") {
    scriptID = ""
  }
  else {
    scriptID = route.params.scriptName.substring(0, route.params.scriptName.length - 5)
  }
  console.log(scriptID)
  console.log(fileContent)
  let result = await window.createMethod.saveScript(scriptID, fileContent)
  if (result.status === true) {
    message.success("保存成功")
    // redirect to the new UUID just in case
    await router.push("/explorer/createScriptEditor/" + result.data)
  }
  else {
    message.error("保存时出现错误：", result.data)
  }
}

loadFileContent()

let treeQueue = []
let convertTreeInfo = {}
async function appendChild(targetNode, targetKey, appendObj) {
  if (targetNode === undefined) {
    return
  }
  else {
    if (targetNode.key === targetKey) {
      // append the object to the children
      targetNode.children.push(appendObj)
      treeKeyList.value.push(appendObj.key)
      return
    }
    if (targetNode.children !== undefined) {
      for (let i = 0; i < targetNode.children.length; i++) {
        await appendChild(targetNode.children[i], targetKey, appendObj)
      }
    }
    return
  }
}

async function modifyObjectContent(targetNode, targetKey, content) {
  if (targetNode === undefined) {
    return
  }
  else {
    if (targetNode.key === targetKey) {
      // modify the content
      targetNode.content = content
      return
    }
    if (targetNode.children !== undefined) {
      for (let i = 0; i < targetNode.children.length; i++) {
        await modifyObjectContent(targetNode.children[i], targetKey, content)
      }
    }
    return
  }
}

async function iterateToFind(targetNode, targetKey) {
  if (targetNode === undefined) {
    return undefined
  }
  else {
    if (targetNode.key === targetKey) {
      // return the object info
      return targetNode
    }
    if (targetNode.children !== undefined) {
      let result
      for (let i = 0; i < targetNode.children.length; i++) {
        result = await iterateToFind(targetNode.children[i], targetKey)
        if (result !== undefined) {
          return result
        }
      }
    }
  }
}

// need first node initialization
async function iterateToGenerateDirList(targetNode) {
  if (targetNode === undefined) {
    return
  }
  else {
    // append the children to the queue
    for (let i = 0; i < targetNode.children.length; i++) {
      generatedCreateSteps.value.push(targetNode.children[i])
      await iterateToGenerateDirList(targetNode.children[i])
    }
    return
  }
}

async function deleteNode(targetNode, targetKey) {
  if (targetNode === undefined) {
    return
  }
  else {
    if (targetNode.children !== undefined) {
      for (let i = 0; i < targetNode.children.length; i++) {
        if (targetNode.children[i].key === targetKey) {
          // delete the target node
          targetNode.children.splice(i, 1)
          treeKeyList.value.splice(treeKeyList.value.indexOf(targetKey), 1)
          return
        }
        await deleteNode(targetNode.children[i], targetKey)
      }
    }
    return
  }
}

async function checkSameObj(objectKeyName) {
  return treeKeyList.value.indexOf(objectKeyName) !== -1;

}

async function appendFolder(selectedKeyName, folderName) {
  // check name
  if (folderName === "") {
    message.warn("需要文件夹名称")
    return
  }
  // check whether has the exact same object
  let result = await checkSameObj(selectedKeyName + "/" + folderName)
  // iterate the tree and find the children of the key node
  console.log(result)
  if (!result) {
    await appendChild(treeInfo.value[0], selectedKeyName, {
      title: folderName,
      key: selectedKeyName + "/" + folderName,
      type: "folder",
      children: [],
      isLeaf: false
    })
    displayCreateFolderDialog.value = false
    newFolderName.value = ""
  }
  else {
    message.warn("此名称已存在")
  }
}

async function appendFile(selectedKeyName, fileName, importLocation="not_import", content="", fileExtension="") {
  // check name
  if (fileName === "") {
    message.warn("需要文件名称")
    return
  }
  // check whether has the exact same object
  let result = await checkSameObj(selectedKeyName + "/" + fileName)
  // iterate the tree and find the children of the key node
  console.log(result)
  if (!result) {
    await appendChild(treeInfo.value[0], selectedKeyName, {
      title: fileName + fileExtension,
      key: selectedKeyName + "/" + fileName,
      type: "file",
      children: [],
      isLeaf: true,
      content: content,
      import_location: importLocation
    })
    displayCreateFileDialog.value = false
    newFileName.value = ""
    console.log(treeInfo.value)
  }
  else {
    message.warn("此名称已存在")
  }
}


async function handleTreeStructureRefactor(info) {
  console.log(info)
  // verify file existence
  let newFileKey = info.node.dataRef.key + "/" + info.dragNode.title
  console.log(newFileKey)
  let newParentKey = info.node.dataRef.key
  let fileExisted =  await checkSameObj(newFileKey)
  console.log(fileExisted)
  if (fileExisted) {
    message.warn("此目录下文件已经存在")
  }
  else {
    // move the object to the new location
    // generate the old location and the new location for the file
    let oldFileKey = info.dragNodesKeys[0]
    // find the object according to the old key
    let obj = await iterateToFind(treeInfo.value[0], oldFileKey)
    // delete the node
    await deleteNode(treeInfo.value[0], oldFileKey)
    // modify the information
    obj.key = newFileKey
    // append the new object
    await appendChild(treeInfo.value[0], newParentKey, obj)
  }
}

// rename a object
async function renameObject(targetObjectKey, targetObjectParentKey, newObjectName) {
  let newFileKey = targetObjectParentKey + "/" + newObjectName
  let newParentKey = targetObjectParentKey
  console.log(newFileKey)
  console.log(newParentKey)
  // check existence
  if (await checkSameObj(newFileKey)) {
    message.warn("此目录下文件已经存在")
  }
  else {
    // move the object to the new location
    // generate the old location and the new location for the file
    let oldFileKey = targetObjectKey
    // find the object according to the old key
    let obj = await iterateToFind(treeInfo.value[0], oldFileKey)
    console.log(obj)
    // delete the node
    await deleteNode(treeInfo.value[0], oldFileKey)
    // modify the information
    obj.key = newFileKey
    obj.title = newObjectName
    console.log(obj)
    // append the new object
    await appendChild(treeInfo.value[0], newParentKey, obj)
    // announce success
    message.success("重命名成功")
    displayRenameDialog.value = false
  }
}
async function generateDirSteps() {
  // initialize the queue in order to iterate and process
  generatedCreateSteps.value = []
  finalListSteps.value = []
  generatedCreateSteps.value.push(treeInfo.value[0])
  // iterate to process
  await iterateToGenerateDirList(generatedCreateSteps.value[0])
  console.log(generatedCreateSteps.value)
  // generate the proper steps according to the generated steps
  for (let i = 0; i < generatedCreateSteps.value.length; i++) {
    if (generatedCreateSteps.value[i].type === 'folder') {
      finalListSteps.value.push({
        method: "create",
        type: "dir",
        name: generatedCreateSteps.value[i].key
      })
    }

    if (generatedCreateSteps.value[i].type === 'file') {
      if (generatedCreateSteps.value[i].import_location !== "" && generatedCreateSteps.value[i].import_location !== "not_import") {
        // means this is an import file, using copy command
        finalListSteps.value.push({
          method: "copy",
          from: generatedCreateSteps.value[i].import_location,
          to : generatedCreateSteps.value[i].key
        })
      }
      else {
        // create the file
        finalListSteps.value.push({
          method: "create",
          type: "file",
          name: generatedCreateSteps.value[i].key
        })
      }
      // write in the content of the file if needed
      if (generatedCreateSteps.value[i].content !== "") {
        finalListSteps.value.push({
          method: "write",
          target: generatedCreateSteps.value[i].key,
          content: generatedCreateSteps.value[i].content
        })
      }
    }

  }

  console.log(finalListSteps.value)

  // TODO: Finish the list generation after the components are finished
  // TODO: Design file selection components.
}

function handleTreeRightClick(info) {
  console.log("Tree object right click: ", info)
  rightClickInfo.value = info.node
  rightClickFullInfo.value = info
  console.log(rightClickInfo.value)
  console.log(rightClickFullInfo.value)
  console.log("Right click info overrided!")
}

async function openImportFileDialog() {
  let selectedFiles = await window.fs.openFileDialog()
  importLocation.value = selectedFiles[0]
}

async function fetchTextEditor() {
  // clear the text first
  textEditorContent.value = ""
  // gather the information
  textEditorTargetObject.value = rightClickInfo.value.key
  console.log(textEditorTargetObject.value)
  // find the content
  let gatheredNodeInfo = await iterateToFind(treeInfo.value[0], textEditorTargetObject.value)
  textEditorContent.value = toRaw(gatheredNodeInfo).content
  console.log(textEditorContent.value)
  // open the dialog
  displayTextEditorDialog.value = true
}

async function saveTextEditorContent() {
  console.log("Gathered info: ", textEditorContent.value)
  // write the file into the content
  await modifyObjectContent(treeInfo.value[0], textEditorTargetObject.value, textEditorContent.value)
  displayTextEditorDialog.value = false
  console.log(treeInfo.value)
}

</script>

<template>
<split-content-view :content-absolute-center="false" menu-style="white-menu">
  <template #menu>
    <h1 style="margin-top: 20px">模板编辑器</h1>
    <a-dropdown>
      <template #overlay>
        <a-menu>
          <a-menu-item key="createFile"  @click="displayCreateFileDialog = !displayCreateFileDialog">
            <file-add-outlined />
            创建文件
          </a-menu-item>
          <a-menu-item key="createFile" @click="displayCreateFolderDialog = !displayCreateFolderDialog">
            <FolderAddOutlined/>
            创建文件夹
          </a-menu-item>
          <a-menu-item key="importFile" @click="displayImportFileDialog = !displayImportFileDialog">
            <file-text-outlined />
            创建特定文件格式的文件
          </a-menu-item>
          <a-menu-item key="importLocalFile" @click="displayImportLocalFileDialog = !displayImportLocalFileDialog">
            <file-add-outlined />
            导入本地文件
          </a-menu-item>
        </a-menu>
      </template>
      <menu-button type="primary" style="margin-top: 5px">添加……</menu-button>
    </a-dropdown>
    <div class="auto-flex-box">
      <a-dropdown :trigger="['contextmenu']">
        <a-directory-tree v-model:tree-data="treeInfo" v-model:selected-keys="selectedObject" block-node style="background: rgba(255,255,255,0) !important;" :draggable="true" @drop="handleTreeStructureRefactor" @rightClick="handleTreeRightClick"></a-directory-tree>
        <template #overlay>
          <a-menu v-if="rightClickInfo.key === '/root'">
            <a-menu-item-group>
              <template #title>没有方法可以对根目录进行操作</template>
            </a-menu-item-group>
          </a-menu>
          <a-menu v-else-if="rightClickInfo.type === 'folder'">
            <a-menu-item key="3" @click="deleteNode(treeInfo[0], rightClickInfo.key)">删除文件夹</a-menu-item>
            <a-menu-item key="4" @click="displayRenameDialog = !displayRenameDialog">重命名文件夹</a-menu-item>
          </a-menu>
          <a-menu v-else-if="rightClickInfo.type === 'file'">
            <a-menu-item key="3" @click="deleteNode(treeInfo[0], rightClickInfo.key)">删除文件</a-menu-item>
            <a-menu-item key="4" @click="displayRenameDialog = !displayRenameDialog">重命名文件</a-menu-item>
            <a-menu-divider></a-menu-divider>
            <a-menu-item key="5" @click="fetchTextEditor()" :disabled="rightClickInfo.import_location !== '' && rightClickInfo.import_location !== 'not_import'">
              编辑文件内容 <div v-if="rightClickInfo.import_location !== '' && rightClickInfo.import_location !== 'not_import'">不可编辑导入文件内容</div>
            </a-menu-item>
            <a-menu-item key="6">在模板行为列表中查看文件</a-menu-item>
          </a-menu>
        </template>
      </a-dropdown>
    </div>
  </template>
  <template #content>
    <header-content-view title="创建行为预览" sub-title="编辑并管理模板的创建行为">
      <a-input placeholder="模板名称" class="column-item" v-model:value="creationScriptName"></a-input>
      <a-alert type="info" message="在左侧创建文件或文件夹自动生成创建文件步骤。点击添加步骤添加额外步骤。" class="column-item"></a-alert>
      <div class="row-display">
        <a-dropdown>
          <a-button type="primary" class="row-inline-item">
            <plus-circle-outlined />
            添加步骤
          </a-button>
          <template #overlay>
            <a-menu>
              <a-menu-item key="script" @click="displayCommandPanelDialog = !displayCommandPanelDialog">
                <CodeOutlined/>
                添加可执行命令/脚本
              </a-menu-item>
            </a-menu>
          </template>
        </a-dropdown>
        <a-button class="row-inline-item" @click="generateDirSteps()">
          <sync-outlined />
          重新生成步骤
        </a-button>
      </div>
      <a-divider></a-divider>
      <a-collapse style="margin: 5px">
        <a-collapse-panel header="项目目录生成项目">
          <a-alert type="info" message="此部分内容通过项目结构自动生成，若要更改请通过左侧文件树更改" closable></a-alert>
          <div v-for="i in finalListSteps" :key="i">
            <form-line v-if="i.method === 'create'">
              <template #left-item>
                <PlusCircleOutlined/>
              </template>
              <template #title>创建文件：{{i.name}}</template>
              <template #right-item></template>
            </form-line>
            <form-line v-if="i.method === 'copy'">
              <template #left-item>
                <CopyOutlined/>
              </template>
              <template #title>复制文件：{{i.to}}</template>
              <template #description>从 {{i.from}} 复制文件</template>
              <template #right-item></template>
            </form-line>
            <form-line v-if="i.method === 'write'">
              <template #left-item>
                <EditOutlined/>
              </template>
              <template #title>写入目标文件：{{i.target}}</template>
              <template #description>写入内容：{{i.content}}</template>
              <template #right-item></template>
            </form-line>
          </div>
        </a-collapse-panel>
        <a-collapse-panel header="额外步骤">
          <a-alert type="info" message="用户自定义步骤将会添加在这里" closable></a-alert>
        </a-collapse-panel>
      </a-collapse>
      <a-divider></a-divider>
      <a-button type="primary" class="column-item" @click="saveFileContent()">保存模板</a-button>
    </header-content-view>
  </template>
</split-content-view>

  <a-modal title="创建文件夹" v-model:visible="displayCreateFolderDialog">
    <div class="column-display">
      <div class="column-item">输入文件夹名称</div>
      <a-input class="column-item" v-model:value="newFolderName"></a-input>
    </div>
    <template #footer>
      <a-button type="primary" class="row-item" @click="appendFolder(selectedObject[0], newFolderName)">创建文件夹</a-button>
      <a-button @click="displayCreateFolderDialog = !displayCreateFolderDialog">关闭</a-button>
    </template>
  </a-modal>

  <a-modal title="创建文件" v-model:visible="displayCreateFileDialog">
    <div class="column-display">
      <div class="column-item">输入文件名称</div>
      <a-input class="column-item" v-model:value="newFileName"></a-input>
    </div>
    <template #footer>
      <a-button type="primary" class="row-item" @click="appendFile(selectedObject[0], newFileName, 'not_import', '')">创建文件</a-button>
      <a-button @click="displayCreateFileDialog = !displayCreateFileDialog">关闭</a-button>
    </template>
  </a-modal>

  <a-modal title="创建特定文件类型的文件" v-model:visible="displayImportFileDialog">
    <div class="column-display">
      <div class="column-item">输入文件名称</div>
      <a-input class="column-item" v-model:value="importFileName"></a-input>

      <div class="column-item">选择导入类型</div>
      <a-select class="column-item" v-model:value="importLocation">
        <a-select-opt-group>
          <template #label>办公文件</template>
          <a-select-option value="{$public_folder}/xlsx" @click="importFileExtension = '.xlsx'">Excel电子表格文件</a-select-option>
          <a-select-option value="{$public_folder}/pptx" @click="importFileExtension = '.pptx'">PPT演示文稿</a-select-option>
          <a-select-option value="{$public_folder}/docx" @click="importFileExtension = '.docx'">Word文字文档</a-select-option>
        </a-select-opt-group>
      </a-select>
    </div>
    <template #footer>
      <a-button type="primary" class="row-item" @click="appendFile(selectedObject[0], importFileName, importLocation, '', importFileExtension)">导入</a-button>
      <a-button @click="displayImportFileDialog = !displayImportFileDialog">关闭</a-button>
    </template>
  </a-modal>

  <a-modal title="导入本地文件" v-model:visible="displayImportLocalFileDialog">
    <div class="column-display">
      <div class="column-item">输入文件名称</div>
      <a-input class="column-item" v-model:value="importFileName"></a-input>

      <div>导入文件地址</div>
      <div class="row-display">
        <a-input class="row-item" v-model:value="importLocation" placeholder="选择导入文件地址"></a-input>
        <a-button type="primary" class="row-item" @click="openImportFileDialog()">选择文件</a-button>
      </div>
    </div>
    <template #footer>
      <a-button type="primary" class="row-item" @click="appendFile(selectedObject[0], importFileName, importLocation, '')">导入</a-button>
      <a-button @click="displayImportLocalFileDialog = !displayImportLocalFileDialog">关闭</a-button>
    </template>
  </a-modal>

  <a-modal title="重命名" v-model:visible="displayRenameDialog">
    <div class="column-display">
      <div class="column-item">目标文件：{{rightClickInfo.title}}</div>
      <div class="column-item"><b>新名称</b></div>
      <a-input class="column-item" v-model:value="newObjectName"></a-input>
    </div>
    <template #footer>
      <a-button type="primary" class="row-item" @click="renameObject(rightClickInfo.key, rightClickInfo.parent.key, newObjectName)">重命名</a-button>
      <a-button @click="displayRenameDialog = !displayRenameDialog">关闭</a-button>
    </template>
  </a-modal>

  <a-modal title="编辑文件" v-model:visible="displayTextEditorDialog">
    <div class="column-display">
      <a-alert type="info" message="文本编辑器编辑的内容只会在可以直接编辑和写入的情况下生效。二进制文件（比如Word文本文档）的内容会被目标文件覆盖。" class="column-item"></a-alert>
      <a-textarea :rows="10" style="font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace" v-model:value="textEditorContent" class="column-item"></a-textarea>
    </div>
    <template #footer>
      <a-button type="primary" @click="saveTextEditorContent()">保存</a-button>
      <a-button @click="displayTextEditorDialog = !displayTextEditorDialog">不保存并退出</a-button>
    </template>
  </a-modal>

  <a-modal title="添加可执行命令/脚本"  v-model:visible="displayCommandPanelDialog">
    <a-alert type="warning" message="不要轻易执行来自其他人的代码。不要执行对操作系统有伤害的代码。默认情况下，Union Project禁用了脚本的执行。若要开启，请前往设置开启。"></a-alert>
    <!-- TODO: Finish component design here -->
    <template #footer>
      <a-button @click="displayCommandPanelDialog = !displayCommandPanelDialog">关闭</a-button>
      <a-button type="primary">确定</a-button>
    </template>
  </a-modal>
</template>

<style scoped>
.auto-flex-box {
  display: flex;
  flex-direction: column;
  flex: auto;
  margin: 10px;
}
.row-display {
  display: flex;
  flex-direction: row;
  margin-bottom: 5px;
}
.row-item {
  margin: 5px;
  flex: auto;
}
.row-inline-item {
  margin-right: 5px;
}
.column-display {
  display: flex;
  flex-direction: column;
}
.column-item {
  margin-bottom: 5px;
}
</style>