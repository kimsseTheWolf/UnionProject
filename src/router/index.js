import { createRouter, createWebHistory } from 'vue-router'
import EmptyOccupation from "@/views/emptyOccupation.vue";

const routers = [
    {
        path: '/',
        name: 'homeEmptyPage',
        component: EmptyOccupation
    },
    {
        path: '/project',
        name: "project homepage",
        component: ()=>import('@/views/projects/projectHome.vue'),
        children: [
            {
                path: '',
                component: ()=>import('@/views/projects/projectList.vue')
            },
            {
                path: 'create',
                component: ()=>import('@/views/projects/createProject.vue')
            }
        ]
    },
    {
        path: '/tags',
        name: "Tags management",
        component: ()=>import('@/views/tags/tagsHome.vue'),
        children: [
            {
                path: 'create',
                component: ()=>import('@/views/tags/createTag.vue')
            },
            {
                path: 'details/:tagName',
                component: ()=>import('@/views/tags/tagsDetails.vue')
            },
            {
                path: 'modify/:targetTagName',
                component: ()=>import('@/views/tags/modifyTag.vue')
            },
        ]
    },
    {
        path: '/dashboard',
        name: "Dashboard Homepage",
        component: ()=>import('@/views/dashboard/dashboardHome.vue')
    },
    {
        path: '/todo',
        name: "Todo Homepage",
        component: ()=>import('@/views/todo/todoHome.vue')
    },
    {
        path: '/settings',
        name: "",
        component: ()=>import('@/views/settings/settingsHome.vue'),
        children: [
            {
                path: 'security',
                component: ()=>import('@/views/settings/security.vue')
            },
            {
                path: 'creationScript',
                component: () => import('@/views/settings/creationScript.vue')
            }
        ]
    },
    {
        path: '/test',
        name: "Settings Homepage",
        component: ()=>import('@/views/test/testHome.vue'),
        children: [
            {
                path: 'fs',
                component: ()=>import('@/views/test/fileReadAndWriteTest.vue')
            }
        ]
    },
    {
        path: '/explorer',
        name: "File Explorer",
        component: () => import('@/views/virtualFsManager/createScriptVisualEditor.vue'),
        children: [
            {
                path: 'createScriptEditor/:scriptName',
                component: () => import('@/views/virtualFsManager/createScriptVisualEditor.vue'),
            }
        ]
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes: routers
})

export default router