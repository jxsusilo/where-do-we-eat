function Restaurant(props) {
    return(
        <div className="restaurant">
            <img className="resto-img" src={props.resto.image_url}/>
            <div className="resto-info">
                <h3>{props.resto.name}</h3>
                <p>{props.resto.cuisine}</p>
                <p>{props.resto.rating}</p>
                <p>{props.resto.address}</p>
            </div>
        </div>
    )
}

export default Restaurant