const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const fs = require('fs')
const path = require('path')
const env = require('dotenv').config({ path: '../../.env' });

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended : false }))
app.use(express.json())
app.use(express.urlencoded({ extended : true }))

const AWS = require('aws-sdk');
const ID = process.env.ID;
const SECRET = process.env.SECRET;
const BUCKET_NAME = 'kibwa-00';
const MYREGION = 'ap-northeast-2';
const s3 = new AWS.S3({ accessKeyId: ID, secretAccessKey: SECRET, region: MYREGION });

app.get('/list', (req, res) => {
    const params = {
        Bucket : BUCKET_NAME,
        Delimiter : '/',
        Prefix : 'uploadedFiles/',
    }
    s3.listObjects(params, function(err, data) {
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

module.exports = app;