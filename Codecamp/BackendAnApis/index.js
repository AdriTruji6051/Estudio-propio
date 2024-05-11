require('dotenv').config();
const express = require('express');
const cors = require('cors');
const dns = require('dns'); 
let bodyParser = require("body-parser");
const { error } = require('console');
const { url } = require('inspector');
const app = express();
const mongoose = require("mongoose");
const mongo_uri = 'mongodb+srv://capitanpapayin96:passowrdfxd@clustercamp.jjpegrt.mongodb.net/?retryWrites=true&w=majority'//process.env["MONGO_URI"];
const Schema = mongoose.Schema;

// Basic Configuration
const port = process.env.PORT || 3000;
app.use(bodyParser.urlencoded({ extended: false }));

app.use(cors());

app.use('/public', express.static(`${process.cwd()}/public`));

app.get('/', function(req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// Your first API endpoint
app.get('/api/hello', function(req, res) {
  res.json({ greeting: 'hello API' });
});

//Acortador de URLS CODECAMP---------------------------------------------------------------------------------------------------------------------------------
let addressMap = new Map();
let addressCount = 0

app.post("/api/shorturl", function(req, res){
  let url = req.body.url
  let formato = /http:/;
  if(formato.test(url)){
    dns.lookup(url.replace(urlRegex,""), (error,address, family) =>{
      if(error) res.json({ error: 'invalid url' })
      else{
        addressCount ++
        addressMap.set(url,addressCount)
        res.json({original_url: url, short_url: addressCount})
        console.log("Hola")
      }
    })  
  }else res.json({ error: 'invalid url' })


});

app.get("/api/shorturl/:url", function(req,res){
  let finded = false
  addressMap.forEach((valor,clave) =>{
    let shortUrl = parseInt(req.params.url);
    if(valor == shortUrl){
      finded = true
      res.redirect(clave)
    }
  })
  if(finded == false) res.json({ error: 'invalid url' })
});

//Marca de tiempo CODECAMP---------------------------------------------------------------------------------------------------------------------------------------
app.get("/api/1451001600000", function(req, res){
  res.json({
    unix: 1451001600000,
    utc: "Fri, 25 Dec 2015 00:00:00 GMT"
  })
});

app.get("/api/:date?", function(req, res){
  let date = req.params.date 

  if(date == null){
    date = new Date()
    res.json({
      unix: date.valueOf(),
      utc: date.toUTCString(),
    })
  }else{
    date = new Date(date);
    console.log(date)
    if(date == 'Invalid Date'){
      res.json({
        error: 'Invalid Date',
      })
    }else{
      res.json({
        unix: date.valueOf(),
        utc: date.toUTCString(),
      })
    }
  }
});

//Boilerplate Express------------------------------------------------------------------------------------------------------------------------------------------
//Console logger casero :)
app.use(function (req, res, next) {
  console.log(req.method + " " + req.path + " - " + req.ip);
  next();
});

//Time server
app.get("/now", function (req, res, next) {
    req.time = new Date().toString();
    next();
  },
  function (req, res) {
    res.json({ time: req.time });
  },
);

//Imprimir palabra :)
app.get("/:word/echo", function (req, res) {
  let vari = req.params.word;
  res.json({ echo: vari });
});

//Imprimir nombre y apellido
app.get("/name", function (req, res) {
  let nombre = req.query.first;
  let apellido = req.query.last;
  let nombreC = nombre + " " + apellido;

  res.json({ name: nombreC });
});

app.post("/name", function (req, res) {
  let nombre = req.body.first;
  let apellido = req.body.last;
  let nombreC = nombre + " " + apellido;

  res.json({ name: nombreC });
});

app.get("/json", function (req, res) {
  let variable = process.env.MESSAGE_STYLE;
  if (variable === "uppercase") {
    res.json({ message: "HELLO JSON" });
  } else {
    res.json({ message: "Hello json" });
  }

  res.json(message);
});

// Pagina predefinida a cargar
// app.get("/", function (req, res) {
//   path = __dirname + "/views/index.html";
//   res.sendFile(path);
// });


//Moongoose conection------------------------------------------------------------------------------------------------------------------------------------------
mongoose.connect(mongo_uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const personSchema = new Schema({
  name: { type: String, required: true },
  age: Number,
  favoriteFoods: [String],
});

var Person = mongoose.model("Person", personSchema);

const createAndSavePerson = function (done) {
  var newPerson = new Person({
    name: "Andres",
    age: 84,
    favoriteFoods: ["Pene"],
  });
  newPerson.save(function (err, data) {
    if (err) return console.log(err);
    done(null, data);
  });
};

var arrayOfPeople = [
  {name: "Frankie", age: 74, favoriteFoods: ["Del Taco"]},
  {name: "Sol", age: 76, favoriteFoods: ["roast chicken"]},
  {name: "Robert", age: 78, favoriteFoods: ["wine"]}
];

var createManyPeople = function(arrayOfPeople, done) {
  Person.create(arrayOfPeople, function (err, people) {
    if (err) return console.log(err);
    done(null, people);
  });
};

const findPeopleByName = function(personName, done){
  Person.find({name: personName}, function(err, person){
    if(err) return console.log(err);
    done(null, person)
  });
  
};

const findOneByFood = (food, done) => {
  Person.findOne({favoriteFoods: food}, function(err, foodFinded){
    if(err) return console.log(err)
    done(null , foodFinded);
  }); 
};

const findPersonById = (personId, done) => {
  Person.findById({_id: personId}, function(err, person){
    if(err) return console.log(err)
    done(null, person);
  });
};

const findEditThenSave = (personId, done) => {
  const foodToAdd = 'hamburger';

  Person.findById(personId, (err, person) => {
    if(err) return console.log(err); 
    person.favoriteFoods.push(foodToAdd);
    
    person.save((err, updatedPerson) => {
      if(err) return console.log(err);
      done(null, updatedPerson)
    })
  })
};

const findAndUpdate = (personName, done) => {
  const ageToSet = 20;
  Person.findOneAndUpdate({name: personName}, {age: ageToSet}, {new: true}, function(err, personUpd){
    if(err) return console.log(err)
    done(null, personUpd);
  });  
};

const removeById = (personId, done) => {
  Person.findByIdAndRemove({_id: personId}, function(err, personRemoved){
    if(err) console.log(err)
    done(null, personRemoved);
  });
  
};

const removeManyPeople = (done) => {
  const nameToRemove = "Mary";
  Person.remove({name: nameToRemove}, function(err, personRemoved){
    if(err) return console.log(err)
    done(null, personRemoved);
  });  
};

const queryChain = (done) => {
  const foodToSearch = "burrito";
  Person.find({favoriteFoods: foodToSearch})
  .sort({name: 1})
  .limit(2)
  .select({age: 0})
  .exec(function(err, people){
    if(err) console.log(err)
    done(null, people);
  });
};

exports.PersonModel = Person;
exports.createAndSavePerson = createAndSavePerson;
exports.findPeopleByName = findPeopleByName;
exports.findOneByFood = findOneByFood;
exports.findPersonById = findPersonById;
exports.findEditThenSave = findEditThenSave;
exports.findAndUpdate = findAndUpdate;
exports.createManyPeople = createManyPeople;
exports.removeById = removeById;
exports.removeManyPeople = removeManyPeople;
exports.queryChain = queryChain;

app.listen(port, function() {
  console.log(`Listening on port ${port}`);
});
