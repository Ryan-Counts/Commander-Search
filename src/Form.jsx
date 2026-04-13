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

    return (
        <div>
            <form onSubmit={handleSearch} >
                <table align="center">
                    {colors.map((obj, index) => (
                        <tbody class="colors">
                            <tr key={index}>
                                <td>
                                    <Checkbox 
                                        obj={obj}
                                        index={index}
                                        onChange={event => handleColorChange(index, event)}
                                    />
                                </td>
                            </tr>
                        </tbody>
                    ))}
                </table>
                <table align="center">
                    { searchTerms.length > 0 && searchTerms.map((searchTerm, index) => (
                        <tbody class="searches">
                            <tr key={index}>
                                <td>
                                    {searchTerm.type}<span>: </span>
                                </td>
                                <td>
                                    {searchTerm.type != 'Rarity' ? (
                                        <input
                                            type="text"
                                            name={searchTerm.type}
                                            value={searchTerm.value}
                                            onChange={event => handleFormChange(index, event)}/>) 
                                        : (
                                            <select value={searchTerm.value} onChange={event => handleFormChange(index, event)}>
                                                <option value="">Select Rarity</option>
                                                {rarities.map((rarity, index) => (
                                                    <option key={index} value={rarity.type}>
                                                        {rarity.type}
                                                    </option>
                                                ))}
                                            </select>
                                    )}
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

                <button type="button" onClick={() => addFields(searchType.index)}>
                    Add Search Term
                </button>
                <div></div>
                <input type="submit" className="w3-button w3-blue" value="Search" />
            </form>
        </div>
    )
}

export default Form;