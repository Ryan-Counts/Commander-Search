import React,{ useState } from 'react';
import APIService from './APIService.jsx'
import Checkbox from './Checkbox.jsx'


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

const Form = (props) => {
    const [colors, setColors] = useState(ColorList.sort((a, b) => a.order - b.order))
    const [searchTerms, setSearchTerms] = useState([])
    const [searchType, setSearchType] = useState('')
    //const [currentSearchFlag, setCurrentSearchFlag] = useState(false);
    const [card, setCard] = useState(0);
    //const [body, setBody] = useState('')
    const [prevCards, setPrevCards] = useState([]);


    const search = () =>{
      APIService.search({colors}, {searchTerms})
      .then((response) => 
        props.setCurrentCard(response),
        setPrevCards([...prevCards, response])
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

    const removeFields=(index)=>{
        const data = [...searchTerms];
        data.splice(index, 1);
        setSearchTerms(data);
        /*if(searchTerms.length == 0){
            setCurrentSearchFlag(false);
        }*/
    }

    return (
        <div>
            <form onSubmit={handleSearch} >
                <table align="center">
                    {colors.map((obj, index) => (
                        <tbody class="colors">
                            <tr key={index}>
                                <td>
                                    <Checkbox obj={obj}/>
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