#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2])
  .then(function (response) {
    const completeDictionary = {};
    let id;
    response.data.forEach(user => {
      id = user.userId;
      if (user.completed === true) {
        if (completeDictionary[id]) {
          completeDictionary[id] += 1;
        } else {
          completeDictionary[id] = 1;
        }
      }
    });
    console.log(completeDictionary);
  })
  .catch(function (error) {
    console.log(error);
  });
