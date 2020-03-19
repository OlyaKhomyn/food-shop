import React, {Component} from 'react';
import axios from 'axios';


class ProductItem extends Component {
    state = {
        id: undefined,
        name: undefined,
        amount: undefined,
        price: undefined,
        new_price: undefined,
        description: undefined,
        image: undefined,
        to_basket: 1
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
                new_price: data.new_price,
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
            if (Number.isInteger(Number(this.state.to_basket)))
            {
                const data = {
                product_id: this.state.id,
                user_id: user_id,
                amount: this.state.to_basket,
                state: false };
                axios.post(url, data, {withCredentials: true}).then(() => {
                    alert('Added to basket.');
                }).catch((error) => {
                    alert(error.response.data['error'])
                })
            }
            else {
                alert("Amount should be an integer!")
            }
        });
    };

    changeAmount = (event) => {
        this.setState({to_basket: event.target.value})
    };

    render() {
        return <div>
            <ul>
                <li>Name: {this.state.name}</li>
                <li>Price: {this.state.price}</li>
                {this.state.new_price && <li>Discount!! New price: {this.state.new_price}</li>}
                <li>Left: {this.state.amount}</li>
                <li>About: {this.state.description}</li>
                <img src={this.state.image} width='35%' height='35%'/>
            </ul>
            <br/>
            Amount
            <input type="text" onChange={this.changeAmount} value={this.state.to_basket} />
            <br />
            <button onClick={this.addToBasket}>Add to basket</button>
        </div>
    }

}

export  default ProductItem;
