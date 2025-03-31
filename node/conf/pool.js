const mysql = require('mysql2')
const env = require('dotenv').config({ path: "../../.env" });

const pool = mysql.createPool({
    // mysql authentication info    
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
})

const promisePool = pool.promise()

module.exports = promisePool;