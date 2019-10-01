import React from 'react';
import {Route, Switch} from 'react-router';
import {BrowserRouter} from 'react-router-dom';

import Main from './containers/main/main';
import Header from './components/header/header';
import TypeList from './components/typeList/typeList'
import ProductsList from './components/productsList/productsList'
import ProductItem from './components/productItem/productItem'
import BasketList from "./components/basketList/basketList";
import TypePost from "./components/typePost/typePost";
import ProductPost from "./components/productPost/productPost";
import Registration from "./components/registration/registration";
import Login from "./components/login/login";
import Profile from "./components/profile/profile";
import OrdersList from "./components/order/prevOrders";


const Routers = () => {
    return (
        <BrowserRouter>
            <Header/>
            <div className='container'>
                <Switch>
                    <Route path='/' exact component={Main}/>
                    <Route path='/catalog' exact component={TypeList} />
                    <Route path='/catalog/:id' exact component={ProductsList}/>
                    <Route path='/registration' component={Registration}/>
                    <Route path='/signin' component={Login}/>
                    <Route path='/profile' component={Profile}/>
                    <Route path='/product/:name' exact component={ProductItem}/>
                    <Route path='/basket' exact component={BasketList}/>
                    <Route path='/new-type' exact component={TypePost}/>
                    <Route path='/new-product' exact component={ProductPost}/>
                    <Route path='/orders' exact component={OrdersList}/>
                </Switch>
            </div>
        </BrowserRouter>
    );
};

export default Routers;