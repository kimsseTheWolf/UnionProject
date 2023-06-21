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
        path: '/setting',
        name: "Settings Homepage",
        component: ()=>import('@/views/settings/settingsHome.vue')
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

]

const router = createRouter({
    history: createWebHistory(),
    routes: routers
})

export default router