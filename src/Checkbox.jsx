const Checkbox = ({obj, index, onChange}) => {

  const handleOnChange = (event) => {
    event.preventDefault();
    onChange(index, event);
  }

  return (
    <>
      <input 
        type="checkbox"
        id={'custom-checkbox-${obj.index}'}
        name={obj.name}
        value={obj.checked}
        onChange={onChange}
      />
    {obj.name}
    </>
  )
};

export default Checkbox;