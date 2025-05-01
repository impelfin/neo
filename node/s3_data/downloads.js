const fs = require('fs');
const env = require('dotenv').config({ path: '../../.env' });

const AWS = require('aws-sdk');
const ID = process.env.ID;
const SECRET = process.env.SECRET;
const BUCKET_NAME = 'kibwa-00';
const MYREGION = 'ap-northeast-2';
const s3 = new AWS.S3({ accessKeyId: ID, secretAccessKey: SECRET, region: MYREGION });

const downloadFile = fileName => {
  const params = {
    Bucket: BUCKET_NAME,
    Key: 'axios.png',
  };
  s3.getObject(params, function (err, data) {
    if (err) {
      throw err;
    }
    fs.writeFileSync(fileName, data.Body);
    console.log('File downloaded successfully.');
  });
};
downloadFile('axios.png');
