const express = require('express');
const path = require('path');
const app = express();
const PORT = 8000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'html');
app.engine('html', require('ejs').renderFile);

const mainRouter = require('./controllers/mainController');
app.use('/', mainRouter);

app.listen(PORT, () => {
    console.log(`Ollama Web Interface server running on http://localhost:${PORT}`);
});
