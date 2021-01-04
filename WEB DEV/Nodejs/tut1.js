const http = require("http");
const server = http.createServer((req,res) => {
    if (req.url == "/"){
        res.end("Hello bhavesh from server end ");
    }    else if (req.url == "/about"){
        res.end("Hello bhavesh from about end ");
    } else {
        res.writeHead(404);
        res.end("Error 404 Page does not exist ");
    } 
});

server.listen(9000,"127.0.0.1",() =>{
    console.log("running on  port 9000");
});