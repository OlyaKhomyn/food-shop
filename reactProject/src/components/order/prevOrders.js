import React from 'react'
import axios from 'axios';
import {forEach} from "react-bootstrap/utils/ElementChildren";
import qs from "qs";

class OrdersList extends React.Component {

    constructor(props) {
        super(props);
        this.state ={
            user: undefined,
            products: [],
            basket: undefined
        };
    }


    componentDidMount() {
        const user_url = `http://127.0.0.1/users/profile`;
        axios.get(user_url, {withCredentials: true}).then(response => {
            this.setState({user: response.data['user_id']});
        }).then(() => {
            const url = `http://127.0.0.1/basket?user_id=${this.state.user}&state=true`;
            axios.get(url, {withCredentials: true}).then(response => {
                this.setState({basket:response.data});
            }).then(() => {this.getProducts()})
        });
    }

    getAmount = () => {
        let {products} = this.state;
        for (let i in this.state.products)
        {
            for (let j in this.state.basket)
            {
                if (this.state.basket[j]['product_id'] == this.state.products[i]['id'])
                {
                    products[i]['amount'] = this.state.basket[j]['amount'];
                }
            }
        }
        this.setState({products})
    };

    getProducts = () => {
        const ids = this.state.basket.map(el => el['product_id']);
        axios.get('http://127.0.0.1/product', {
            withCredentials:true,
            params: {
                'product_id': ids
            },
            paramsSerializer: params => {
                return qs.stringify(params, {arrayFormat: 'repeat'});
            }
        }).then(response => {
            this.setState({products: response.data})}).then(()=>this.getAmount())
    };


    onFormSubmit(e){
        e.preventDefault();
        let data = {
            user_id: this.state.user_id,
            products: this.state.prod_id,
            total_price: this.state.total_price,
            payment_info: {
                city: this.state.city,
                department: this.state.department,
                phone: this.state.phone,
                user_id: this.state.user_id
            }
        };
        axios.post("http://127.0.0.1/order", data, {withCredentials:true})
            .then((response) => {
                this.changeProductsState();
                alert('Order is successfully made!')
            }).catch((error, info) => {
                alert('Incorrect data!')
        });
    }


    render() {
        return (
            <ul>
                {
                    this.state.products.map(el => {
                        return <li>Name: {el['name']}; Price for one: {el['price']};
                    Amount: {el['amount']}; Total price: {el['price'] * el['amount']};</li>
                    })
                }
            </ul>
        )
    }
}

export default OrdersList;
