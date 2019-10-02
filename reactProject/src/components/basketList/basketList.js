import React, {Component} from 'react';
import axios from 'axios';
import qs from 'qs';
import BasketItem from '../basketItem/basketItem'
import Order from "../order/order";

class BasketList extends Component {
    state = {
        user: undefined,
        basket: [],
        products: null,
        buy: false
    };

    getData = () => {
        const user_url = `http://127.0.0.1/users/profile`;
        axios.get(user_url, {withCredentials: true}).then(response => {
            this.setState({user: response.data['user_id']});
        }).then(() => {
            const url = `http://127.0.0.1/basket?user_id=${this.state.user}&state=false`;
            axios.get(url, {withCredentials: true}).then(response => {
                this.setState({basket:response.data});
            }).then(() => {this.getProducts()})
        });
    };

    getAmount = () => {
        let {products} = this.state;
        for (let i in this.state.products)
        {
            for (let j in this.state.basket)
            {
                if (this.state.basket[j]['product_id'] == this.state.products[i]['id'])
                {;
                    if (products[i]['new_price'])
                    {
                        products[i]['price'] = products[i]['new_price']
                    }
                    products[i]['amount'] = this.state.basket[j]['amount'];
                    products[i]['basket_id'] = this.state.basket[j]['id']
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

    componentWillMount() {
        this.getData()
    }

    order = () => {
        this.setState({
            buy: !this.state.buy})
    };

    render() {
        return (
        <div>
            {
                this.state.products && this.state.products.map(obj => {
                    return <BasketItem basketId={obj['basket_id']} productId={obj['id']} productName={obj['name']}
                                       productPrice={obj['price']} amount={obj['amount']} />
                }) || "No element in basket"
            }
            <hr />
            { this.state.products && <button onClick={this.order} type="button">Buy</button>}
            {
                this.state.buy  && <Order products={this.state.products} user_id={this.state.user} />
            }
        </div>);
    }
}

export default BasketList;
