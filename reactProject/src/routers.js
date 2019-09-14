import React from 'react';
import {Route, Switch} from 'react-router';
import {BrowserRouter} from 'react-router-dom';

import Main from './containers/main/main';
import Header from './components/header/header';

const Routers = () => {
    return (
        <BrowserRouter>
            <Header/>
            <div className='container'>
                <Switch>
                    <Route path='/' exact component={Main}/>

                </Switch>
            </div>
        </BrowserRouter>
    );
};

export default Routers;