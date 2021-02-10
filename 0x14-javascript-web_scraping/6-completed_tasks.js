#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, response);

function response (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const userIds = [];
    const completedTasks = {};
    const bodyJson = JSON.parse(body);
    // console.log(body);
    bodyJson.forEach(element => {
      if (!userIds.includes(element.userId)) {
        userIds.push(element.userId);
      }
    });
    userIds.forEach(id => {
      completedTasks[id] = bodyJson
        .filter(task => task.userId === id && task.completed)
        .map(task => 1)
        .reduce((acc, cur) => acc + cur);
    });
    console.log(completedTasks);
  }
}
