import React from 'react'
import './App.css';
import MainPage from './pages/MainPage';
import Login from './pages/Login';
import Title from './components/Title';
import NewSession from './pages/NewSession';
import { BrowserRouter, Routes, Route, Navigate, HashRouter } from "react-router-dom";

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

  //const [checkedList, setCheckedList] = useState([]);
  //const [name, setName] = useState("");
  //const [loginSessionCode, setSessionCode] = useState("");

  // useEffect(() => {
  //   console.log(checkedList)
  // }, [checkedList])

  // const submit = () => {
  //   console.log('hgtuyvj');
  //   //fetch('server,com/uploasd/'+ sessionCode), {body: JSON.stringify({chexcked: checkedList})}.gthem()
  // }

  return (
    <div className='App'>
      <div className='header'>
        <Title/>
      </div>
      <div className='content'>
        <HashRouter >
          <Routes>
            <Route path="/" element={<Navigate to="login" />}/>
            <Route path="main" element={<MainPage />} />
            <Route path="login" element={<Login />} />
            <Route path="new-session" element={<NewSession />} />
          </Routes>
        </HashRouter >
      </div>
    </div>
  )
}

export default App