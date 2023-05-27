import React, { useEffect, useState } from "react";

function UserInput(props) {
    const [checkedList, setCheckedList] = useState([]);
    const handleSelect = (event) => {
        const value = event.target.value;
        const isChecked = event.target.checked;
     
        if (isChecked) {
          //Add checked item into checkList
          setCheckedList([...checkedList, value]);
        } else {
          //Remove unchecked item from checkList
          const filteredList = checkedList.filter((item) => item !== value);
          setCheckedList(filteredList);
        }
      };

    return (
        <div className="UserInput">
            <h2>{props.name}</h2>
            <div className="card-body">
                {props.listData.map((item, index) => {
                    return (
                    <div key={item.id} className="checkbox-container">
                        <input
                        type="checkbox"
                        value={item.value}
                        onChange={handleSelect}
                        />
                        <label>{item.value}</label>
                    </div>
                    );
                })}
            </div>
        </div>
    )
}

export default UserInput