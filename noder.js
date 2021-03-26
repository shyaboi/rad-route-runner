const util = require("util");
const exec = util.promisify(require("child_process").exec);
const fs = require ("fs")

// console.log(process.argv[14])

let eObj = process.argv[14].slice(0, -2)

const doThing = ()=> {eval(eObj)}

// let obj = process.argv[2]
// console.log(obj)
// const writeData = () => {
//   const cb = ()=> {console.log('noder file writter ran')}
//   fs.appendFile('testFile.txt', '\nText Written From noder!\n', 'utf8', cb);
// }

try {
   doThing()
} catch (error) {
  console.error(error)
  console.error('noder went wrong')
}

// const noder = async (cmd) => {
//   const { stdout, stderr } = await exec(cmd);
//   console.log("stdout:", stdout);
//   console.error("stderr:", stderr);
// };

// writeData()
// noder("echo Noder! Ran!");
// noder("python pyRunner.py");
