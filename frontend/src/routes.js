import React from 'react';
import {Route, Switch} from 'react-router-dom';
import Loadable from 'react-loadable';

import {LoadingComponent} from './components/LoadingComponent';

import URLS from './urls';

const Dashboard = Loadable({
    loader: () => import('./containers/dashboard/Dashboard'),
    loading: LoadingComponent
});

export const appRoutes = (
    <Switch>
        <Route exact path={URLS.dashboard.index} component={Dashboard}/>
    </Switch>
);
