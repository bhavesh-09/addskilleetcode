const express= require("express");
const app = express();
const PORT=process.env.PORT || 5000;
const expressLayouts = require('express-ejs-layouts');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const flash=require("connect-flash");
const session = require("express-session");
const passport = require("passport");
const path = require('path')

// Passport Config
require('./config/passport')(passport);

// Connect to Mongo
mongoose.connect("mongodb://localhost:27017/nutrifiredb", { useNewUrlParser: true, useUnifiedTopology: true })
	.then(() => console.log('Connected to database...'))
    .catch(err => console.log('Database error:', err))

// EJS
app.use(expressLayouts)
app.set('view engine', 'ejs')
app.set("views",path.join(__dirname,"views"))

//Body parser
// app.use(bodyParser.json());
app.use(express.urlencoded({extended: true}))


// Express session
app.use(
    session({
      secret: 'secret',
      resave: true,
      saveUninitialized: true
    })
  ); 

// Passport middleware
app.use(passport.initialize());
app.use(passport.session());

// Connect flash
app.use(flash());

// Global variables
app.use(function(req, res, next) {
  res.locals.success_msg = req.flash('success_msg');
  res.locals.error_msg = req.flash('error_msg');
  res.locals.error = req.flash('error');
  res.locals.page=req.flash("page")
  next();
});

// Public
app.use(express.static(path.join(__dirname, 'public')))

//Routes
app.use("/",require("./routes/index"));
app.use("/users",require("./routes/users"));
app.use("/meals",require("./routes/meals"));




app.listen(PORT,console.log("Server on port 5000"));
