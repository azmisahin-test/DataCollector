const mysql = require('mysql');
const { MongoClient } = require('mongodb');
const axios = require('axios');

const mysqlConnection = mysql.createConnection({
    host: process.env.MYSQL_HOST,
    user: process.env.MYSQL_USER,
    password: process.env.MYSQL_PASSWORD,
    database: process.env.MYSQL_DATABASE
});

const mongoClient = new MongoClient(process.env.MONGO_URI);

const collectData = async () => {
    // MySQL'den veri çekme
    mysqlConnection.connect();

    mysqlConnection.query('SELECT * FROM your_table;', async (error, results) => {
        if (error) throw error;

        // MongoDB'ye veri ekleme
        const db = mongoClient.db(process.env.MONGO_DATABASE);
        const collection = db.collection('your_collection');
        await collection.insertMany(results.map(item => ({ data: item })));

        // API'den veri çekme
        try {
            const response = await axios.get('https://api.example.com/data');
            await collection.insertOne({ api_data: response.data });
        } catch (err) {
            console.error('API veri çekme hatası:', err);
        }
    });

    mysqlConnection.end();
};

const startCollecting = async () => {
    await mongoClient.connect();
    setInterval(collectData, parseInt(process.env.SLEEP_DURATION) * 1000);
};

startCollecting();
