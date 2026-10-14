import React from 'react';

const CardDisplay = ({currentCard}) => {
		

	return (
		<div>
			{currentCard.card_faces ? (
            <div>
              {currentCard.card_faces.map((face, index) => (
                <img key={index} src={face.image_uris?.normal} alt={face.name} />
              ))}
            </div>
          ) : (
            <img src={currentCard.image_uris?.png} alt={currentCard.name} />
          )}      
		</div> 
	)
}

export default CardDisplay;