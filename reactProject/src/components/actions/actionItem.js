import React, {Component} from 'react';
import axios from 'axios';


class ActionItem extends Component {

    delete = () => {
        axios.delete(`http://127.0.0.1/action/${this.props.id}`, {withCredentials: true}).
        then(() => {
            alert("Action cancelled");
            window.location.reload()
        })
            .catch(er=>console.log(er));
        this.props.type_ids.forEach(el => axios.patch(
            `http://127.0.0.1/product/${el}`,
            {"new_price": null},
            {withCredentials:true})
        )
    };

    render() {
        return <div>
            Discount: {this.props.discount}%; Valid to: {this.props.valid_to};
            <button onClick={this.delete} type="button">Cancel action</button>
        </div>
    }

}

export  default ActionItem;
