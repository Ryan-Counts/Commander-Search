 import { useState, useEffect, useMemo } from 'react'
import APIService from './APIService.jsx'

import './App.css'
import Form from './Form.jsx'
import CardDisplay from './CardDisplay.jsx';
import PrevCards from './PrevCards.jsx';

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


function App() {

  const [currentCard, setCurrentCard] = useState(0);
  const [cardFaces, setCardFaces] = useState(0);
  const [colors, setColors] = useState(ColorList.sort((a, b) => a.order - b.order))
  const [prevCards, setPrevCards] = useState([]);

  useEffect(() => {
    fetch('/api/getCard')
      .then(res => res.json())
      .then(data => {
        if (data && data.object !== 'error' && !data.error) setCurrentCard(data);
      })
      .catch(() => {});
  }, []);

  const newCard = (card) => {
    setCurrentCard(card);
    setPrevCards([...prevCards, card]);
  };

  const removePrevCard = (targetCard) => {
    setPrevCards(prev => prev.filter(card => card.name !== targetCard.name));
  };

  return (
    <>
      <section id="header">
        <h1>Commander Search</h1>
      </section>
      <section id="search">
        <Form 
          colors={colors}
          newCard={newCard}
          ColorList={ColorList}
        />
      </section>
      <section id="center">
        <p>The current card is {currentCard.name}.</p>
        <div>The link to the current card is <a href={currentCard.scryfall_uri}> here</a>.</div>
        <CardDisplay
          currentCard={currentCard}
        />
        <h4>Previous Cards:</h4>
        <PrevCards
          prevCards={prevCards}
          removePrevCard={removePrevCard}
        />

      </section>

      <div className="ticks"></div>

      
      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
