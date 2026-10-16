import React from "react";

const PrevCards = ({ prevCards, removePrevCard }) => (
	<div className="prev-cards">
		{prevCards.map((card, index) => (
			<div className="prev-card" key={index}>
				<span className="prev-card-name">{card.name}</span>
				<a href={card.scryfall_uri}>Link to card</a>
				<button type="button" onClick={() => removePrevCard(card)}>Remove</button>
			</div>
		))}
	</div>
);

export default PrevCards;