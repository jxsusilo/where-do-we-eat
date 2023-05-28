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

  const [checkedListCuisine, setCheckedListCuisine] = useState([]);
  const [checkedListPrice, setCheckedListPrice] = useState([]);
  const [participants, setParticipants] = useState([]);
  const [restoList, setRestoList] = useState([]);

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

  // const restaurants = [
  //   { name: "Restaurant ABC", rating: 5, address: "123 First St, Los Angeles", imgsrc: "https://s3-media1.fl.yelpcdn.com/bphoto/hWa52yLwUAtiZh-xPYXGxg/o.jpg"},
  //   { name: "Second Restaurant", rating: 3, address: "222 Second St, Irvine", imgsrc: "https://s3-media2.fl.yelpcdn.com/bphoto/2vmY6wfVW3LRap0DFS-Ayw/o.jpg"},
  //   { name: "CUCINA enoteca Irvine", rating: 4, address: "222 Second St, Irvine", imgsrc: "https://s3-media2.fl.yelpcdn.com/bphoto/2vmY6wfVW3LRap0DFS-Ayw/o.jpg"},
  //   { name: "Luna Rossa", rating: 5, address: "222 Second St, Irvine", imgsrc: "https://s3-media2.fl.yelpcdn.com/bphoto/2vmY6wfVW3LRap0DFS-Ayw/o.jpg"},
  //   { name: "Brio Italian Grille", rating: 2, address: [
  //     "774 Spectrum Ctr Dr",
  //     "Irvine, CA 92618"
  //   ], imgsrc: "https://s3-media2.fl.yelpcdn.com/bphoto/2vmY6wfVW3LRap0DFS-Ayw/o.jpg"},
  // ]

  // const participantList = [
  //   username,
  //   'Friend1',
  //   'Friend2',
  //   'Friend3',
  // ]


useEffect(() => {
  console.log(checkedListCuisine, checkedListPrice);
  console.log(JSON.stringify({ checkedCuisine: checkedListCuisine, checkedPrice: checkedListPrice }));
  getdata();
}, [checkedListCuisine, checkedListPrice]);

const submit = () => {
  fetch('http://127.0.0.1:5000/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ checkedCuisine: checkedListCuisine, checkedPrice: checkedListPrice, roomCode: sessionCode })
  }).then(res => res.json()).then(response => {
    console.log(response)
    setRestoList(response['restaurants'])
    console.log(response)
  })
};

  const getdata = async () => {
    await fetch('http://127.0.0.1:5000/get-participants', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ roomCode: sessionCode })
    }).then(res => res.json()).then(response => {
      console.log(response);
      var participantList = response['info'];
      console.log(participantList, 'gfd');
      setParticipants(participantList)
    });
    await fetch('http://127.0.0.1:5000/get-restaurants', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ roomCode: sessionCode })
    }).then(res => res.json()).then(response => {
      console.log(response)
      setRestoList(response['restaurants'])
      console.log(response)
    });
  }



  return (
    <div className='App'>
      <p>Welcome, {username}!</p>
      <p>Session Code: {sessionCode}</p>
      <div className='container'>
        <div className='column' id='column1'>
          <h2>Enter Your Preferences:</h2>
          <UserInput name='Cuisine' listData={cuisineList} checkedList={checkedListCuisine} setCheckedList={setCheckedListCuisine} />
          <UserInput name='Price' listData={priceList} checkedList={checkedListPrice} setCheckedList={setCheckedListPrice} />
          <br></br>
          <button onClick={submit}>SUBMIT</button>
        </div>
        <div className='column' id='column2'>
          <h2>Results</h2>
          <RestaurantList listData={restoList}/>
        </div>
        <div className='column' id='column3'>
          <h2>Participants</h2>
            {participants.map((pname, index) => {
                return (
                    <p>{pname}</p>
                );
              })
            }
        </div>
      </div>
    </div>
  )
}

export default MainPage;