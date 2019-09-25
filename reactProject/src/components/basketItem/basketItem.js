import React, {Component} from 'react';
import axios from 'axios';
import {Link} from "react-router-dom";
import {withRouter} from "react-router";
import 'react-confirm-alert/src/react-confirm-alert.css';
import { confirmAlert } from 'react-confirm-alert';
class BasketItem extends Component {

    state = {
        productId: this.props.productId,
        productName: this.props.productName,
        productPrice: this.props.productPrice,
        edit: false,
    };

    delete = () => {
        confirmAlert({
            title: 'Confirm to delete',
            message: 'Are you sure you want to delete this field?',
            buttons: [
                {
                    label: 'Yes',
                    onClick: () => {
                        const url = `http://127.0.0.1/basket/${this.props.basketId}`;
                        axios.delete(url, {withCredentials: true}).
                        then(() => {window.location.reload()}).
                        // eslint-disable-next-line no-console
                        catch(error => { console.log(error) });
                    }
                },
                {
                    label: 'No'
                }
                ]
        });
    };

    render() {
        return <div>
            <Link to={
                {
                    pathname: `/product/${this.state.id}-${this.state.productId}`,
                    state: {id: this.state.productId}
                }}
            >
                <li>Name: {this.state.productName}; Price for one: {this.state.productPrice};
                    Amount: {this.props.amount}; Total price: {this.state.productPrice * this.props.amount};</li>
            </Link>
                <div>
                    <button onClick={this.delete} type="button">Remove from basket</button>
                    <button onClick={this.edit} type="button">Edit</button>
                </div>
            </div>
    }
}

export default withRouter(BasketItem);
