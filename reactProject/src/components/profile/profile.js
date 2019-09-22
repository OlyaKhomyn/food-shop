import React, { Component } from "react";
import axios from 'axios';
import cookie from 'react-cookies';



class Profile extends Component {
    state = {
        first_name: "",
        last_name: "",
        email: "",
        role: ""
    };

    componentDidMount() {
        const url = `http://127.0.0.1/users/profile`;
        axios.get(url, { withCredentials:true }).then(response => {
            this.setState({
                first_name:response.data['first_name'],
                last_name:response.data['last_name'],
                email:response.data['email'],
                role: response.data['role_id']
            })
        }
        )

    }

    render() {
        return (
            <div className="Profile">
                <div className="align-profile">
                    <div className="one-value">
                        <label>First Name:</label>
                        <label className="profile-value">{this.state.first_name}</label>
                    </div>

                    <div className="one-value">
                        <label>Last Name:</label>
                        <label className="profile-value">{this.state.last_name}</label>
                    </div>

                    <div className="one-value">
                        <label>Email:</label>
                        <label className="profile-value">{this.state.email}</label>
                    </div>
                    <div className="one-value">
                        <label>Role</label>
                        <label className="profile-value">{this.state.role}</label>
                    </div>

                </div>

            </div>
        );
    }
}

export default Profile;
