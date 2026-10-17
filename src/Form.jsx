import React,{ useState } from 'react';
import APIService from './APIService.jsx'
import AutocompleteSet from './AutocompleteSet.jsx'
import AutocompleteArtist from './AutocompleteArtist.jsx'


const searchTypes = [
    {
        type: 'Colors'
    },
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
    },
    {
        type: 'Set'
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
    const [error, setError] = useState('');

    const search = () => {
        const colorTerm = searchTerms.find((t) => t.type === 'Colors');
        const selected = colorTerm ? colorTerm.value : [];
        const colorsForApi = colors.map((c) => ({ ...c, checked: selected.includes(c.name) }));
        const otherTerms = searchTerms.filter((t) => t.type !== 'Colors');

        setError('');
        APIService.search({ colors: colorsForApi }, { searchTerms: otherTerms })
            .then((response) => newCard(response))
            .catch((err) => setError(err.message));
    };

    const handleSearch=(event)=>{ 
      event.preventDefault()
      search()
    }

    const handleFormChange = (index, event) => {
    setSearchTerms(searchTerms.map((term, i) =>
        i === index ? { ...term, value: event.target.value } : term
        ));
    };

    const addFields = () => {
        if (searchType === '' || searchType === '-1') return;
        if (searchType === 'Colors' && searchTerms.some((t) => t.type === 'Colors')) return;

        const value = searchType === 'Colors' ? [] : '';
        setSearchTerms([...searchTerms, { type: searchType, value }]);
    };

    const toggleColor = (index, name) => {
        setSearchTerms(searchTerms.map((term, i) => {
            if (i !== index) return term;
            const selected = term.value.includes(name);
            return {
                ...term,
                value: selected
                    ? term.value.filter((n) => n !== name)
                    : [...term.value, name],
            };
        }));
    };

    const removeFields=(index)=>{
        const data = [...searchTerms];
        data.splice(index, 1);
        setSearchTerms(data);
    }

    const renderField = (searchTerm, index) => {

        if (searchTerm.type === 'Colors') {
            return (
                <div className="color-picker">
                    {colors.map((c) => {
                        const selected = searchTerm.value.includes(c.name);
                        return (
                            <button
                                type="button"
                                key={c.name}
                                className={`color-chip color-${c.name.toLowerCase()}${selected ? ' selected' : ''}`}
                                aria-pressed={selected}
                                aria-label={c.name}
                                title={c.name}
                                onClick={() => toggleColor(index, c.name)}
                            >
                                {c.name === 'Blue' ? 'U' : c.name[0]}
                            </button>
                        );
                    })}
                </div>
            );
        }

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

        if (searchTerm.type === 'Set') {
            return (
                <AutocompleteSet 
                    index={index}
                    onChange={event => handleFormChange(index, event)}
                />
            );
        }

        if (searchTerm.type === 'Artist') {
            return (
                <AutocompleteArtist 
                    index={index}
                    onChange={event => handleFormChange(index, event)}
                />
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
                <div className="search-list">
                    {searchTerms.map((searchTerm, index) => (
                        <div
                            className={`search-term${searchTerm.type === 'Colors' ? ' search-term-colors' : ''}`}
                            key={index}
                        >
                            <span className="search-term-label">{searchTerm.type}:</span>
                            <div className="search-term-field">
                                {renderField(searchTerm, index)}
                            </div>
                            <button type="button" onClick={() => removeFields(index)}>Remove</button>
                        </div>
                    ))}
                </div>
                <div>&nbsp;</div>
                <div>Add Search Criteria!</div>
                <div className='add-term'>
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
                </div>
                <div></div>
                {error && <p className="search-error" role="alert">{error}</p>}
                <input type="submit" className="w3-button w3-blue" value="Search" />
            </form>
        </div>
    )
}

export default Form;