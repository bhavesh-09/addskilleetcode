const path = require('path')
const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const expressLayouts = require('express-ejs-layouts') 

const app = express()



// app.set('view engine', 'ejs')

// // Connect to Mongo
// mongoose.connect("mongodb://localhost:27017/nutrifiredb", { useNewUrlParser: true, useUnifiedTopology: true })
// 	.then(() => console.log('Connected to database...'))
//     .catch(err => console.log('Database error:', err))

// EJS
app.use(expressLayouts)
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs')


app.use(bodyParser.json())
app.use(express.urlencoded({extended: false}))

// Public
app.use(express.static(path.join(__dirname, 'public')))


// Routes
app.use('/', require('./routes/index'))
app.use('/users', require('./routes/users'))

equire('./routes/meals')(app);


app.listen(80, function () {
    console.log("I m here at port 80");
});