import React, { Component } from "react";
import axios from 'axios';
import cookie from 'react-cookies';
import { Link } from "react-router-dom";


class Login extends Component {

    state = {
      'email': "",
      'password': ""
    };

    handleChange = event => {
        this.setState({
            [event.target.id]: event.target.value
        });
    }

    handleSubmit = () => {
        const user = {
          "email": this.state.email,
          "password": this.state.password
        };

        const url = `http://127.0.0.1/users/login`;

        axios.post(url, user, { withCredentials:true, crossDomain: true }
        ).then(res =>
            window.location = 'http://127.0.0.1:3000/catalog'
        ).catch( error => {

        });
    };


    componentWillMount() {
        if (cookie.load('error')) {
            alert(cookie.load('error'));
            cookie.remove('error', { path: '/' });
        }
    }


    render() {
        return (
            <div className="Login">
                <div className="align-profile">
                    <hr />
                    <label className="users" htmlFor="email">Email: </label>
                    <input id="email"
                        className="user-input"
                        type="email"
                        value={this.state['email']}
                        onChange={this.handleChange}
                    />
                    <hr />
                    <label className="users" htmlFor="password">Password: </label>
                    <input id="password"
                        className="user-input"
                        value={this.state['password']}
                        onChange={this.handleChange}
                        type="password"
                    />
                </div>
                <hr />
                <input
                    id="users-btn"
                    className="user-input"
                    type="button"
                    onClick={this.handleSubmit}
                    value='Sign in'
                />

                <Link className="login-link" to="/registration">I am not signed up yet.</Link>
            </div>
        );
    }
}

export default Login;
