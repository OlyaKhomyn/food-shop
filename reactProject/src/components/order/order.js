import React from 'react'
import axios from 'axios';
import {forEach} from "react-bootstrap/utils/ElementChildren";

class Order extends React.Component {

    constructor(props) {
        super(props);
        this.state ={
            user_id: this.props.user_id,
            products: this.props.products,
            prod_id: undefined,
            total_price:undefined,
            city: undefined,
            department: undefined,
            phone: undefined
        };
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.onChange = this.onChange.bind(this);
    }

    total_price = () => {
        let price = 0;
        let ids = [];
        this.state.products.forEach(el => {
            price += el['amount']*el['price'];
            ids.push(el['id'])
        });
        this.setState({
            total_price: price,
            prod_id: ids
        })
    };

    componentDidMount() {
        this.total_price()
    }

    changeProductsState = () => {
        this.state.products.forEach(el => {
            let data = {
                product_id: el['id'],
                user_id: this.state.user_id,
                amount: el['amount'],
                state: true
            };
            axios.put(`http://127.0.0.1/basket/${el['basket_id']}`, data, {withCredentials:true}).then(response => {
                console.log(response)
            }).catch(er => {
                console.log(er)
            })
        } )
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
        let valid = data.payment_info.city != undefined && data.payment_info.department != undefined && data.payment_info.phone != undefined;
        if (valid) {
            axios.post("http://127.0.0.1/order", data, {withCredentials: true})
                .then((response) => {
                    this.changeProductsState();
                    alert('Order is successfully made!')
                }).catch((error, info) => {
                alert('Incorrect data!')
            });
        }
        else {
            alert("Input all required fields!")
        }
    }
    onChange(e) {
        this.setState({[e.target.name]: e.target.value})
    }

    render() {
        return (
            <form onSubmit={this.onFormSubmit}>
                <h1>Fill in this form, please</h1>
                City
                <input type="text" name="city" value={this.state.city} onChange={this.onChange} />
                <hr />
                Department
                <input type="text" name="department" value={this.state.department} onChange= {this.onChange} />
                <hr />
                Phone
                <input type="text" name="phone" value={this.state.phone} onChange={this.onChange} />
                <hr />
                <p>Total price: {this.state.total_price}</p>
                <hr />
                <button type="submit">Make order</button>
            </form>
        )
    }
}

export default Order;
