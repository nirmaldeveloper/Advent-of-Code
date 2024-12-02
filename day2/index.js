const fs = require("fs");
const readline = require("readline");

const input_path = "input.csv";

const inputStream = fs.createReadStream(input_path);
lst1 = [];
async function processLineByLine() {
  const rl = readline.createInterface({
    input: inputStream,
      terminal: false,
  });

  for await (const line of rl) {
    //console.log(line);
    output = line.split(" ").map(Number);
    //console.log(output);
    lst1.push(output);
  }
};

processLineByLine().then(()=>{
  let count = 0;
  for(let x =0; x<lst1.length; x++){
  //console.log(lst1[x]);
  let lst = lst1[x];
  let i =1;
  if(lst[0] > lst[1]){
    while(i<lst.length){
      let x = lst[i-1];
      let y = lst[i];
      let z = x -y;
      if((x > y) && !(z < 1 || z > 3)){
        i++;
      }
      else{break;}
    }
  }
  else if(lst[0] < lst[1]){
    while(i<lst.length){
      let x = lst[i-1];
      let y = lst[i];
      let z = y - x;
      if((x < y) && !(z < 1 || z > 3)){
        i++;
      }
      else{break;}
  }
    }
  if( i == lst.length){
    count++;
  }
  }
  console.log(count);
});





