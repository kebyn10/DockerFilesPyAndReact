import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { getTasks } from "../features/tasks/tasksSlice"

const Initial = () => {
    const tasks=useSelector(state=>state.tasks)
    console.log('taskssss->',tasks.tasks);
    const dispatch=useDispatch()
    useEffect(()=>{
      const peticion=async()=>{
          fetch('http://fastapiPrueba:8000/api/getAll', {
              method: 'GET',
              headers: {
                  'Content-Type': 'application/json'
              }
          })
          .then(response => response.json())
          .then(data => {
            console.log('data',data);
            dispatch(getTasks(data))
          })
          .catch(error1=> {
            console.log('segundo intento el link http://fastapiPrueba:8000/api/getAll no sirve error1',error1);
            fetch('http://localhost:8000/api/getAll', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
              console.log('data',data);
              dispatch(getTasks(data))
            })
            .catch((error)=>{
                console.log('segundo intento el link http://localhost:8000/api/getAll no sirve',error);
            })
          });
         
      }   
  
      peticion()
     
  },[])
    return (
      <>
        <h1 style={{width:"100%",textAlign:"center"}}>
          Tareas 
        </h1>
        <div style={{width:"100%",display:"flex",justifyContent:"space-evenly"}}>
          {
            tasks.tasks.length>0 ? 
            tasks.tasks.map((item,id)=>(
                <div key={id} style={{width:"40%",padding:"3px",borderRadius:"20px",background:"black",color:"white",marginRight:"5px"}}>
              <h3 style={{padding:"4px"}}>Titulo</h3>
              <p  style={{padding:"4px"}}>Description</p>
            </div>
              ))
              
            : null
          }
         
        </div>
      </>
    )
}

export default Initial