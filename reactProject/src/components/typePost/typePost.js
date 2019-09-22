import React from 'react'
import axios from 'axios';

class TypePost extends React.Component {

    constructor(props) {
        super(props);
        this.state ={
            file: null,
            type_name: undefined
        };
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.onChange = this.onChange.bind(this);
    }
    onFormSubmit(e){
        e.preventDefault();
        const formData = new FormData();
        formData.append('photo',this.state.file);
        console.log(this.state.type_name);
        formData.append('type',this.state.type_name);
        const config = {
            headers: {
                'content-type': 'image/png'
            }
        };

        axios.post("http://127.0.0.1/type",formData,config)
            .then((response) => {
                alert("The file is successfully uploaded");
            }).catch((error) => {
                console.log(error)
        });
    }
    onChange(e) {
        this.setState({file:e.target.files[0]});
    }

    setTypeName = (e) => {
        this.setState({type_name: e.target.value})
    };

    render() {
        return (
            <form onSubmit={this.onFormSubmit}>
                <h1>New type of product</h1>
                <input type="text"  onChange={this.setTypeName} />
                <hr />
                <input type="file" name="myImage" onChange= {this.onChange} />
                <hr />
                <button type="submit">Add type</button>
            </form>
        )
    }
}

export default TypePost;
