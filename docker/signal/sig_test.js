'use strict';

var http = require('http');

var server = http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from io.js\n');
});

server.listen(8000, '0.0.0.0', function () {
    console.log('Server Started on port 8000');
});

var signals = {
    SIGINT: 2,
    SIGTERM: 15,
};

function shutdown(signalName, value) {
    server.close(function () {
        console.log('Server Stopped by ' + signalName);
        process.exit(128 + value);
    });
}

Object.keys(signals).forEach(function (sig) {
    process.on(sig, function () {
        shutdown(sig, signals[sig]);
    });
});
