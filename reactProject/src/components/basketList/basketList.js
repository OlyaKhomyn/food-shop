import React, {Component} from 'react';
import axios from 'axios';
import qs from 'qs';

class BasketList extends Component {
    state = {
        user: undefined,
        basket: [],
        products: []
    };

    getData = () => {
        const user_url = `http://127.0.0.1/users/profile`;
        axios.get(user_url, {withCredentials: true}).then(response => {
            this.setState({user: response.data['user_id']});
            console.log(response.data['user_id'])
        }).then(() => {
            const url = `http://127.0.0.1/basket?user_id=${this.state.user}&state=false`;
            axios.get(url, {withCredentials: true}).then(response => {
                this.setState({basket:response.data});
            }).then(() => this.getProducts())
        });
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
        }).then(response => this.setState({products: response.data}))
    };

    componentDidMount() {
        this.getData()
    }

    render() {
        return (
        <div>
                <ul>
                    {
                        this.state.products.map(obj => {
                            return  <li key={obj['id']}> {obj['name']}  {obj['price']}</li>
                        })
                    }
                </ul>
            </div>);
    }
}

export default BasketList;
