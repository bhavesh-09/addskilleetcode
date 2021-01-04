const mongoose = require('mongoose');
const MealSchema = new mongoose.Schema({
  mealname:{
    type:String,
    required:true
  },
  mealtype: {
    type: String,
    required:true,
  },
  description: {
    type: String,
    min: 20,
  },
  
  calories:{
    type:Number
  },
  // DayLimit: {
  //   type: Boolean,
  // },
  // userId: {
  //   type: String,
  //   required: true,
  // },
  // modifiedOn: {
  //   type: Date,
  //   default: new Date(),
  // },
});

 
const Meal = mongoose.model('Meal', MealSchema);
module.exports = Meal;