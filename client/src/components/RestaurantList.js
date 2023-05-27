import Restaurant from "./Restaurant";

function RestaurantList(props) {
    return (
        <div className="card-body">
            {props.listData.map((item, index) => {
                return (
                    <Restaurant name={item.name} rating={item.rating} address={item.address} />
                );
            })}
        </div>
    )
}

export default RestaurantList