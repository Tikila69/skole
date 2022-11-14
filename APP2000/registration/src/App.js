import './App.css';
import { useState } from "react"
import Axios from "axios"



function App() {
  const [usernameReg, setUsernameReg] = useState("")
  const [passwordReg, setPasswordReg] = useState("")

  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const [loginStatus, setLoginStatus] = useState("")
  
  
  const register = () => {
    Axios.post("http://localhost:3001/register", {
      username: usernameReg,
      password: passwordReg
    }).then((response) => {
      console.log(response)
    })
  }

  const login = () => {
    Axios.post("http://localhost:3001/login", {
      username: username,
      password: password
    }).then((response) => {
      if (response.data.message) {
        setLoginStatus(response.data.message)
      } else {
        setLoginStatus(response.data[0].username)
      }
    })
  }

  return (
    <div className="App">
      <div className="registration">
        <h1>Registration</h1>
        <label>Username</label>
        <input type="text" onChange={(e)=> setUsernameReg(e.target.value)} /><br />

        <label>Password</label>
        <input type="password" onChange={(f) => setPasswordReg(f.target.value)}/><br />

        <button onClick={
          register
        }>Registration</button>
      </div>
      <div className="login">
        <h1>Registration</h1>
        <label>Username</label>
        <input type="text" placeholder="Username..." onChange={(e) =>setUsername(e.target.value)} /><br />

        <label>Password</label>
        <input type="password" onChange={(e) =>setPassword(e.target.value)} /><br />

        <button onClick={login}>Login</button>
        <h1>{loginStatus}</h1>
      </div>
    </div>
  );
}

export default App;
