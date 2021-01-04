const express = require('express');
const app = express();
const router = express.Router();
const bodyParser = require('body-parser');
const Meal=require("../models/Meal");

app.use(express.urlencoded({extended: true}))


router.get('/tracker',  (req, res) =>
  res.render('tracker', {
    // meal: req.meal
    
  })
);

router.post("/tracker",  (req, res) => {
    var myData = new Meal(req.body);
    myData.save().then(()=> {
        res.send("item saved to database");
    }).catch(err => {
        res.status(400).send("unable to save to database");
    });
});

router.get('/test',  (req, res) =>
  res.render('test', {
    Meal:mealname
    
    
  })
);





module.exports = router;
