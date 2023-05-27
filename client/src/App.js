import React, { useState, useEffect } from 'react'
import Title from './components/Title'
import UserInput from './components/UserInput'
import './App.css';
import RestaurantList from './components/RestaurantList';

function App() {
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

  const [checkedList, setCheckedList] = useState([]);

  const cuisineList = [
    { id: "1", value: "American" },
    { id: "2", value: "Chinese" },
    { id: "3", value: "Italian" },
    { id: "4", value: "Japanese" },
    { id: "5", value: "Korean" },
    { id: "6", value: "Mexican" },
    { id: "7", value: "Thai" },
    { id: "8", value: "Vietnamese" },
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

  const sessionCode = "ABCDE1"

  useEffect(() => {
    console.log(checkedList)
  }, [checkedList])

  const submit = () => {
    console.log('hgtuyvj');
    //fetch('server,com/uploasd/'+ sessionCode), {body: JSON.stringify({chexcked: checkedList})}.gthem()
  }

  return (
    <div className='App'>
      <Title/>
      <p>Session Code: {sessionCode}</p>
      <div className='container'>
        <div className='column'>
          <UserInput name='Cuisine' listData={cuisineList} checkedList={checkedList} setCheckedList={setCheckedList} />
          <UserInput name='Price' listData={priceList} checkedList={checkedList} setCheckedList={setCheckedList} />
          <button>Submit Preferences</button>
        </div>
        <div className='column'>
          <h2>Results</h2>
          <RestaurantList listData={restaurants}/>
        </div>
        <button onClick={submit}>clicjk, hgtr</button>
      </div>
    </div>
  )
}

export default App