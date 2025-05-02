const express = require('express');
const app = express.Router();
const bodyParser = require('body-parser');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const env = require('dotenv').config({ path: '../../.env' });

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const AWS = require('aws-sdk');
const ID = process.env.ID;
const SECRET = process.env.SECRET;
const BUCKET_NAME = 'kibwa-00';
const MYREGION = 'ap-northeast-2';
const s3 = new AWS.S3({ accessKeyId: ID, secretAccessKey: SECRET, region: MYREGION });

var storage = multer.diskStorage({
    destination(req, file, cb) {
        cb(null, 'uploadedFiles/');
    },
    filename(req, file, cb) {
        cb(null, `${Date.now()}_${file.originalname}`);
    },
});

var upload = multer({ dest: 'uploadedFiles/' });
var uploadWithOriginalFilename = multer({ storage: storage });

app.get('/', function (req, res) {
    res.render('upload');
});

app.get('/list', (req, res) => {
    const params = {
        Bucket: BUCKET_NAME,
        Delimiter: '/',
        Prefix: 'uploadedFiles/',
    };
    s3.listObjects(params, function (err, data) {
        if (err) throw err;
        // res.json(data.Contents)
        res.writeHead(200);
        var template = `
            <!doctype html>
            <html>
            <head>
                <title>Result</title>
                <meta charset="utf-8">
            </head>
            <body>
                <table border="1" margin: auto; text-align: center;>
                    <tr>
                        <th> Key </th>
                        <th> LastModified </th>
                        <th> Size </th>
                        <th> StorageClass </th>
                        <th> Down </th>
                        <th> Del </th>
                    </tr>
        `;
        for (var i = 1; i < data.Contents.length; i++) {
            template += `
                    <tr>
                        <th> ${data.Contents[i]['Key']} </th>
                        <th> ${data.Contents[i]['LastModified']} </th>
                        <th> ${data.Contents[i]['Size']} </th>
                        <th> ${data.Contents[i]['StorageClass']} </th>
                        <th> 
                            <form method='post' action='downloadFile'>
                            <button type='submit' name='dlKey' value=${data.Contents[i]['Key']}>Down</button>
                            </form>
                        </th>
                        <th> 
                            <form method='post' action='deleteFile'>
                            <button type='submit' name='dlKey' value=${data.Contents[i]['Key']}>Del</button>
                            </form>
                        </th>
                    </tr>
            `;
        }
        template += `
                </table>
            </body>
            </html>
            `;
        res.end(template);
    });
});

app.post('/uploadFile', uploadWithOriginalFilename.single('attachment'), function (req, res) {
    res.render('confirmation', { file: req.file, files: null });

    console.log(req.file.filename);
    const filename = req.file.filename;
    const file = 'uploadedFiles/' + filename;
    const uploadFile = filename => {
        const fileContent = fs.readFileSync(filename);
        const params = {
            Bucket: BUCKET_NAME,
            Key: filename,
            Body: fileContent,
        };
        s3.upload(params, function (err, data) {
            if (err) {
                return console.log(err);
            }
            console.log(`File uploaded successfully. ${data.Location}`);
        });
    };
    uploadFile(file);

    const filePath = path.join(__dirname, '../uploadedFiles', filename);
    fs.unlink(filePath, err => (err ? console.log(err) : console.log(`File delete successfully. ${filePath}`)));
});

app.post('/downloadFile', function (req, res) {
    var filename = req.body.dlKey;
    console.log(filename);

    const downloadFile = filename => {
        const params = {
            Bucket: BUCKET_NAME,
            Key: filename,
        };
        s3.getObject(params, function (err, data) {
            if (err) {
                return console.log(err);
            }
            res.attachment(filename);
            res.send(data.Body);
            res.send();
        });
    };
    downloadFile(filename);
});

app.post('/deleteFile', function (req, res) {
    var filename = req.body.dlKey;
    console.log(filename);

    const deleteFile = filename => {
        const params = {
            Bucket: BUCKET_NAME,
            Key: filename,
        };
        s3.deleteObject(params, function (err, data) {
            if (err) {
                return console.log(err);
            }
            console.log(data);
            res.redirect('/list');
        });
    };
    deleteFile(filename);
});

module.exports = app;
