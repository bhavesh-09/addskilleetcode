var express = require("express");
var app = express();
var bodyParser = require("body-parser");
var mongoose = require("mongoose");
app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
mongoose.connect("mongodb://localhost:27017/todolistdb", { useNewUrlParser: true, useUnifiedTopology: true });
const itemSchema = {
    name: String
}
const Item = mongoose.model("Item", itemSchema);
const item1 = new Item({
    name: "Welcome Bhavesh",
});
const item2 = new Item({
    name: "MERN stack",
});
const item3 = new Item({
    name: "TODO List",
});
const d = [item1, item2, item3];

// Item.insertMany(d,function(err)
// {
//     if(err){
//         console.log(err);
//     }
//     else{
//         console.log("Successfully saved items to DB");
//     }
// });





// var i = "";
// var i1=[];


app.get("/", function (req, res) {
    // res.send("<h1>Hey guys!!</h1>");
    Item.find({}, function (err, f) {
        // console.log(f);
        if (f.length === 0) {
            Item.insertMany(d, function (err) {
                if (err) {
                    console.log(err);
                }
                else {
                    console.log("Successfully saved items to DB");
                }
            });
            res.redirect("/");
        }
        else {
            res.render("list", { newListItem: f });
        }
    });
        
});

app.post("/", function (req, res) {
    const itemName=req.body.new;
    // i = req.body.new;
    // i1.push(i);
    //console.log(i);
    // res.render("list",{newListItem:i})
    res.redirect("/");
    const item=new Item({
        name: itemName
    });
    item.save();
});

app.post("/delete",function(req,res)
{
  const check=(req.body.checkbox);
  Item.findByIdAndRemove(check,function(err)
  {
      if(!err)
      {
          console.log("Successfully deleted");
          res.redirect("/");
      }
  })
});







app.listen(80, function () {
    console.log("I m here at port 80");
});