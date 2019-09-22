import React, { Component } from 'react';
import axios from 'axios';
import { Link } from "react-router-dom";

import './registration.css';

class Registration extends Component {
    state = {
        email: "",
        password: "",
        first_name: "",
        last_name: ""
    };

    validateForm = () => {
        return this.state['email'].length > 0 && this.state['password'].length > 0
            && this.state['first_name'].length > 0 && this.state['last_name'].length > 0;
    };

    handleChange = event => {
        this.setState({
            [event.target.id]: event.target.value
        });
    };

    handleSubmit = event => {
        event.preventDefault();
        if (this.validateForm()) {
            const user = {
                "email": this.state.email,
                "password": this.state.password,
                "first_name": this.state.first_name,
                "last_name": this.state.last_name
            };

            const url = `http://127.0.0.1/users/register`;

            axios.post(url, user, {withCredentials: true, crossDomain: true}
            ).then(response => {
                alert(response.data.message);
                window.location = `http://127.0.0.1:3000/catalog`;
            }).catch(error => {
                alert(alert(error.response.data['error']));
            });
        }
        else {
            alert("Enter all required fields!")
        }
    };

    render() {
        return (
            <div className="Register">
                <div className="align-profile">
                    <label className="users" htmlFor="first_name">First Name:</label>
                    <input id="first_name"
                        className="user-input"
                        type="text"
                        value={this.state.first_name}
                        onChange={this.handleChange}
                    />
                    <label className="users" htmlFor="last_name">Last Name:</label><br />
                    <input id="last_name"
                        className="user-input"
                        type="text"
                        value={this.state.last_name}
                        onChange={this.handleChange}
                    />
                    <label className="users" htmlFor="email">Email:</label><br />
                    <input id="email"
                        className="user-input"
                        type="email"
                        value={this.state.email}
                        onChange={this.handleChange}
                    />
                    <label className="users" htmlFor="password">Password:</label><br />
                    <input id="password"
                        className="user-input"
                        value={this.state.password}
                        onChange={this.handleChange}
                        type="password"
                    />
                </div>
                <input
                    id="users-btn"
                    className="user-input"
                    type="button"
                    onClick={this.handleSubmit}
                    value='Register'
                />
                <hr className="hr-text" data-content="OR">
                </hr>
                <Link className="login-link" to="/signin">I already have an account.</Link>
            </div>
        );
    }
}

export default Registration;
