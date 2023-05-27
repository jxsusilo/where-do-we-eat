function Restaurant(props) {
    return(
        <div className="restaurant">
            <img className="resto-img" src={props.imgsrc}/>
            <div className="resto-info">
                <h3>{props.name}</h3>
                <p>{props.rating}</p>
                <p>{props.address}</p>
            </div>
        </div>
    )
}

export default Restaurant