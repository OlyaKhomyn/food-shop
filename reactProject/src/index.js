import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './app.css';
import Routers from "src/routers";

const app = (
    <div>
        <Routers />
    </div>
);

ReactDOM.render(app, document.getElementById('root'));
