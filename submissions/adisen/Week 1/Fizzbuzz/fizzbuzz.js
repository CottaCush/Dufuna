function fizzBuzz(){
  for (var i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log("FizzBuzz");
    }
    else if (i % 3 == 0) {
      console.log("Fuzz");
      continue;
    }
    else if (i % 5 == 0) {
      console.log("Buzz");
      continue;
    }
    else {
      console.log(i);
      continue;
    }
  }
}
