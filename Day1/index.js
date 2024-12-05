const fs = require("fs");
const readline = require("readline");

const input_path = "input.csv";

const inputStream = fs.createReadStream(input_path);
lst1 = [];
lst2 = [];
async function processLineByLine() {
  const rl = readline.createInterface({
    input: inputStream,
      terminal: false,
  });

  for await (const line of rl) {
    output = line.split("   ");
    lst1.push(output[0]);
    lst2.push(output[1]);
  }
};

processLineByLine().then(()=>{
  lst1.sort();
  lst2.sort();
  sum = 0;
  for(let i = 0; i< lst1.length; i++){
    sum += Math.abs(lst1[i] - lst2[i]);

  }
  console.log(sum);

  count_sum = 0;
  for(let i=0; i < lst1.length; i++){
    count_sum += lst1[i] * lst2.filter(x => x==lst1[i]).length;
  }


  console.log(count_sum);
});
