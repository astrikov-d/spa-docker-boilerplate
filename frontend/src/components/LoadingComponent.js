import React from 'react';


export const LoadingComponent = ({isLoading, error}) => {
    if (isLoading) {
        return <p>Loading..</p>;
    } else if (error) {
        return <p>Unable to load requested page.</p>
    } else {
        return null;
    }
};