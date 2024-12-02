const fs = require("fs/promises");
const path = require("path");

const currentYear = 2024;

const target = process.argv[process.argv.length - 1].replace(/[^0-9\.]/g, "");
const testRun = process.argv[process.argv.length - 2].includes("test");
const inputFile = testRun ? "testInput.txt" : "input.txt";
const [day, part = 1] = target.split(".");

if (!day || process.argv.length < 3) {
  console.error("Please specify a target");
  return;
}

async function exists(f) {
  try {
    await fs.stat(f);
    console.log(f, "exists")
    return true;
  } catch (e) {
    console.log(f, "does not exist", e)

    return false;
  }
}

async function run() {

  const filePath = `./src/${currentYear}/day${day}/part${part}`
  const readDataFile = fs.readFile(path.join(__dirname, `./src/${currentYear}/day${day}/${inputFile}`), 'utf8');

  const pyFile = path.join(__dirname,`${filePath}.py`);
  if(await exists(pyFile)) {
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python3', [ pyFile, await readDataFile ]);
    pythonProcess.stdout.on('data', (data) => {
      console.log(String(data))
    });
    pythonProcess.stderr.on('data', (data) => {
      console.error("Error:", String(data));
    });
  } else {
    const [code, input] = await Promise.all([
      import(`${filePath}.js`),
      readDataFile
    ])
    console.log("Result:", code.default(input))
  }
}

run();
