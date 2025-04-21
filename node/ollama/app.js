// app.js
// Ollama Web Interface - 메인 서버 파일

const express = require('express');
const path = require('path');
const app = express();
const PORT = 8000;

// 미들웨어
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// 뷰 엔진 설정 (HTML 렌더링)
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'html');
app.engine('html', require('ejs').renderFile);

// 라우터
const mainRouter = require('./controllers/mainController');
app.use('/', mainRouter);

// 서버 시작
app.listen(PORT, () => {
  console.log(`Ollama Web Interface server running on http://localhost:${PORT}`);
});
