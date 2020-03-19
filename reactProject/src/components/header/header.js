import React, {Component} from 'react';
import { Link } from "react-router-dom";
import cookie from 'react-cookies';
import axios from 'axios';
import './header.css';


class Header extends Component {

    state = {
        element1: <Link className="nav-link nav-text" to="/registration">Sign up</Link>,
        element2: <Link className="nav-link nav-text" to="/signin">Sign in</Link>,
        element3: undefined,
        element4: undefined,
        element5: undefined,
        element6: undefined
    };

    componentDidMount() {
        let condition = cookie.load("session") != undefined;
        console.log(cookie.load("session"))
        let isAdmin = cookie.load("admin") == "True";
        if (isAdmin && condition)
        {
            this.setState({
                element1: <Link className="nav-link nav-text" to="/profile">Profile</Link>,
                element2: <Link className="nav-link nav-text" to="#" onClick={this.signOut}>Sign out</Link>,
                element3: <Link className="nav-link nav-text" to="/catalog">Catalog</Link>,
                element4: <Link className="nav-link nav-text" to="/new-type">New Type</Link>,
                element5: <Link className="nav-link nav-text" to="/new-product">New Product</Link>,
                element6: <Link className="nav-link nav-text" to="/new-action">Actions</Link>
            });
        } else if (condition)
        {
            this.setState({
                element1: <Link className="nav-link nav-text" to="/profile">Profile</Link>,
                element2: <Link className="nav-link nav-text" to="#" onClick={this.signOut}>Sign out</Link>,
                element3: <Link className="nav-link nav-text" to="/catalog">Catalog</Link>,
                element4:  <Link className="nav-link nav-text" to="/basket">Basket</Link>,
                element5: <Link className="nav-link nav-text" to="/orders">Orders</Link>
            });
        } else {
            this.setState({
                element1: <Link className="nav-link nav-text" to="/registration">Sign up</Link>,
                element2: <Link className="nav-link nav-text" to="/signin">Sign in</Link>
            });
        }
    }

    signOut = () => {
        const url = `http://127.0.0.1/users/logout`;
        let signout = confirm("Sure you want to sign out?");
        if (signout){
            axios.post(url,  { withCredentials:true }
            ).then( () => {
                cookie.remove('session', { path: '/' });
                cookie.remove('admin', { path: '/' });
                window.location = `http://127.0.0.1:3000/signin`;
            });
        }
    };

    render() {
        return (
            <div className="header">
                <nav className='navbar fixed-top navbar-expand-lg'>
                    <button className="navbar-toggler" type="button" data-toggle="collapse"
                            data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                            aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"/>
                    </button>
                    <span className="collapse navbar-collapse" id="navbarSupportedContent">
                    <div className="left-nav-items">
                        <ul className="navbar-nav ml-auto">
                            <li className="nav-item">
                                {this.state.element3}
                            </li>
                            <li className="nav-item">
                                {this.state.element4}
                            </li>
                            <li className="nav-item">
                                {this.state.element5}
                            </li>
                            <li className="nav-item">
                                {this.state.element6}
                            </li>
                        </ul>
                    </div>
                        <div className='right-nav-items'>
                        <ul className="navbar-nav">
                            <li className="nav-item active">
                                {this.state.element1}
                            </li>
                            <li className="nav-item active">
                                {this.state.element2}
                            </li>
                        </ul>
                    </div>
                    </span>
                </nav>
            </div>
        );
    }
}

export default Header;
