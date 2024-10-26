const express = require('express');
const mysql = require('mysql2');
const app = express();
const PORT = process.env.PORT || 3000;

const connection = mysql.createConnection({
  host: process.env.MYSQL_HOST || 'mysql',
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: process.env.MYSQL_DATABASE
});

app.get('/data', (req, res) => {
  connection.query('SELECT * FROM sample_data', (error, results) => {
    if (error) {
      return res.status(500).send(error);
    }
    res.json(results);
  });
});

app.listen(PORT, () => {
  console.log(`API server running on port ${PORT}`);
});
