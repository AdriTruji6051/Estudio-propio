import axios from 'axios'
const tasksAPI = axios.create({
    baseURL: 'http://localhost:8000/tasks/api/v1/tasks/' //Definimos nuestra nueva direccion prefefinida :)
})

export const getAllTasks = () => {
    return tasksAPI.get('/')
}

// export const createTasks = (tasks) =>{
//     return tasksAPI.post('/', tasks)
// }

export const createTasks = (tasks) => tasksAPI.post('/', tasks); //----------------- Otra forma de escribirlo al solo trabajar una linea y devolver un valor

export const deleteTasks = (id) => tasksAPI.delete('/' + id);