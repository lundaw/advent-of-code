import fs from "node:fs";
import path from "node:path";

export default function (): Array<number> {
    let input: Array<string> = new Array();

    function readInput(): void {
        const inputPath = path.join(global.inputRoot, "day3");
        input = fs.readFileSync(inputPath, "utf-8").split(/\r?\n/gm);
    }

    function part1(): number {
        let priorities_sum = 0;

        for (let i = 0; i < input.length; i++) {
            const half_length = Math.floor(input[i].length / 2);
            const first_part = new Set(input[i].slice(0, half_length));
            const second_part = new Set(input[i].slice(half_length));
            const intersect = Array.from(new Set([...first_part].filter(i => second_part.has(i))));

            if (intersect.length > 1) {
                throw Error("Intersection unexpectedly had more than 1 elements!");
            }
            priorities_sum += intersect[0].charCodeAt(0) - (intersect[0] === intersect[0].toUpperCase() ? 38 : 96);
        }

        return priorities_sum;
    }

    function part2(): number {
        let priorities_sum = 0;

        for (let i = 0; i < input.length; i += 3) {
            const groups = input.slice(i, i + 3).map(group => new Set(group));
            const intersect = Array.from(new Set([...groups[0]].filter(i => groups[1].has(i) && groups[2].has(i))));
            
            if (intersect.length > 1) {
                throw Error("Intersection unexpectedly had more than 1 elements!");
            }
            priorities_sum += intersect[0].charCodeAt(0) - (intersect[0] === intersect[0].toUpperCase() ? 38 : 96);
        }

        return priorities_sum;
    }

    readInput();
    const results = [part1(), part2()];

    return results;
}