import React, { useState, useEffect } from 'react'
//import Title from '../components/Title'
import UserInput from '../components/UserInput'
import '../App.css';
import RestaurantList from '../components/RestaurantList';
import { useLocation } from 'react-router-dom';

function MainPage(props) {
  // const [data, setData] = useState([{}])

  // useEffect (() => {
  //   fetch("http://localhost:5000/members").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )
  // }, [])
  const location = useLocation();
  //the data here will be an object since an object was
  const data = location.state;
  console.log(data);
  const sessionCode = data.sessionCode;
  const username = data.username;

  const [checkedList, setCheckedList] = useState([]);

  const cuisineList = [
    { id: "1", value: "American" },
    { id: "2", value: "Chinese" },
    { id: "3", value: "Greek" },
    { id: "4", value: "Indian" },
    { id: "5", value: "Italian" },
    { id: "6", value: "Japanese" },
    { id: "7", value: "Korean" },
    { id: "8", value: "Mexican" },
    { id: "9", value: "Nigerian" },
    { id: "10", value: "Thai" },
    { id: "11", value: "Vietnamese" },
  ];

  const priceList = [
    { id: "1", value: "$" },
    { id: "2", value: "$$" },
    { id: "3", value: "$$$" },
    { id: "4", value: "$$$$" },
  ];

  const restaurants = [
    { name: "Restaurant ABC", rating: 5, address: "123 First St, Los Angeles"},
    { name: "Second Restaurant", rating: 3, address: "222 Second St, Irvine"},
  ]


useEffect(() => {
  console.log(checkedList);
}, [checkedList]);

const submit = () => {
  fetch('http://127.0.0.1:5000/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ checked: checkedList })
  }).then(res => res.json()).then(response => {
    console.log(response)
  })
};

  return (
    <div className='App'>
      <p>Welcome, {username}!</p>
      <p>Session Code: {sessionCode}</p>
      <div className='container'>
        <div className='column'>
          <UserInput name='Cuisine' listData={cuisineList} checkedList={checkedList} setCheckedList={setCheckedList} />
          <UserInput name='Price' listData={priceList} checkedList={checkedList} setCheckedList={setCheckedList} />
          <button onClick={submit}>Submit Preferences</button>
        </div>
        <div className='column'>
          <h2>Results</h2>
          <RestaurantList listData={restaurants}/>
        </div>
      </div>
    </div>
  )
}

export default MainPage;