import React from 'react'
import axios from 'axios';
import Select from 'react-select';
import ActionItem from "./actionItem";

const colourStyles = {
  control: styles => ({ ...styles, backgroundColor: 'white' }),
  option: (styles) => {
    return {
      ...styles,
      backgroundColor: '#ff9966'
    };
  },
};


class ActionPost extends React.Component {

    constructor(props) {
        super(props);
        this.state ={
            discount: undefined,
            valid_to: undefined,
            typeNames: undefined,
            selectedOption: undefined,
            ids: undefined,
            products: undefined,
            actions: []
        };
        this.onFormSubmit = this.onFormSubmit.bind(this);
    }

    addDiscountToTypes = () => {
        this.state.ids.forEach(el => {
            axios.get(`http://127.0.0.1/product?type=${el}`, {withCredentials:true}).then(response => {
                this.setState({products: response.data})
            }).then(() => {
                this.state.products.forEach(el => {
                    axios.patch(`http://127.0.0.1/product/${el['id']}`,
                        {"new_price": el['price']-el['price']*(this.state.discount/100)},
                        {withCredentials:true}).catch(er=>console.log(er))
                })
            })
        })
    };

    onFormSubmit(e){
        e.preventDefault();
        let data = {
            discount:  this.state.discount,
            type_ids: this.state.ids,
            valid_to: this.state.valid_to
        };
        axios.post("http://127.0.0.1/action",data,{withCredentials: true}).
        then(() => {
                this.addDiscountToTypes();
                alert("The action is successfully uploaded");
        }).catch((error) => { });
    }

    componentDidMount() {
        this.getAllActions();
        this.getTypes();
    }

    getAllActions = () => {
        axios.get('http://127.0.0.1/action', {withCredentials:true}).then(response => {
            this.setState({actions: response.data});
        })
    };

    getTypes = () => {
        const types = `http:///127.0.0.1/type`;
        axios.get(types, {withCredentials: true}
        ).then(response => {
            let type = response.data;
            let names = type.map(el => {
                return {value: el['id'], label: el['type']}
            });
            let ids = names.map(el => el['value']);
            this.setState({typeNames: names, ids: ids});
        });
    };

    setValue = (e) => {
        this.setState({[e.target.name]: e.target.value})
    };

    handleChange = (selectedOption) => {
        this.setState({selectedOption});
    };

    render() {
        return (
            <div>
                <form onSubmit={this.onFormSubmit}>
                    <h1>New action</h1>
                    Discount value
                    <input type="text"  name="discount" value={this.state.discount} onChange={this.setValue} />
                    <hr />
                    <label>Add types:</label>
                                <Select
                                    styles={colourStyles}
                                    options={this.state.typeNames}
                                    onChange={this.handleChange}
                                    isMulti
                                />
                    <hr />
                    Valid to
                    <input type="date"  name="valid_to" value={this.state.valid_to} onChange={this.setValue} />
                    <hr />
                    <button type="submit">Add discount</button>
                </form>
                <div>{
                    this.state.actions.map(el => {
                        console.log(el) ;
                        return <ActionItem key={el['id']} id={el['id']} discount={el['discount']}
                                                                 type_ids={el['type_ids']}
                                                                 valid_to={el['valid_to']} />})
                }
                </div>
            </div>
        )
    }
}


export default ActionPost;
