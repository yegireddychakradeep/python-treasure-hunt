var startTime, endTime;

function startTimer() {
  startTime = new Date();
};

function stopTimer() {
  endTime = new Date();
  var timeDiff = endTime - startTime; //in ms
  // strip the ms
  timeDiff /= 1000;
  
  // get seconds 
  var seconds = Math.round(timeDiff);
  return seconds;
};
