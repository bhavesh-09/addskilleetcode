// practical for mongo db using in power shell

use bhaveshdb
db.items.insertOne({name:"Bhavesh",surname:"sharma",age:23})
db.items.insertMany([{name:"Bhavesh",surname:"sharma",age:23},{name:"Hitesh",surname:"shar",age:21},{name:"Bhavana",surname:"shama",age:43},{name:"Mahesh",surname:"shaa",age:53}])

// search query in db 

db.items.find({age:{$gt:43}})    //(gt=greater than age 43)
db.items.deleteOne({name:"Bhavesh",surname:"sharma",age:23}) 
db.items.updateOne({name:"Mahesh"}, {$set:{name:"Bhavesh",age:23}})