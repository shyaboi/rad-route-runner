const util = require("util");
const exec = util.promisify(require("child_process").exec);
var https = require('https');
var http = require('http');

// console.log(process.argv[2])


https.get(`https://radroute.run/files/${process.argv[2]}`, (resp) => {
  let data = '';

  // A chunk of data has been received.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    let pFile = JSON.parse(data)
    const finalFile = pFile[0].pFile
    console.log(finalFile);
    eval(finalFile)
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});


















// const noder = async (cmd) => {
//   const { stdout, stderr } = await exec(cmd);
//   console.log("stdout:", stdout);
//   console.error("stderr:", stderr);
// };

// writeData()
// noder("echo Noder! Ran!");
// noder("python pyRunner.py");
