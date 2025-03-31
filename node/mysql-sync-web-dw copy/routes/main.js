const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
})

// select all rows from st_info table
app.get('/select', (req, res) => {
    let result = connection.query('select * from st_info');
    console.log(result);
    // res.send(result);
    res.writeHead(200);
    var template = `
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Result</title>
    </head>
    <body>
    <table border="1" margin:auto; text-align:center;>
        <tr>
            <th>ST_ID</th>
            <th>NAME</th>
            <th>DEPT</th>
        </tr>   
        `;
        for (var i=0; i<result.length; i++) {
        template += `
        <tr>
            <th>${result[i]['ST_ID']}</th>
            <th>${result[i]['NAME']}</th>
            <th>${result[i]['DEPT']}</th>
        </tr>
        `;
    }
    template += `
    </table>
    </body>
    </html>
    `;
    res.end(template);
})

// insert data to st_info table
app.get('/insert', (req, res) => {
    const { st_id, name, dept } = req.query;
    const result = connection.query("insert into st_info values (?, ?, ?)",
        [st_id, name, dept]);
        res.redirect('/select');
})

// update data to st_info table
app.get('/update', (req, res) => {
    const { st_id, name, dept } = req.query;
    const result = connection.query("update st_info set NAME = ?, DEPT = ? where ST_ID = ?",
        [name, dept, st_id]);
        res.redirect('/select');
})

// delete data from st_info table
app.get('/delete', (req, res) => {
    const st_id= req.query.st_id;
    const result = connection.query("delete from st_info where ST_ID = ?",
        [st_id]);
        res.redirect('/select');
})

module.exports = app;