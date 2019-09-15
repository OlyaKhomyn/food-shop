import React, {Component} from 'react';
import axios from 'axios';
import {Link, withRouter} from "react-router-dom";

class TypeList extends Component {

    state = {
        types: []
    };

    getData = () => {
        const url = 'http://127.0.0.1:5000/type';
        axios.get(url, {withCredentials:true}).then(response => {
            this.setState({types:response.data});
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
                        this.state.types.map(obj => (
                            <li key={obj['id']}>
                                <Link
                                    to={
                                        {
                                            pathname: `/catalog/${obj['type']}`,
                                            state: {id: obj['id']}
                                        }}
                                >
                                    {obj['type']}
                                </Link>
                            </li>))
                    }
                </ul>
            </div>
        );
    }

}

export default withRouter(TypeList)
