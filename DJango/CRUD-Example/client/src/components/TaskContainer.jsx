import { useNavigate } from "react-router-dom"

export function TaskCard({ tasks }) {

  const navigate = useNavigate()


    return (
  
      <div style={{background: "blue"}}
        onClick={() =>{
          navigate('/tasks/' + tasks.id)
        }}
      >
          <h1>{tasks.tittle}</h1>
          <p>{tasks.description}</p>
          <hr/>
      </div>
  
    )
  }