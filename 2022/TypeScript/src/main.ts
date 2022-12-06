import path from "node:path";
import { fileURLToPath } from "node:url";

global.year = 2022;
global.appRoot = path.dirname(fileURLToPath(import.meta.url));
global.inputRoot = path.join(global.appRoot, "..", "..", "..", "_inputs", global.year.toString());

console.log("---- Advent of Code 2022 TypeScript solutions")
for(let i = 1; i <= 25; i++) {
    const modulePath = `./day${i}/day${i}.js`;
    try {
        const module = await import(modulePath);
        const results = module.default();
        console.log(`Day ${i}: (${results[0]}, ${results[1]})`);
    }
    catch (exception) {
        if (exception instanceof Error && exception.code === "ERR_MODULE_NOT_FOUND") {
            continue;
        }
        else {
            throw exception;
        }
    }
}