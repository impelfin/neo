const express = require('express');
const morgan = require('morgan');
const path = require('path');
const fs = require('fs');
const app = express();
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

app.set('port', process.env.Port || 8000);
app.set('views', path.join(__dirname, 'public'));
app.set('view engine', 'ejs');
app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

var main = require('./routes/main');
app.use('/', main);

app.listen(app.get('port'), function () {
    var dir = './uploadedFiles';
    if (!fs.existsSync(dir)) fs.mkdirSync(dir);
    console.log('Server is Started~!! Port : ' + app.get('port'));
});
