import { createRouter, createWebHistory } from 'vue-router'
import EmptyOccupation from "@/views/emptyOccupation.vue";

const routers = [
    {
        path: '/',
        name: 'homeEmptyPage',
        component: EmptyOccupation
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routers
})

export default router