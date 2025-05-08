var http = require('http');

const hostname = '0.0.0.0'
const port = 8000

var server = http.createServer(function (req, res) {
    res.statusCode = 200;
    res.writeHead('Content-Type': 'text/plain');
    res.end(`Hello from NodeJS in ${proccess.arch}!\n`);
});

server.listen(port, hostname, function () {
    console.log(`Server running at http://${hostname}:${port}/`);
});

