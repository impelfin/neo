var oracledb = require('oracledb');
var dbConfig = require('./dbConfig');
var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');

oracledb.initOracleClient({ libDir: '/opt/oracle/instantclient_21_13' })

var app = express();
app.set('port', process.env.PORT || 3000);
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

oracledb.autoCommit = true;

app.get('/', (req, res) => {
    res.send('Web Server started~!!');
})

app.get('/dbTestSelect', function (req, res) {
    oracledb.getConnection(
        {
            user: dbConfig.user,
            password: dbConfig.password,
            connectString: dbConfig.connectString
        },
        function (err, connection) {
            if (err) {
                console.error(err.message);
                return;
            }
            let query = "select * from usertbl";

            connection.execute(query, [], function (err, result) {
                if (err) {
                    console.err(err.message);
                    doRelease(connection);
                    return;
                }
                console.log(result.rows);
                doRelease(connection, result.rows);
            })
        })

    function doRelease(connection, rowList) {
        connection.release(
            function (err) {
                if (err) {
                    console.error(err.message);
                }
                console.log('List size : ' + rowList.length);
                res.send(rowList);
            }
        )
    }
});

app.post('/dbTestInsert', function (req, res) {
    oracledb.getConnection({
        user: dbConfig.user,
        password: dbConfig.password,
        connectString: dbConfig.connectString
    },
        function (err, connection) {
            if (err) {
                console.error(err.message);
                return;
            }
            let query = 'insert into usertbl(userid, username, birthyear, addr, mobile1, mobile2, height, mdate) ' +
                'values(:userid, :username, :birthyear, :addr, :mobile1, :mobile2, :height, :mdate)';

            let binddata = [
                req.body.userid,
                req.body.username,
                Number(req.body.birthyear),
                req.body.addr,
                req.body.mobile1,
                req.body.mobile2,
                Number(req.body.height),
                new Date(req.body.mdate)
            ];

            connection.execute(query, binddata, function (err, result) {
                if (err) {
                    console.error(err.message);
                    doRelease(connection);
                    return;
                }
                console.log('Row Insert : ' + result.rowsAffected);
                doRelease(connection, result.rowsAffected);
            });
        });

    function doRelease(connection, result) {
        connection.release(function (err) {
            if (err) {
                console.error(err.message);
            }
            res.sendStatus(200);
        })
    }
})

app.all('*', function (req, res) {
    res.status(404).send('<h1>Error - Page is not found.</h1>');
})

app.listen(app.get('port'), function () {
    console.log("Express server listening on port " + app.get('port'));
})