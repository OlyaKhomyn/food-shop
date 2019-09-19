import React, {Component} from 'react';
import axios from 'axios';
import ProductListItem from '../productListItem/productListItem'

class ProductsList extends Component {
    state = {
        products: [],
        id: this.props.location.state.id
    };

    getData = () => {
        const url = `http://127.0.0.1/product?type=${this.state.id}`;
        axios.get(url, {withCredentials: true}).then(response => {
            this.setState({products:response.data});
        })
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
                            return  <li key={obj['id']}><ProductListItem id={obj['id']} name={obj['name']} price={obj['price']} /></li>
                        })
                    }
                </ul>
            </div>);
    }
}

export default ProductsList;
