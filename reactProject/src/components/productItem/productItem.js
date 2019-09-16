import React, {Component} from 'react';
import axios from 'axios';


class ProductItem extends Component {
    state = {
        id: undefined,
        name: undefined,
        amount: undefined,
        price: undefined,
        description: undefined
    };

    getData = () => {
        const id = this.props.location.state.id;
        const url = `http://127.0.0.1:5000/product/${id}`;
        axios.get(url, {withCredentials: true}).then(response => {
            const data = response.data;
            this.setState({
                id: id,
                name: data.name,
                price: data.price,
                amount: data.amount,
                description: data.description
            });
        })
    };

    componentDidMount() {
        this.getData();
    }

    addToBasket = () => {
        const url = `http://127.0.0.1:5050/basket`;
        const data = {
            product_id: this.state.id,
            user_id: 1,
            amount: 1,
            state: false
        };
        axios.post(url, data, {withCredentials: true}).then(() => {
            alert('Success');
        }).catch(() => alert('Something wrong'))
    };

    render() {
        return <div>
            <ul>
                <li>Name: {this.state.name}</li>
                <li>Price: {this.state.price}</li>
                <li>Left: {this.state.amount}</li>
                <li>About: {this.state.description}</li>
            </ul>
            <button onClick={this.addToBasket}>Add to basket</button>
        </div>
    }

}

export  default ProductItem;
