#!/usr/bin/node
const request = require('request');
const UrlToGet = process.argv[2];
request(UrlToGet, function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    const AllTasks = JSON.parse(body);
    const TasksDone = {};
    for (const i in AllTasks) {
      if (AllTasks[i].completed === true) {
        if (AllTasks[i].userId in TasksDone) {
          TasksDone[AllTasks[i].userId]++;
        } else {
          TasksDone[AllTasks[i].userId] = 1;
        }
      }
    }
    console.log(TasksDone);
  }
});
