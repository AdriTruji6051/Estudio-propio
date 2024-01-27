import { useEffect, useState } from "react"
import { getAllTasks } from '../api/tasks.api'
import { TaskCard } from "./TaskContainer";

export  function TaskList() {

    const [tasks, setTasks] = useState([])

    useEffect(() => {
        console.log('Pagina cargada')

        async function loadTasks() {
            const res = await getAllTasks()
            setTasks(res.data)
        }

        loadTasks();

    }, []);

  return (
    <div>
        {tasks.map( tasks => (
            <TaskCard key = {tasks.id}  tasks = {tasks}/>
        ))}
    </div>
  )
}
