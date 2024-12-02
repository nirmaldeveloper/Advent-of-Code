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
function checkLimit(j){
  let y = (Math.abs(j) === 3 || Math.abs(j) === 2 || Math.abs(j) === 1);
  return y;
}

let count = 0;
function IsSafeReport(numbers){
  let i =1;
  if(numbers.length < 2)
  {
    return false;
  }
  let incr = numbers[1] > numbers[0];
  if(incr){
    for(let x = 0; x < numbers.length-1; x++){
         let z = numbers[x] - numbers[x+1];
         if( z < 0 && checkLimit(z)){
           i++;
         }
      else{
        return false;
      }

    }
  }
  else if(!incr){
    for(let x = 0; x < numbers.length-1; x++){
       let z = numbers[x] - numbers[x+1];
       if( z > 0 && checkLimit(z)){
            i++;
       }
      else{
        return false;
      }
    }
  }
  else{
    return false;
  }
  //console.log(numbers);
  
  if( i == numbers.length){
    return true;
  }
  
  return false;
}

processLineByLine().then(()=>{
  //Part1
  let count_safe = 0;
  for(let x =0; x<lst1.length; x++)
  {
  
  let lst_a = lst1[x];
  if(IsSafeReport(lst_a)){
    count_safe++;
  }
  }
  console.log(count_safe);
  
  //Part2
  for(let x =0; x<lst1.length; x++)
  {
    let lst = lst1[x];
    if(IsSafeReport(lst))
    {
      count++;
    }
    else
    {
      //Since we found the array is not safe, let's find if it    //could be made safe by just excluding one element
    for(let a = 0; a< lst.length; a++){
      const chunck = [...lst.slice(0,a), ...lst.slice(a+1)];
      
      if(IsSafeReport(chunck))
      {
        count++;
        break; //break after finding which number to exclude
       }
      }
    }
  }
  console.log(count);
  
});
