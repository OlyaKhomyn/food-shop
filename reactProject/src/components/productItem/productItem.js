import React, {Component} from 'react';
import axios from 'axios';


class ProductItem extends Component {
    state = {
        id: undefined,
        name: undefined,
        amount: undefined,
        price: undefined,
        description: undefined,
        image: undefined
    };

    getData = () => {
        const id = this.props.location.state.id;
        const url = `http://127.0.0.1/product/${id}`;
        axios.get(url, {withCredentials: true}).then(response => {
            const data = response.data;
            this.setState({
                id: id,
                name: data.name,
                price: data.price,
                amount: data.amount,
                description: data.description
            });
        }).then(() => this.getImage())
    };

    componentDidMount() {
        this.getData();
    }

    getImage= () => {
        const url = `http://127.0.0.1/product/${this.state.id}?download=true`;
        axios.get(url, {
            responseType: 'arraybuffer',
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'image/png'
            }
        }).then((response) => {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            this.setState({image:url})
        })
    };

    addToBasket = () => {
        const url = `http://127.0.0.1/basket`;
        let user_id = undefined;
        const auth_status_url = 'http://127.0.0.1/users/profile';
        axios.get(auth_status_url, {withCredentials: true}).
        then(response => {
            user_id = response.data.user_id;
        }).then(response =>
        {
           const data = {
            product_id: this.state.id,
            user_id: user_id,
            amount: 1,
            state: false };
           axios.post(url, data, {withCredentials: true}).then(() => {
            alert('Added to basket.');
        }).catch((error) => {
            alert(error.response.data['error'])
            })
        });
    };

    render() {
        return <div>
            <ul>
                <li>Name: {this.state.name}</li>
                <li>Price: {this.state.price}</li>
                <li>Left: {this.state.amount}</li>
                <li>About: {this.state.description}</li>
                <img src={this.state.image} width='35%' height='35%'/>
            </ul>
            <button onClick={this.addToBasket}>Add to basket</button>
        </div>
    }

}

export  default ProductItem;
