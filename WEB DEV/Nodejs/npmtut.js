const validator = require('validator');
const chalk = require('chalk');

const ans = validator.isEmail('bhavesh09@gmail.com'); //=> true
console.log(ans?chalk.green.inverse(ans):chalk.red.inverse(ans));