import { BrowserRouter, Route, Routes } from "react-router-dom"
import Initial from "./components/initial"



const App=()=>{
    return(
      <div >
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Initial/>} />
        </Routes>
      </BrowserRouter>
      hola mundo
    </div>
    )
}

export default App
