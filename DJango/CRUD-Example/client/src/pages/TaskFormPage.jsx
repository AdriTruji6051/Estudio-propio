import {useForm} from 'react-hook-form'; //Otras bibliotecas de validaciones son yup y zod 
import { createTasks, deleteTasks } from '../api/tasks.api';
import {useNavigate, useParams} from 'react-router-dom'

export function TaskFormPage() {

  const {register, handleSubmit, formState: {errors}} = useForm()                            //para validar los datos de nuestros inputs
  const navigate = useNavigate()
  const params = useParams()


  const onSubmit = handleSubmit(async data => {
    const res = await createTasks(data)
    navigate('/tasks')
  })

    return (
        <div> 
          <form onSubmit={onSubmit}>
            <input type="text" placeholder="tittle"
              {...register('tittle', { required: true})}                      //para almacenar datos en variables temporales mediante jsx
            />

              {errors.tittle && <span> este campo es requerido </span>}

            <textarea rows="3" placeholder="description"
              {...register('description', { required: true})}    
            ></textarea>

              {errors.description && <span> este campo es requerido </span>}

            <button>Save</button>
          </form>

          {params.id && <button onClick={async () => {
            const accepted = window.confirm('Estas seguro?')
            if(accepted){
              await deleteTasks(params.id)
              navigate('/tasks')
            }
          }}>Delete</button>}
          
        </div>
      )
}