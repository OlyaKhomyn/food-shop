import React, {Component} from 'react';
import axios from 'axios';
import {Link} from "react-router-dom";
import {withRouter} from "react-router";

class ProductsList extends Component {
    state = {
        products: [],
        id: this.props.location.state.id
    };

    getData = () => {
        // console.log(this.props.match.params.id);
        const url = `http://127.0.0.1:5000/product?type=${this.state.id}`;
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
                        this.state.products.map(obj => (
                            <li key={obj['id']}>
                                <Link
                                    to={
                                        {
                                            pathname: `/${obj['id']}-${obj['name']}`,
                                            state: {id: obj['id']}
                                        }}
                                >
                                    {obj['name']}
                                </Link>
                            </li>))
                    }
                </ul>
            </div>);
    }
}

export default withRouter(ProductsList);
