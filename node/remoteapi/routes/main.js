const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const CircularJSON = require('circular-json');
const request= require('request');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

let urls = '';

app.get('/Hello', (req, res) => {
    urls = 'http://13.125.182.26:8000/Hello';
    request(urls, {json:true}, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    })
})

// request X, response O
app.get('/api/users', (req, res) => {
    axios
        .get('http://13.125.182.26:8000/api/users')
        .then(result => {
            res.json({ok: true, users: result.data.users})
        })
        .catch(error => {
            console.log(error);
        })
})

// query string, request O, response O
app.get('/api/users/user', (req, res) => {
    if (req.query.name == null) {
        urls = 'http://13.125.182.26:8000/api/users/user?id=' + req.query.id;
    } else {
        urls = 'http://13.125.182.26:8000/api/users/user?id=' + req.query.id + '&name=' + req.query.name; 
    }

    request(urls, { json: true }, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    });
});

// query params(path param), request O, response O
app.get('/api/users/:id', (req, res) => {
    urls = 'http://13.125.182.26:8000/api/users/user?id=' + req.params.id;

    request(urls, { json: true }, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    });
})

// post, request body O, response O
app.post('/api/users/userBody', (req, res) => {
    const option = {
        uri : 'http://13.125.182.26:8000/api/users/userBody',
        method : 'POST',
        form : { id : req.body.id },
    };
    request.post(option, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    })
})

// post, request body O, response O
app.post('/api/users/add', (req, res) => {
    const option = {
        uri : 'http://13.125.182.26:8000/api/users/add',
        method : 'POST',
        form : { id : req.body.id, name: req.body.name },
    };
    request.post(option, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    })
})

// put, request body O, response O
app.put('/api/users/update', (req, res) => {
    const option = {
        uri : 'http://13.125.182.26:8000/api/users/update/',
        method : 'PUT',
        form : { id : req.body.id, name: req.body.name },
    };
    request.put(option, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    })
})

// patch, request params & body O, response O
app.patch('/api/users/update/:id', (req, res) => {
    const option = {
        uri : 'http://13.125.182.26:8000/api/users/update/' + req.params.id,
        method : 'PATCH',
        form : { name: req.body.name },
    };
    request.patch(option, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    })
})

// delete, request body O, response O
app.delete('/api/users/delete', (req, res) => {
    const option = {
        uri : 'http://13.125.182.26:8000/api/users/delete/',
        method : 'DELETE',
        form : { id: req.body.id },
    };
    request.delete(option, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    })
})

module.exports = app;