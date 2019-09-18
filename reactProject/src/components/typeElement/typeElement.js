import React, {Component} from 'react';
import {Link} from "react-router-dom";
import {withRouter} from "react-router";
import axios from 'axios';
import Image from "react-bootstrap/Image";


class TypeElement extends Component {

    state = {
        id: this.props.id,
        type: this.props.type,
        image: undefined
    };

    getImage= () => {
        const url = `http://127.0.0.1:5000/type/${this.state.id}?download=true`;
        axios.get(url, {
            responseType: 'arraybuffer',
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'image/png'
            }
        }).then((response) => {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            this.setState({image:url})
        })
    };

    componentDidMount() {
        this.getImage()
    }


    render() {
        return <div><Link to={
            {
                pathname: `/catalog/${this.state.type}`,
                state: {id: this.state.id}
            }}
        >
            {this.state.type}
            <img src={this.state.image} width='35%' height='35%'/>
        </Link>
        </div>
    }
}

export default withRouter(TypeElement);