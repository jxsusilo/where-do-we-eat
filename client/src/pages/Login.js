import React, { useState, useEffect } from 'react'
import {useNavigate} from 'react-router-dom';


function Login(props) {

  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [code, setCode] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault()
    fetch('http://127.0.0.1:5000/setup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ roomcode: code, location: 0})
  })
    navigate('/main', {state: {
      sessionCode: code,
      username: name,
    }});
  }

  const createNewSession = (e) => {
    navigate('/new-session');
  }

  return (
    <div className='login'>
        <h3>Login to Existing Session</h3>
        <form onSubmit={handleSubmit}>
            <label>Session Code:
                <br/>
                <input
                type="text" 
                value={code}
                onChange={(e) => setCode(e.target.value)}
                />
            </label>
            <br/>
            <label>Name:
                <br/>
                <input
                type="text" 
                value={name}
                onChange={(e) => setName(e.target.value)}
                />
            </label>
            <br/>
            <input type="submit" />
        </form>
        <p>OR</p>
        <h3>Create a New Session</h3>
        <button onClick={createNewSession}>CREATE</button>
    </div>
  )
}

export default Login;