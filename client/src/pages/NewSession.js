import React, { useState, useEffect } from 'react'
import {useNavigate} from 'react-router-dom';

function NewSession() {
    const navigate = useNavigate();

    const [name, setName] = useState("");
    const [loc, setLoc] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault()
        navigate('/main', {state: {
          sessionCode: '(RANDOMLY GENERATED CODE)',
          username: name,
        }});
      }

    return(
        <div className="newSession">
            <h3>Create New Session</h3>
            <form onSubmit={handleSubmit}>
                <label>Location:
                    <br/>
                    <input
                    type="text" 
                    value={loc}
                    onChange={(e) => setLoc(e.target.value)}
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
        </div>
    )
}

export default NewSession;