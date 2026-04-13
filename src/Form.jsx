import React,{ useState } from 'react';
import APIService from './APIService.jsx'
import Checkbox from './Checkbox.jsx'


const searchTypes = [
    {
        type: 'CMC'
    },
    {
        type: 'Power'
    },
    {
        type: 'Toughness'
    },
    {
        type: 'Oracle Text'
    },
    {
        type: 'Artist'
    },
    {
        type: 'Rarity'
    },
    {
        type: 'Type Line'
    },
    {
        type: 'ID Type'
    }
];

const rarities = [
    {
        type: 'Common'
    },
    {
        type: 'Uncommon'
    },
    {
        type: 'Rare'
    },
    {
        type: 'Mythic'
    }
];

const Form = ({colors, newCard, ColorList}) => {

    const [searchTerms, setSearchTerms] = useState([])
    const [searchType, setSearchType] = useState('')
    const [card, setCard] = useState(0);

    const search = () =>{
      APIService.search({colors}, {searchTerms})
      .then((response) => 
        newCard(response)
    )
      .catch(error => console.log('error',error))
    }

    const handleSearch=(event)=>{ 
      event.preventDefault()
      search()
    }

    const handleFormChange=(index, event)=>{
        const data = [...searchTerms];
        data[index].value = event.target.value;
        setSearchTerms(data);
    }

    const addFields=(index)=>{
        if(searchType != "-1" && searchType != ""){
            const newField = {type: searchType, value: ''};
            setSearchTerms([...searchTerms, newField])
        }
    }

    const handleColorChange=(event)=>{
        colors[event].checked = !colors[event].checked;
    }

    const removeFields=(index)=>{
        const data = [...searchTerms];
        data.splice(index, 1);
        setSearchTerms(data);
    }

    const renderField = (searchTerm, index) => {
        if (searchTerm.type === 'Rarity') {
            return (
                <select value={searchTerm.value} onChange={event => handleFormChange(index, event)}>
                    <option value="">Select Rarity</option>
                    {rarities.map((rarity, rIdx) => (
                        <option key={rIdx} value={rarity.type}>
                            {rarity.type}
                        </option>
                    ))}
                </select>
            );
        }

        if (searchTerm.type === 'ID Type') {
            return (
                <select value={searchTerm.value} onChange={event => handleFormChange(index, event)}>
                    <option value="=">Equals</option>
                    <option value=">">Greater Than</option>
                    <option value="<">Less Than</option>
                </select>
            );
        }

        return (
            <input
                type="text"
                name={searchTerm.type}
                value={searchTerm.value}
                onChange={event => handleFormChange(index, event)}
            />
        );
    };

    return (
        <div>
            <form onSubmit={handleSearch} >
                <table align="center">
                    {colors.map((obj, index) => (
                        <tbody className="colors" key={index}>
                            <tr>
                                <td>
                                    <Checkbox 
                                        obj={obj}
                                        index={index}
                                        onChange={() => handleColorChange(index)}
                                    />
                                </td>
                            </tr>
                        </tbody>
                    ))}
                </table>
                <table align="center">
                    { searchTerms.length > 0 && searchTerms.map((searchTerm, index) => (
                        <tbody className="searches" key={index}>
                            <tr>
                                <td>
                                    {searchTerm.type}<span>: </span>
                                </td>
                                <td>
                                    {renderField(searchTerm, index)}
                                </td>
                                <td>
                                    <button type="button" onClick={() => removeFields(index)}>Remove</button>
                                </td>
                            </tr>
                        </tbody>
                    ))}
                </table>
                <div>&nbsp;</div>
                <div>Add Search Criteria!</div>
                <select value={searchType} onChange={(e) => setSearchType(e.target.value)}>
                    <option value="-1">Select Search Type</option>
                    {searchTypes.map((type, index) => (
                        <option key={index} value={type.type}>
                            {type.type}
                        </option>
                    ))}
                </select>

                <button type="button" onClick={() => addFields()}>
                    Add Search Term
                </button>
                <div></div>
                <input type="submit" className="w3-button w3-blue" value="Search" />
            </form>
        </div>
    )
}

export default Form;