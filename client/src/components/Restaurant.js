function Restaurant(props) {
    return(
        <div className="restaurant">
            <h3>{props.name}</h3>
            <p>{props.rating}</p>
            <p>{props.address}</p>
        </div>
    )
}

export default Restaurant