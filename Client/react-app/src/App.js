// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
import axios from 'axios'
import logo from './logo.svg';

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(() => {
    axios.get('http://127.0.0.1:4000/data').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>React + Flask Dockerized application</p>
        <div>{getMessage.status === 200 ?

          // <h3>{JSON.stringify(getMessage.data)}</h3>
          <h3>{getMessage.data.backend_data}</h3>
          :
          <h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}

export default App;
