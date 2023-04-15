import React, { useState } from 'react';
import type { InputProps } from '../types/types';

const Input = (props: InputProps): JSX.Element => {
  const { onSubmit } = props;
  const [formData, setFormData] = useState({ location: '', date: '' });

  const handleSubmit = (e: any) => {
    e.preventDefault();
    onSubmit(formData);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({ ...prevState, [name]: value }));
  };

  return (
    <>
      <h2>Add a trip to your dashboard</h2>
      <form className="form" onSubmit={handleSubmit}>
        <div className="form-row">
          <label htmlFor="location">Location</label>
          <input
            type="text"
            id="location"
            name="location"
            onChange={handleChange}
          ></input>
        </div>

        <div>
          <label htmlFor="date">Date</label>
          <input
            type="date"
            id="date"
            name="date"
            onChange={handleChange}
          ></input>
        </div>

        <div>
          <input type="submit" value="Add"></input>
        </div>
      </form>
    </>
  );
};

export default Input;
