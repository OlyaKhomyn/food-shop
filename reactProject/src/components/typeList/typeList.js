import React, {Component} from 'react';
import axios from 'axios';
import {Link, withRouter} from "react-router-dom";
import TypeElement from "../typeElement/typeElement"
import {element} from "prop-types";

class TypeList extends Component {

    state = {
        types: []
    };

    getData = () => {
        const url = 'http://127.0.0.1/type';
        axios.get(url, {withCredentials:true, }).then(response => {
            // console.log(response.data);
            this.setState({types:response.data});
        })
    };

    componentDidMount() {
        this.getData()
    }


    render() {
        return (
            <div>
                {
                    // console.log(this.state.types)
                    // this.state.types.map(element => console.log(element))
                    this.state.types.map(obj => <TypeElement id={obj['id']} type={obj['type']} />)
                }
            </div>
        );
    }

}

export default withRouter(TypeList)
