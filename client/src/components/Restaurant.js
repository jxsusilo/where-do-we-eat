import React, { useState, useEffect } from 'react';

function Restaurant(props) {
    const [vote, setVote] = useState([]);

    const capitalizedCuisine = (props.resto.cuisine).charAt(0).toUpperCase() + (props.resto.cuisine).slice(1)
    var stars = "";
    for (let i = 0; i < props.resto.rating; i++) {
        stars += "★";
    }

    const upvote = () => {
        if (vote == 1) {
            setVote(0);
            fetch('http://127.0.0.1:5000/downvote', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({ restaurant: props.resto.name})
    })
        } else {
            setVote(1);
            fetch('http://127.0.0.1:5000/upvote', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({ restaurant: props.resto.name})
    })
        }
        console.log(vote);
    }

    const downvote = () => {
        if (vote == -1) {
            setVote(0);
            fetch('http://127.0.0.1:5000/upvote', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({ restaurant: props.resto.name})
    })
        } else {
            setVote(-1);
            fetch('http://127.0.0.1:5000/downvote', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({ restaurant: props.resto.name})
    })
        }
        console.log(vote);
    }

    return(
        <div className="restaurant">
            <img className="resto-img" src={props.resto.image_url}/>
            <div className="resto-info">
                <div className="resto-name">
                    <h3>{props.resto.name}</h3>
                </div>
                <p>{capitalizedCuisine} | {props.resto.price}</p>
                <p className="stars">{stars}</p>
                {(props.resto.location).map((loc, index) => {
                return (
                    <div>{loc}</div>
                );
            })}
            </div>
            <div className="votes">
                <button className="upvote" onClick={upvote} style={vote == 1 ? {backgroundColor:'#6C8EAD'} : {}}>▲</button>
                <button className="downvote" onClick={downvote} style={vote == -1 ? {backgroundColor:'#6C8EAD'} : {}}>▼</button>
            </div>
        </div>
    )
}

export default Restaurant