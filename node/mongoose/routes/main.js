const express = require("express");
const app = express.Router();
const mongoose = require("mongoose");
const async = require("async");

// define schema
const userSchema = new mongoose.Schema(
  {
    userid: String,
    name: String,
    city: String,
    sex: String,
    age: Number,
  },
  {
    versionKey: false,
  }
);

// create model with mongodb collection and schema
var User = mongoose.model("users", userSchema);

app.get("/Hello", function (req, res) {
  res.send("Hello World!!");
});

// list
app.get("/list", function (req, res) {
  User.find({}, function (err, docs) {
    if (err) console.log(err);
    res.send(docs);
  }).projection({ _id: 0 });
});

// get
app.get("/get", async function (req, res) {
  try {
    var userid = req.query.input;
    if (!userid) {
      return res.status(400).send("User ID is required");
    }

    var user = await User.findOne({ userid: userid }).select("-_id");
    if (!user) {
      return res.status(404).send("User not found");
    }

    res.status(200).json(user);
  } catch (err) {
    console.log(err);
    res.status(500).send("Error retrieving user");
  }
});

// insert
app.post("/insert", async function (req, res) {
  try {
    var { userid, name, city, sex, age } = req.body;

    if (!userid || !name || !city || !sex || !age) {
      return res.status(400).send("All fields are required");
    }

    var existingUser = await User.findOne({ userid: userid });
    if (existingUser) {
      return res.status(409).send("User ID already exists");
    }

    var user = new User({
      userid: userid,
      name: name,
      city: city,
      sex: sex,
      age: age,
    });
    await user.save();
    res.status(200).send("Insert Success");
  } catch (err) {
    console.log(err);
    res.status(500).send("Insert Error");
  }
});

// update
app.post("/update", async function (req, res) {
  try {
    var { userid, name, city, sex, age } = req.body;

    if (!userid) {
      return res.status(400).send("User ID is required");
    }

    var user = await User.findOne({ userid: userid });
    if (!user) {
      return res.status(404).send("User not found");
    }

    user.name = name || user.name;
    user.city = city || user.city;
    user.sex = sex || user.sex;
    user.age = age || user.age;

    await user.save();
    res.status(200).send("Update Success");
  } catch (err) {
    console.log(err);
    res.status(500).send("Update Error");
  }
});

// delete
app.post("/delete", async function (req, res) {
  try {
    var userid = req.body.userid;
    if (!userid) {
      return res.status(400).send("User ID is required");
    }

    var user = await User.findOne({ userid: userid });
    if (!user) {
      return res.status(404).send("User not found");
    }

    await User.deleteMany({ userid: userid });
    res.status(200).send("Delete Success");
  } catch (error) {
    console.log(error);
    res.status(500).send("Delete Error");
  }
});

module.exports = app;

async.series(
  [query1, query2, query3, query4, query5, query6],
  function (err, result) {
    if (err) {
      console.log("Error : " + err);
    } else {
      console.log("Task Finished");
    }
  }
);

// select * from users
function query1(callback) {
  User.find({}, { _id: 0 }).exec(function (err, user) {
    console.log("\nQuery 1");
    console.log(user + "\n");
    callback(null);
  });
}

// select userid, name, city from users
function query2(callback) {
  User.find({}, { _id: 0, userid: 1, name: 1, city: 1 }).exec(function (
    err,
    user
  ) {
    console.log("\nQuery 2");
    console.log(user + "\n");
    callback(null);
  });
}

// select * from users where city='Seoul' order by userid limit 3
function query3(callback) {
  User.find({ city: "Seoul" }, { _id: 0 })
    .sort({ userid: 1 })
    .limit(3)
    .exec(function (err, user) {
      console.log("\nQuery 3");
      console.log(user + "\n");
      callback(null);
    });
}

// select userid, name from users where userid="/02/"
function query4(callback) {
  User.find({ userid: { $regex: "02" } }, { _id: 0 })
    .select("userid name")
    .exec(function (err, user) {
      console.log("\nQuery 4");
      console.log(user + "\n");
      callback(null);
    });
}

// using JSON doc query
// select userid, name, age from users where city="Seoul" and age > 15 and age < 23
function query5(callback) {
  User.find({ city: "Seoul", age: { $gt: 15, $lt: 23 } }, { _id: 0 })
    .sort({ age: -1 })
    .select("userid name age")
    .exec(function (err, user) {
      console.log("\nQuery 5");
      console.log(user + "\n");
      callback(null);
    });
}

// using querybuilder
// select userid, name, age from users where city="Seoul" and age > 15 and age < 30 oder by age
function query6(callback) {
  User.find({}, { _id: 0 })
    .where("city")
    .equals("Seoul")
    .where("age")
    .gt(15)
    .lt(30)
    .sort({ age: 1 })
    .select("userid name age")
    .exec(function (err, user) {
      console.log("\nQuery 6");
      console.log(user + "\n");
      callback(null);
    });
}
