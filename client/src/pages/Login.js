import React, { useState, useEffect } from 'react'

function Login(props) {

      const [name, setName] = useState("");
      const [code, setCode] = useState("");

      const handleSubmit = (e) => {
        e.preventDefault()
        alert(name + code);
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
            <button>Create</button>
        </div>
      )
}

export default Login;