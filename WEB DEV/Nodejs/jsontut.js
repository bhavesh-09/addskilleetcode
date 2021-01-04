const fs= require("fs")
const resume = {
    name: "bhavesh",
    surname: "sharma",
    dob: "9/1/1997",

};

const JSONData = JSON.stringify(resume)
fs.writeFile("jsontut.json",JSONData,(err) => {
    console.log("done");
    
})




// const objData = JSON.parse(JSONData)
// console.log(objData)