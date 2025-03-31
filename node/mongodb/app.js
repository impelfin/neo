const express = require('express');
const morgan = require('morgan');
const fs = require('fs');
const path = require('path');
const mongoClient = require('mongodb').MongoClient;

const app = express();
app.set('port', process.env.Port || 8000);
app.use(morgan('dev'));

var db;
var databaseUrl = 'mongodb://192.168.1.34:27017';

app.get('/', (req, res) => {
    res.send('Web Server Started~!!')
})

app.get('/things', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, client) {
        if (err != null) {
            res.json({'count' : 0})
        } else {
            db = client.db('test');
            db.collection('things').find({}).toArray(function (err, result) {
                if (err) throw err
                    console.log('result : ');
                    console.log(result);
                    res.json(JSON.stringify(result));
            })
        }
    })
})

app.get('/emp', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, client) {
        if (err != null) {
            res.json({'count' : 0})
        } else {
            db = client.db('test');
            db.collection('emp').find({}).toArray(function (err, result) {
                if (err) throw err
                    console.log('result : ');
                    console.log(result);
                    res.json(JSON.stringify(result));
            })
        }
    })
})

app.get('/primer', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, client) {
        if (err != null) {
            res.json({'count' : 0})
        } else {
            db = client.db('test');
            db.collection('primer').find({}).toArray(function (err, result) {
                if (err) throw err
                    console.log('result : ');
                    console.log(result);
                    res.json(JSON.stringify(result));
            })
        }
    })
})

app.listen(app.get('port'), function () {
    console.log("Server is Started~!! " + app.get('port'));
});

