const util = require("util");
const exec = util.promisify(require("child_process").exec);
const fs = require ("fs")

console.log(process.argv[10])

let eObj = process.argv[10].slice(0, -1)

eval(eObj)

// let obj = process.argv[2]
// console.log(obj)
// const writeData = () => {
//   const cb = ()=> {console.log('noder file writter ran')}
//   fs.appendFile('testFile.txt', '\nText Written From noder!\n', 'utf8', cb);
// }

const noder = async (cmd) => {
  const { stdout, stderr } = await exec(cmd);
  console.log("stdout:", stdout);
  console.error("stderr:", stderr);
};

// writeData()
noder("echo Noder! Ran!");
// noder("python pyRunner.py");
