import { useEffect } from 'react';
import {useForm} from 'react-hook-form'; //Otras bibliotecas de validaciones son yup y zod 
import { createTasks, deleteTasks, updateTasks, getTask} from '../api/tasks.api';
import {useNavigate, useParams} from 'react-router-dom'
import { toast } from 'react-hot-toast'

export function TaskFormPage() {

  const {register, handleSubmit, formState: {errors}, setValue} = useForm()                            //para validar los datos de nuestros inputs
  const navigate = useNavigate()
  const params = useParams()


  const onSubmit = handleSubmit(async data => {

    if(params.id){
      console.log('Actualizando...')
      await updateTasks(params.id, data)
      //Mensaje de informacion ;)
      toast.success('Tarea actualizada', {position: 'bottom-right', 
      style: {
        background: 'yellow',
        color: 'black',
        height: 100,
        width: 300,
        fontSize: 35
      }})
    } 
    else {
      await createTasks(data);
      //Mensaje de informacion ;)
      toast.success('Tarea creada', {position: 'bottom-right', 
      style: {
        background: 'violet',
        color: 'white',
        height: 100,
        width: 300,
        fontSize: 35
      }})
    }

    navigate('/tasks');
  });

  useEffect(() => {

    async function loadTask() { // Se hace una funcion debido a que no podemos pasar como tal el codigo como si fuera parametro dentro de nuestro useEffect
      if(params.id){
        console.log('Obteniendo datos....')
        const res = await getTask(params.id)
        console.log(res)
        setValue('tittle', res.data.tittle)
        setValue('description', res.data.description)
      }
    }

    loadTask()
  }, []);

    return (
        <div className='max-w-xl mx-auto'> 
          <form onSubmit={onSubmit}>
            <input type="text" placeholder="tittle"
              {...register('tittle', { required: true})}
              className='bg-zinc-700 p-3 rounded-lg block w-full mb-3'                    //para almacenar datos en variables temporales mediante jsx
            />

              {errors.tittle && <span> este campo es requerido </span>}

            <textarea rows="3" placeholder="description"
              {...register('description', { required: true})} 
              className='bg-zinc-700 p-3 rounded-lg block w-full mb-3'     
            ></textarea>

              {errors.description && <span> este campo es requerido </span>}

            <button className='bg-indigo-500 p-3 rounded-lg block w-full mt-3'>Save</button>
          </form>

          {params.id && 
            <div className='flex justify-center'>
              <button 
                className='bg-red-500 p-3 rounded-lg w-48 mt-3'
                onClick={async () => {
                const accepted = window.confirm('Estas seguro?')
                if(accepted){
                  await deleteTasks(params.id)

                    //Mensaje de informacion ;)
                  toast.success('Tarea eliminada', {position: 'bottom-right', 
                    style: {
                      background: 'red',
                      color: 'white',
                      height: 100,
                      width: 300,
                      fontSize: 35
                    }})

                navigate('/tasks')
                  }
                 }}>Delete</button>
              </div>}
          
        </div>
      )
}