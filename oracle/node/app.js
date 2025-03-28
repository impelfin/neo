var oracledb = require('oracledb');
var dbConfig = require('./dbConfig');

oracledb.initOracleClient({libDir:'/opt/oracle/instantclient_21_13'})

oracledb.getConnection(
    {
        user: dbConfig.user,
        password: dbConfig.password,
        connectString: dbConfig.connectString
    }, function(err, connection) {
        if (err) {
            console.error(err.message);
            return;
        }
        connection.execute(
            'select * from usertbl',
            function (err, result) {
                if (err) {
                    console.error(err.message);
                    doRelease(connection);
                    return;
                }
                console.log(result.metaData);
                console.log(result.rows);
                doRelease(connection);
            }
        )
    }
);

function doRelease(connection) {
    connection.release(
        function (err) {
            if (err) {
                console.error(err.message);
            }
        }
    )
}