const Checkbox = ({ obj, index, onChange }) => (
  <label className="color-checkbox">
    <input
      type="checkbox"
      id={`custom-checkbox-${index}`}
      name={obj.name}
      onChange={onChange}
    />
    {obj.name}
  </label>
);

export default Checkbox;