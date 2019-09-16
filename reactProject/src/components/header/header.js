import React, {Component} from 'react';
import { Link } from "react-router-dom";
import './header.css';


class Header extends Component {

    state = {
        element3: undefined,
        element4: undefined
    };

    componentWillMount() {
        this.setState({
                element3: <Link className="nav-link nav-text" to="/catalog">Catalog</Link>,
                element4: <Link className="nav-link nav-text" to="/basket">Basket</Link>
            });
    }

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
                        </ul>
                    </div>
                    </span>
                </nav>
            </div>
        );
    }
}

export default Header;
