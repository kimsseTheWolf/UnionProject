<script setup>
import HeaderContentView from "@/components/splitViews/headerContentView.vue";
import {computed, ref, toRaw, unref} from "vue";
import {useRouter} from "vue-router";
import CreateTag from "@/views/tags/createTag.vue";
import CreateScriptCreater from "@/components/explorer/createScriptCreater.vue";
import {message} from "ant-design-vue";
import {PlusCircleOutlined, ScheduleOutlined, DesktopOutlined, ExclamationCircleTwoTone} from "@ant-design/icons-vue";
import FormLine from "@/components/form/form-line.vue";

const router = useRouter()

const projectName = ref("")
const projectDescription = ref("")
const projectTags = ref([])
const availableTagsNames = ref([])
const availableCreationMethods = ref([])
const availableTagsInfo = ref({})
const processedTagsList = ref([])
const startDate = ref()
const enableEndDate = ref(true)
const endDate = ref()
const fullDate = ref([startDate.value, endDate.value])
const storeMethod = ref("inApp")
const projectStoreLocation = ref("")
const selectedMethodName = ref("notSelected")
const methodDescription = ref("")
const overviewCollapseActiveKeys = ref(['basic', 'date', 'storage', 'template'])

const tagMenuSelectedItem = ref([])

const displayCreateTagPage = ref(false)
const displayDirUnsafeWarning = ref(false)

const stepCount = ref(1)
const createProjectIsLoading = ref(false)
const isDisplayDateWarning = computed(()=>{
  try {
    let content = startDate.value.$d
    return {status: false, data:content}
  }
  catch (e) {
    return {status: true}
  }
})
const isDisplayEndDate = computed(()=>{
  try{
    let content = endDate.value.$d
    return {status: true, data: content}
  }
  catch (e) {
    return {status: false, data: undefined}
  }
})
const allowCreate = computed(()=>{
  if (projectName.value === "") {
    console.log("Name does not passed")
    return false
  }
  if (isDisplayDateWarning.value.status) {
    console.log("Start date does not passed")
    return false
  }
  if (enableEndDate.value === true && isDisplayEndDate.value.status === false) {
    console.log("End date does not passed")
    return false
  }
  if (storeMethod.value !== "inApp" && projectStoreLocation.value === '') {
    console.log("Store location does not passed")
    return false
  }
  if (selectedMethodName.value === "notSelected" || selectedMethodName.value === "createNewScript") {
    console.log("Template method does not passed")
    return false
  }
  else{
    return true
  }

})

async function getTagsData() {
  // hide the modal
  displayCreateTagPage.value = false
  // read and apply tags metadata to react value
  let tagsName = await window.tags.openMetadataFile()
  availableTagsInfo.value = tagsName
  // apply the keys to the list
  availableTagsNames.value = Object.keys(tagsName)
}

function handleTagMenuOnselect() {
  if (tagMenuSelectedItem.value.indexOf('unionProject:createNewTag') !== -1) {
    handleCreateTagPage()
  }
}

function handleCreateTagPage() {
  displayCreateTagPage.value = !displayCreateTagPage.value
}

function handleTagSelected(tagName) {
  // identify whether the item has already added to the list
  if (projectTags.value.indexOf(tagName) !== -1) {
    return
  }
  // add the name of the tag to the selected list
  projectTags.value.push(tagName)
}

function handleTagDeleted(tagName) {
  // identify whether the tag is existed in the list
  if (projectTags.value.indexOf(tagName) === -1) {
    return
  }
  // remove the tag from the list using the tag name
  let targetIndex = projectTags.value.indexOf(tagName)
  projectTags.value.splice(targetIndex, 1)
}

async function checkDirIsSafe(dir) {
  let result = await window.fs.checkDirectoryIsEmpty(dir)
  if (!result) {
    displayDirUnsafeWarning.value = true
    return
  }
  displayDirUnsafeWarning.value = false
}

async function triggerOpenFolderSelection() {
  let result = await window.fs.openFolderDialog(false, "", "选择一个文件夹")
  // apply the store location to the app
  if (result === undefined) {
    projectStoreLocation.value = ""
    return
  }
  projectStoreLocation.value = result[0]
  await checkDirIsSafe(projectStoreLocation.value)
}

async function getCreateMethods() {
  let result = await window.project.getCreateMethods()
  availableCreationMethods.value = result[0]
}

async function getCreateMethodData(csLocation) {
  // get the original filename
  let id = csLocation.substring(0, 36)
  let result = await  window.createMethod.readScript(csLocation)
  methodDescription.value = result.data.description
}

function handleTimeRageChange(dates, valueStrings){
  console.log(dates)
  startDate.value = dates[0]
  endDate.value = dates[1]
}

// create project
async function createProject() {
  createProjectIsLoading.value = false
  // process tag ID
  for (let i = 0; i < projectTags.value.length; i++) {
    processedTagsList.value.push(availableTagsInfo.value[projectTags.value[i]].uuid)
  }
  // process store location
  if (storeMethod.value === "inApp") {
    projectStoreLocation.value = "inApp"
  }


  let tempScriptLocation = await window.createMethod.generateScript(toRaw(projectName.value), toRaw(projectDescription.value), toRaw(processedTagsList.value), toRaw(startDate.value.$d), toRaw(endDate.value.$d), toRaw(projectStoreLocation.value), toRaw(selectedMethodName.value))
  message.info("已生成脚本，正在创建项目……")
  console.log(tempScriptLocation)
  createProjectIsLoading.value = true
}

// Init process
getTagsData()
getCreateMethods()
</script>

<template>
  <header-content-view title="创建新项目" sub-title="设置您希望如何创建这个新项目">

    <a-steps :current="stepCount - 1">
      <a-step title="基本信息" @click="stepCount = 1"></a-step>
      <a-step title="开始&结束时间" @click="stepCount = 2"></a-step>
      <a-step title="存放方式" @click="stepCount = 3"></a-step>
      <a-step title="项目模板" @click="stepCount = 4"></a-step>
      <a-step title="总览" @click="stepCount = 5"></a-step>
    </a-steps>

    <div style="margin-top: 10px">
      <div v-if="stepCount === 1">
        <div><b>项目名称</b></div>
        <a-input v-model:value="projectName"></a-input>
        <div class="column-item"><b>项目简介</b></div>
        <a-textarea v-model:value="projectDescription"></a-textarea>
        <div class="column-item"><b>项目标签</b></div>
        <div class="tags-panel">
          <div class="row-display">
            <a-tag v-for="tag in projectTags" :key="tag" :closable="true" @close="handleTagDeleted(tag)" :color="availableTagsInfo[tag].color">{{tag}}</a-tag>
            <div v-if="projectTags.length === 0">选择标签并添加到此处</div>
          </div>
        </div>
        <a-dropdown class="column-item">
          <template #overlay>
            <a-menu>
              <a-menu-item-group>
                <template #title>使用现有的标签</template>
                <a-menu-item v-for="tagName in availableTagsNames" :key="tagName" @click="handleTagSelected(tagName)">
                  {{tagName}}
                </a-menu-item>
              </a-menu-item-group>
              <a-menu-item-group>
                <template #title>没有想要的标签？</template>
                <a-menu-item key="unionProject:createNewTag" @click="handleCreateTagPage">
                  创建一个新的标签
                </a-menu-item>
              </a-menu-item-group>
            </a-menu>
          </template>
          <a-button>
            <PlusCircleOutlined/>
            添加新的标签
          </a-button>
        </a-dropdown>
        <a-divider></a-divider>
      </div>

      <div v-if="stepCount === 2">
        <div class="column-item">
          <div class="row-display">
            <div class="row-item">
              <ScheduleOutlined/>
            </div>
            <div class="row-item">
              <b>选择项目开始 / 结束的日期与时间</b>
            </div>
          </div>
        </div>
        <div class="column-item">
          <form-line>
            <template #title>
              选择开始日期
            </template>
            <template #description>
              当项目开始之后系统会提示您
            </template>
            <template #right-item>
              <a-range-picker :show-time="{ format: 'HH:mm' }" class="row-item" :placeholder="['选择开始日期', '选择结束日期']" format="YYYY-MM-DD HH:mm" v-if="enableEndDate" @change="handleTimeRageChange" v-model:value="fullDate"></a-range-picker>
              <a-date-picker :show-time="{ format: 'HH:mm' }" class="row-item" placeholder="选择开始日期" format="YYYY-MM-DD HH:mm" v-model:value="startDate" v-if="!enableEndDate"></a-date-picker>
            </template>
          </form-line>
          <form-line>
            <template #title>这个项目包含结束日期</template>
            <template #description>若您不希望这个项目有结束日期限制，可以关闭此开关</template>
            <template #right-item>
              <a-switch v-model:checked="enableEndDate"></a-switch>
            </template>
          </form-line>
          <a-divider/>
        </div>
      </div>

      <div v-if="stepCount === 3">
        <div class="column-item">
          <div class="row-display">
            <div class="row-item">
              <DesktopOutlined/>
            </div>
            <div class="row-item">
              <b>存放方式</b>
            </div>
          </div>
        </div>
        <form-line>
          <template #title>选择存储位置</template>
          <template #right-item>
            <a-select v-model:value="storeMethod">
              <a-select-option value="inApp">将项目数据存储在应用程序内</a-select-option>
              <a-select-option value="local">将项目数据存储在本地的其他位置上</a-select-option>
            </a-select>
          </template>
        </form-line>
        <form-line>
          <template #description>
            <div id="description" v-if="storeMethod === 'inApp'">此方法将会把你的所有项目相关文件（元数据文件与文档）存储在Union Project的运行目录下。</div>
            <div id="description" v-if="storeMethod === 'local'">此方法将会把你的所有项目相关文件（元数据文件与文档）存储在您指定的目录下</div>
          </template>
        </form-line>
        <div class="column-item" v-if="storeMethod === 'local'">
          <form-line>
            <template #title>选择本地存储位置</template>
            <template #right-item>
              <a-button type="primary" @click="triggerOpenFolderSelection">选择文件位置</a-button>
            </template>
            <template #description>
              您已经选择了位置：{{projectStoreLocation}}
            </template>
          </form-line>
          <a-alert message="此目录非空" type="warning" v-if="displayDirUnsafeWarning" class="column-item">
            <template #description>
              这个目录里还有其他文件和文件夹，创建新项目的操作会覆写此文件夹中所有的数据，请妥善处理并及时备份！
            </template>
          </a-alert>
        </div>
        <a-divider/>
      </div>

      <div v-if="stepCount === 4">
        <div class="column-display" style="margin-top: 5px">
          <form-line>
            <template #title>
              选择一个模板
            </template>
            <template #description>
              选择您希望如何生成此项目
            </template>
            <template #right-item>
              <a-select v-model:value="selectedMethodName" class="column-item">
                <a-select-option value="notSelected">选择模板</a-select-option>
                <a-select-option v-for="i in availableCreationMethods" :value="i.file_name" :index="i" @click="getCreateMethodData(i.file_name)">{{i.friendly_name}}</a-select-option>
                <a-select-option value="createNewScript">创建自定义模板</a-select-option>
              </a-select>
            </template>
          </form-line>
          <form-line>
            <template #title>模板描述</template>
            <template #description>{{methodDescription}}</template>
          </form-line>
          <!--        <create-script-creater v-if="selectedMethodName === 'createNewScript'"></create-script-creater>-->
          <form-line v-if="selectedMethodName === 'createNewScript'">
            <template #title>打开模板编辑器</template>
            <template #description>使用内置的模板编辑器快速创建项目模板</template>
            <template #right-item>
              <a-button type="primary" @click="message.info('此功能还未上线，尽请期待！')">打开项目模板编辑器</a-button>
            </template>
          </form-line>
          <a-divider></a-divider>
        </div>
      </div>

      <div v-if="stepCount === 5">
        <div><b>检查所有项目属性</b></div>
        <a-alert v-if="!allowCreate" message="部分必要信息没有填写或无效。请检查所有的信息并修正无效信息。" type="warning" class="column-item"></a-alert>
        <a-collapse class="column-item" v-model:activeKey="overviewCollapseActiveKeys">
          <a-collapse-panel key="basic" header="基本信息">
            <form-line>
              <template #title>项目名称</template>
              <template #description>{{projectName}}</template>
              <template #right-item>
                <a-button type="link" @click="stepCount = 1">修改</a-button>
                <a-tooltip v-if="projectName === ''">
                  <template #title>
                    您必须填写此字段，否则项目无法正常创建
                  </template>
                  <ExclamationCircleTwoTone two-tune-color="#eb2f96" class="bigger-icon"/>
                </a-tooltip>
              </template>
            </form-line>
            <form-line>
              <template #title>项目简介</template>
              <template #description>{{projectDescription}}</template>
              <template #right-item>
                <a-button type="link" @click="stepCount = 1">修改</a-button>
              </template>
            </form-line>
            <form-line>
              <template #title>选择的标签</template>
              <template #description>
                <div class="row-display">
                  <a-tag v-for="tag in projectTags" :key="tag" :closable="false" :color="availableTagsInfo[tag].color">{{tag}}</a-tag>
                </div>
              </template>
              <template #right-item>
                <a-button type="link" @click="stepCount = 1">修改</a-button>
              </template>
            </form-line>
          </a-collapse-panel>
          <a-collapse-panel key="date" header="项目开始与截止日期">
            <form-line>
              <template #title>项目开始日期</template>
              <template #description v-if="!isDisplayDateWarning.status">{{isDisplayDateWarning.data}}</template>
              <template #right-item>
                <a-button type="link" @click="stepCount = 2">修改</a-button>
                <a-tooltip v-if="isDisplayDateWarning.status">
                  <template #title>
                    您必须填写此字段，否则项目无法正常创建
                  </template>
                  <ExclamationCircleTwoTone two-tune-color="#eb2f96" class="bigger-icon"/>
                </a-tooltip>
              </template>
            </form-line>
            <form-line>
              <template #title>项目结束日期</template>
              <template #description v-if="isDisplayDateWarning.data">
                {{isDisplayDateWarning.data}}
              </template>
              <template #description v-if="!isDisplayDateWarning.data">
                此项目并没有设置结束日期
              </template>
              <template #right-item>
                <a-button type="link" @click="stepCount = 2">修改</a-button>
              </template>
            </form-line>
          </a-collapse-panel>
          <a-collapse-panel key="storage" header="存放方式">
            <form-line>
              <template #title>存放方式</template>
              <template #description>
                <div v-if="storeMethod === 'inApp'">
                  存储在Union Project应用程序内部
                </div>
                <div v-else>
                  存储在外部：{{projectStoreLocation}}
                </div>
              </template>
              <template #right-item>
                <a-button type="link" @click="stepCount = 3">修改</a-button>
                <a-tooltip v-if="storeMethod !== 'inApp' && projectStoreLocation === ''">
                  <template #title>
                    您必须提供存储位置，否则项目无法正常创建
                  </template>
                  <ExclamationCircleTwoTone two-tune-color="#eb2f96" class="bigger-icon"/>
                </a-tooltip>
              </template>
            </form-line>
          </a-collapse-panel>
          <a-collapse-panel key="template" header="模板设置">
            <form-line>
              <template #title>使用的模板</template>
              <template #description>
                <div v-if="selectedMethodName === 'notSelected'">
                  未选择
                </div>
                <div v-else-if="selectedMethodName === 'createNewScript'">
                  创建自定义模板
                </div>
                <div v-else>
                  {{selectedMethodName}}
                </div>
              </template>
              <template #right-item>
                <a-button type="link" @click="stepCount = 4">修改</a-button>
                <a-tooltip v-if="selectedMethodName === 'notSelected' || selectedMethodName === 'createNewScript'">
                  <template #title>
                    您必须选择一个模板，否则项目将无法正常创建
                  </template>
                  <ExclamationCircleTwoTone two-tune-color="#eb2f96" class="bigger-icon"/>
                </a-tooltip>
              </template>
            </form-line>
          </a-collapse-panel>
        </a-collapse>
        <a-divider/>
      </div>
    </div>

    <div style="margin-top: 10px" class="row-display">
      <a-button type="primary" :disabled="stepCount >= 5" class="row-item" v-on:click="stepCount++">下一步</a-button>
      <a-button :disabled="stepCount <= 1" class="row-item" v-on:click="stepCount--">上一步</a-button>
      <a-button :disabled="!allowCreate" class="row-item" type="primary" @click="createProject" :loading="createProjectIsLoading">创建并完成</a-button>
    </div>


    <a-modal title="创建一个新的标签" :visible="displayCreateTagPage">
      <create-tag @on-create-tag="getTagsData"></create-tag>
      <template #footer>
        <a-button @click="handleCreateTagPage">取消</a-button>
      </template>
    </a-modal>
  </header-content-view>
</template>

<style scoped>
.row-display {
  display: flex;
  flex-direction: row;
}
.row-item {
  margin-right: 5px;
}
.column-display {
  display: flex;
  flex-direction: column;
}
.column-item {
  margin-top: 5px;
}
#description {
  color: gray;
}
.tags-panel{
  display: flex;
  flex-direction: column;
  margin-top: 5px;
  margin-bottom: 5px;
  border-radius: 5px;
  padding: 5px;
  background-color: #f5f5f5;
}
.bigger-icon{
  font-size: large;
}
</style>