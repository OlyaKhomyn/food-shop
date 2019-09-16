import React, {Component} from 'react';
import {Link} from "react-router-dom";
import {withRouter} from "react-router";

class ProductListItem extends Component {

    state = {
        id: this.props.id,
        name: this.props.name,
        price: this.props.price
    };

    render() {
        return <Link to={
            {
                pathname: `/product/${this.state.id}-${this.state.name}`,
                state: {id: this.state.id}
            }}
        >
            <div>
                <ul>
                    <li>Name: {this.state.name}</li>
                    <li>Price: {this.state.price}</li>
                </ul>
            </div>
        </Link>
    }
}

export default withRouter(ProductListItem);
