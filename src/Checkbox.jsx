const Checkbox = ({obj}) => {

  const onChange = (event) => {
    event.preventDefault();
    obj.checked = !obj.checked;
    obj.name = obj.name;
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