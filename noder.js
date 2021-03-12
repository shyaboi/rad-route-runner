const util = require('util');
const exec = util.promisify(require('child_process').exec);



const noder = async(cmd)=> {
  const { stdout, stderr } = await exec(cmd);
  console.log('stdout:', stdout);
  console.error('stderr:', stderr);
}
noder('echo Noder! Ran!');
noder('python rrGetter.py');
