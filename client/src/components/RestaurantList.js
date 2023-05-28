import Restaurant from "./Restaurant";

function RestaurantList(props) {
    return (
        <div className="card-body">
            {props.listData.map((item, index) => {
                return (
                    <Restaurant resto={item} key={item.name}/>
                );
            })}
        </div>
    )
}

export default RestaurantList