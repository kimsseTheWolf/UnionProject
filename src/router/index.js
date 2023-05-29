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
        component: ()=>import('@/views/projects/projectHome.vue')
    },
    {
        path: '/tags',
        name: "Tags management",
        component: ()=>import('@/views/tags/tagsHome.vue')
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
        name: "Settings Homepage",
        component: ()=>import('@/views/settings/settingsHome.vue')
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes: routers
})

export default router