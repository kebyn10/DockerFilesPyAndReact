import { configureStore } from "@reduxjs/toolkit";
import taskReucer from "../features/tasks/tasksSlice.js"

export const store=configureStore({
    reducer:{
        tasks:taskReucer
    }
})