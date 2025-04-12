
const port = 3000; 
const db = require('old-wio.db'); 
const express = require('express');
const http = require('http');
const path = require('path');
const socketIo = require('socket.io');
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files (e.g., index.html)
app.use(express.static('public'));

// Route to handle data requests
app.get('/pair', (req, res) => {
    // Example data response. Replace with your actual data fetching logic.
    const data = {
        paired: 'true'
    };
    res.json(data);
});

// Simulate emitting new data periodically
 


app.get('/', (req, res) => {  
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/bus-selection.html', (req, res) => {  
    res.sendFile(path.join(__dirname, 'bus-selection.html'));
});
app.get('/route-selection', (req, res) => {
    res.sendFile(path.join(__dirname, 'route-selection.html'));
});
app.get('/track', (req, res) => {  
    res.sendFile(path.join(__dirname, 'tracking.html'));
});
app.get('/bus-range.html', (req, res) => {  
    res.sendFile(path.join(__dirname, 'bus-range.html'));
});


io.on('connection', (socket) => {
    console.log('A client connected:', socket.id);
    clientID = socket.id;
    io.emit('newData', {
        sid: socket.id
    });

    socket.on('disconnect', () => {
        console.log('A client disconnected:', socket.id);
    });
});

// Listen on a port
server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});

let clientID = "";
 
let user1 = "";
let response1 = "";
let subscriptions = [];
let i = 0; 

app.get('/quickfind', async (req, res) => {
    let bus = req.query.bus;
    
    await io.emit("quickfind", {
        bus: bus
    })
    db.set("quickfind", bus);
    res.sendFile(path.join(__dirname, 'route-selection.html'));
    console.log(bus)
    await io.emit("quickfind", {
        bus: bus
    })

})

app.get('/response', (req, res) => {
 
    let lati = req.query.lati; // Extract the value of the 'data' query parameter
    let long = req.query.long; // Extract the value of the 'data' query parameter
    let stat = req.query.stat; // Extract the value of the 'data' query parameter 
    let psc = req.query.psc; // Extract the value of the 'data' query parameter 
    if(!psc) psc = "0";
    console.log(`lati: ${lati}`);
    console.log(`long: ${long}`);
    console.log(`stat: ${stat}`);
    console.log(`psc: ${psc}`);
    db.set(`lati`, `${lati}`);
    db.set(`long`, `${long}`);
    db.set(`stat`, `${stat}`);
    db.set(`psc`, `${psc}`);
    res.json({ lat: lati, long: long, stat: stat, psc: psc });
    io.emit('locData', {
        latitude: lati,
        longtitude: long,
        state: stat,
        psc: psc
    });

});

app.get('/search', (req, res) => {
    res.send(user1);
}) 
app.get('/result', (req, res) => {
    res.send(response1);
})  

app.get('/user', async (req, res) => {
    //syntax = /user?data=571
    //2 char of bus number, 1 to 57
    //1 char of up or down, 0 = down, 1 = up
    let busNo = req.query.b; // Extract the value of the 'data' query parameter
    let Route = req.query.r; // Extract the value of the 'data' query parameter 
    let upOrdown = "UP";
    if(Route == 1) upOrdown = "DOWN";
    console.log(`BusNumber: ${busNo}`);
    console.log(`upORdown: ${Route} - ${upOrdown}`); 
    let c = await db.fetch("Counter");
    db.set(`B0`, `${busNo}`)
    db.set(`R0`, `${Route}`)

    //db.add(`Counter`, 1)
    res.json({ user: busNo, route: upOrdown});  // Respond with the data value
});

app.get('/data', async (req, res) => {
    
    let lati = await db.fetch(`lati`);
    let long = await db.fetch(`long`);
    let stat = await db.fetch(`stat`);
    if(lati)  res.json({ stored: 1, lat: lati, long: long, stat: stat });
    if(!lati) res.json({ stored: 0, lat: lati, long: long, stat: stat });

    db.set(`lati`, "");
    db.set(`long`, "");
    db.set(`stat`, ""); 
    
});

app.get('/fetch', (req, res) => {
    let b = parseInt(db.fetch("B0"));
    let r = db.fetch("R0");
    let result = ``;
    if(b < 1000) result += "0";
    if(b < 100) result += "0";
    if(b < 10)  result += "0";
    db.set(`B0`, ``);
    db.set(`R0`, ``);
    let userCode = genCode();
    result += `${b}${r}`;
    console.log(`Result: ${result}${userCode}`);
    if(result == "NaNnull") res.send("00000");
    if(result != "NaNnull") res.send(`${result}${userCode}`); //${userCode}

}) 
app.get('/clear', (req, res) => {
    
        user1 = "0";
        response1 = "0"; 
        res.json({ user: user1, response: response1 });   
}) 


function genCode() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let result = '';
    for (let i = 0; i < 4; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        result += characters[randomIndex];
    }
    return result;
}
 




/*

Main page:

1. Select Bus No.
2. Select Route



Bus pages:
1. select Bus:
Card structure
device bus into parts of 10
1-10 11-20
21-30 31-40
41-50 51-57

divide them after selcting one
1 2
3 4
5 6
7 8
9 10

card structure will be opened

2. select route:
1 to 57 bus numbers on drop down menu with source and destination


*/