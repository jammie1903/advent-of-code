const fs = require("fs/promises");
const path = require("path");

const target = process.argv[process.argv.length -1].replace(/[^0-9\.]/g, "");
const [day, part = 1] = target.split(".");
if(!day || process.argv.length < 3) {
  console.error("Please specify a target");
  return;
}
async function run() {
  const [code, input] = await Promise.all([
    import(`./src/day-${day}/part${part}.js`),
    fs.readFile(path.join(__dirname, `./src/day-${day}/input.txt`), 'utf8')
  ])
  console.log("Result:", code.default(input))
}

run();
