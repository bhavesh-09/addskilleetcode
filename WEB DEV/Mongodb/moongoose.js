var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/bhaveshdb', { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
    // we're connected!
    console.log("we are connected bro")
});

const kittySchema = new mongoose.Schema({
    name: String
  })

// NOTE: methods must be added to the schema before compiling it with mongoose.model()
kittySchema.methods.speak = function () {
    const greeting = this.name
      ? "my cat name is " + this.name
      : "I don't have a name";
    console.log(greeting);
  }

const Kitten = mongoose.model('bhaveshcats', kittySchema);

const silence = new Kitten({ name: 'Billu' });
// console.log(silence.name); 
// silence.speak()

silence.save(function (err, silence) {
    if (err) return console.error(err);
    silence.speak();
  });

Kitten.find({name:"bhaveshcats"},function (err, kittens) {
    if (err) return console.error(err);
    console.log(kittens);
  })