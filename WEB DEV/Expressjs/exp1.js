const express = require("express")
const path = require("path");

const app = express();
const port = 80;


app.use('/static',express.static('static')) //for serving static files 



app.set('view engine','pug') //set the template(rename it to templates   ) engine for pug 


app.set('views',path.join(__dirname,'views')) //set the templates directory

//pug demo page
app.get('/demo',(req, res) => {
    res.status(200).render('demo', { title: 'Hey Bhavesh', message: 'Hello I am Pug ur page!' })
  });

app.get("/",(req,res) => {
    res.send("This is my first express app")
});

app.get("/about",(req,res) => {
    res.send("This is my first about page ")
});

app.post("/about",(req,res) => {
    res.send("This is my post about page ")
});



app.listen(port,() =>{
    console.log(`The application is running on port ${port}`)
});
