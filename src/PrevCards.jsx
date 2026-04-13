import React from "react";

const PrevCards = ({prevCards, removePrevCard}) => {

	

	return (
		<div>
			{prevCards.map((card, index) => (
				<div key={index}>
					<p>{card.name}</p>
					<a href={card.scryfall_uri}>Link to card</a>
					<button onClick={() => removePrevCard(card)}>Remove</button>
				</div>
			))}
		</div>
	)
}

export default PrevCards;