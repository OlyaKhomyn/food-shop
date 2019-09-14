import React, { Component } from 'react';

import './main.css';

class Main extends Component {

    render () {
      return (
        <div className='main'>
            <h1>What can be better than delicious tasty food?</h1>
            <form className='try_cont' action='/new'>
            <button className=' btn-dark btn-lg text-center try_btn'>Try now</button>
            </form>
        </div>
      );
    }
}

export default Main;
