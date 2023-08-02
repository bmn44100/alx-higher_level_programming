#!/usr/bin/node

let request = require('request');
let request_url = process.argv[2];
request(request_url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let completed = {};
    let user_tasks = JSON.parse(body);
    for (let i in user_tasks) {
      let current_task = user_tasks[i];
      if (current_task.completed === true) {
        if (completed[current_task.userId] === undefined) {
          completed[current_task.userId] = 1;
        } else {
          completed[current_task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('Wrong status code');
  }
});
