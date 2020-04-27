import axios from 'axios';

export const apiURL = `http://${process.env.REACT_APP_API_HOST}`;

const api = axios.create({
    baseURL: `${apiURL.trim('/')}/api/`,
    timeout: 600000
});

api.interceptors.request.use((config) => {
    const user = JSON.parse(localStorage.getItem('user')) || {};

    if (user.token) {
        const headers = {
            ...config.headers,
            Authorization: 'Token ' + user.token,
        };
        return {...config, headers};
    }

    return config;
});

export default api;
