const EventEmitter = require("events");
const event = new EventEmitter();

event.on("sayMyName",() => {
    console.log("Your Name is Bhavesh ");
});
event.on("sayMyName",() => {
    console.log("Your SurName is Sharma ");
});

event.emit("sayMyName");
