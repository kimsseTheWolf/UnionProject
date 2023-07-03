const compiler = require("./compiler")

compiler.compileScriptV1("./target.json", compiler.TOP_LEVEL).then(r => console.log(r))