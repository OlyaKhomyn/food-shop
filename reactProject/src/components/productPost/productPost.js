import React from 'react'
import axios from 'axios';


class ProductPost extends React.Component {

    constructor(props) {
        super(props);
        this.state ={
            file: null,
            name: undefined,
            price: undefined,
            amount: undefined,
            type: undefined,
            description: undefined
        };
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.onChange = this.onChange.bind(this);
    }
    onFormSubmit(e){
        e.preventDefault();
        const formData = new FormData();
        formData.append('photo',this.state.file);
        formData.append('name',this.state.name);
        formData.append('price',this.state.price);
        formData.append('amount',this.state.amount);
        formData.append('type',this.state.type);
        formData.append('description',this.state.description);
        const config = {
            headers: {
                'content-type': 'image/png'
            }
        };

        axios.post("http://127.0.0.1/product",formData,config)
            .then((response) => {
                alert("The product is successfully uploaded");
            }).catch((error) => {
                console.log(error.response);
                if (error.response.data['error'] != undefined)
                {
                    alert(error.response.data['error'] + "\nIt must be either .png or .jpg")
                }
                else {
                    alert("Input all required fields")
                }
        });
    }
    onChange(e) {
        this.setState({file:e.target.files[0]});
    }

    setValue = (e) => {
        this.setState({[e.target.name]: e.target.value})
    };

    render() {
        return (
            <form onSubmit={this.onFormSubmit}>
                <h1>New product</h1>
                Name
                <input type="text"  name="name" value={this.state.name} onChange={this.setValue} />
                <hr />
                Price
                <input type="text"  name="price" value={this.state.price} onChange={this.setValue} />
                <hr />
                Amount
                <input type="text"  name="amount" value={this.state.amount} onChange={this.setValue} />
                <hr />
                Type
                <input type="text"  name="type" value={this.state.type} onChange={this.setValue} />
                <hr />
                Description
                <textarea  name="description" value={this.state.description} onChange={this.setValue} />
                <hr />
                <input type="file" name="myImage" onChange= {this.onChange} />
                <hr />
                <button type="submit">Add product</button>
            </form>
        )
    }
}


export default ProductPost;
