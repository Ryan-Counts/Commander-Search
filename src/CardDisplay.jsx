const CardDisplay = ({ currentCard }) => {
	if (!currentCard || (!currentCard.image_uris && !currentCard.card_faces)) return null;

	return (
		<div className="card-display">
			{currentCard.image_uris ? (
				<img src={currentCard.image_uris.normal} alt={currentCard.name} />
			) : (
				currentCard.card_faces.map((face, index) => (
					<img key={index} src={face.image_uris?.normal} alt={face.name} />
				))
			)}
		</div>
	);
};

export default CardDisplay;