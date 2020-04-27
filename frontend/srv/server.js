'use strict';

const express = require('express');
const path = require('path');
const fs = require('fs');

const buildPath = path.join(__dirname, 'build');

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express();

app.get('/favicon.ico', function (req, res) {
    const filePath = path.join(buildPath, 'favicon.ico');

    res.sendFile(filePath);
});

app.get('/manifest.json', function (req, res) {
    const filePath = path.join(buildPath, 'manifest.json');

    res.sendFile(filePath);
});

app.use('/static', express.static(path.join(buildPath, 'static')));

app.get('*', (req, res) => {
    const filePath = path.join(buildPath, 'index.html');

    fs.readFile(filePath, {encoding: 'utf-8'}, (err, data) => {
        if (!err) {
            res.send(data);
        }
    });
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
