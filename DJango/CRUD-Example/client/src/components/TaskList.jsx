import { useEffect, useState } from "react"
import { getAllTasks } from '../api/tasks.api'

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
            <div key={tasks.id}>
                <h1>{tasks.tittle}</h1>
                <p>{tasks.description}</p>
            </div>
        ))}
    </div>
  )
}
