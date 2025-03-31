const express = require('express');
const bodyParser = require('body-parser');
const pool = require('../../conf/pool')

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
})

// select all rows from st_info table
app.get('/select', async (req, res) => {
    const [rows] = await pool.query('select * from st_info');
    console.log(rows);
    res.send(rows);
})

// insert data to st_info table
app.get('/insert', async (req, res) => {
    const { st_id, name, dept } = req.query;
    const [rows] = await pool.query("insert into st_info values (?, ?, ?)",
        [st_id, name, dept]);
    res.redirect('/select');
})

//update data to st_info table
app.get('/update', async (req, res) => {
    const { st_id, name, dept } = req.query;
    const [rows] = await pool.query("update st_info set NAME = ?, DEPT = ? where ST_ID = ?",
        [name, dept, st_id]);
    res.redirect('/select');
})

// delete data from st_info table
app.get('/delete', async (req, res) => {
    const st_id= req.query.st_id;
    const [rows] = await pool.query("delete from st_info where ST_ID = ?",
        [st_id]);
    res.redirect('/select');
})

module.exports = app;