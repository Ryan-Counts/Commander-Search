import React from 'react';

const CardDisplay = ({ currentCard }) => (
	<div className="card-display">
		{currentCard.card_faces ? (
			currentCard.card_faces.map((face, index) => (
				<img key={index} src={face.image_uris?.normal} alt={face.name} />
			))
		) : (
			<img src={currentCard.image_uris?.normal} alt={currentCard.name} />
		)}
	</div>
);

export default CardDisplay;