const express = require("express");
const path = require("path");
const fs = require("fs");
const app = express();
const port = 80;


//Static related code
app.use('/static',express.static('static')) //for serving static files 
// app.use(express.urlencoded())
app.use(express.urlencoded({ extended: true }))

//pug related code
app.set('view engine','pug') //set the template(rename it to templates) engine for pug 
app.set('views',path.join(__dirname,'views')) //set the templates directory


//ENDPOINTS
app.get('/', (req, res)=>{
    const con = "Lorem ipsum "
    const params = {'title': 'Bhavesh Express', "content": con}
    res.status(200).render('index.pug', params);
})
app.post('/',(req,res)=>{
    // console.log(req.body)
    Name = req.body.Name
    age = req.body.age
    gender = req.body.gender
    address = req.body.address
    more = req.body.more

    let resultIs=`the name of the client is ${Name}, ${age} years old, ${gender}, residing at ${address}. More about him/her: ${more}`
    fs.writeFileSync("output.txt",resultIs)
    const params = {'message':"Your form is submitted Successfully!!"}
    res.status(200).render('index.pug',params)
});
     
//SERVER
app.listen(port,() =>{
    console.log(`The application is running on port ${port}`)
});