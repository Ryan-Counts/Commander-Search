import { useState, useEffect, useMemo } from 'react'
import APIService from './APIService.jsx'

import Form from './Form.jsx'
import './App.css'


function App() {
  
  //const [count, setCount] = useState(0);
  const [currentCard, setCurrentCard] = useState(0);
  //const [searchTerm, setSearchTerm] = useState(0);
  const [colors, setColors] = useState('')

  useEffect(() => {
    fetch('/api/getCard').then(res => res.json()).then(data => {
      setCurrentCard(data);
    });
  }, []);


  const ColorList = [
  { 
    order: 0,
    name: 'White',
  },
  { 
    order: 1,
    name: 'Blue',
  },
  { 
    order: 2,
    name: 'Black',
  },
  { 
    order: 3,
    name: 'Red',
  },
  { 
    order: 4,
    name: 'Green',
  }
];


  /*const search = useEffect(() => {
    const selectedColors = data.filter((d) => d.checked).map((d) => d.name);
    console.log(selectedColors);
    fetch('/api/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ colors: selectedColors.join(',') }),
    })
    .then(res => res.json())
    .then(data => {
      console.log(data);
      setCurrentCard(data);
    });

  });*/

  return (

    <>
      <section id="header">
        <h1>Commander Search</h1>
      </section>
      <section id="search">
        <Form 
          colors={colors}
          setCurrentCard={setCurrentCard}
        />
      </section>
      <section id="center">
        <p>The current card is {currentCard.name}.</p>
        <img src={currentCard.image_uris?.normal} alt={currentCard.name} />
      </section>

      <div className="ticks"></div>

      
      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
