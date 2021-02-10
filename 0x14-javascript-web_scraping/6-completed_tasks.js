#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, response);

function response (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTasks = {};
    const bodyJson = JSON.parse(body);
    // console.log(body);
    bodyJson
      .filter(task => task.completed)
      .forEach(task => {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId] += 1;
        }
      });
    console.log(completedTasks);
  }
}
