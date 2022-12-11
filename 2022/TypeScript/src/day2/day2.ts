import fs from "node:fs";
import path from "node:path";

export default function (): Array<number> {
    let input: Array<string>;

    function readInput(): void {
        const inputFile = path.join(global.inputRoot, "day2");
        input = fs.readFileSync(inputFile, "utf-8").split(/\r?\n/g);
    }

    function part1(): number {
        const score_index = new Map<string, number>([
            ["A X", 1 + 3], ["A Y", 2 + 6], ["A Z", 3 + 0],
            ["B X", 1 + 0], ["B Y", 2 + 3], ["B Z", 3 + 6],
            ["C X", 1 + 6], ["C Y", 2 + 0], ["C Z", 3 + 3],
        ]);

        return input.reduce((accumulator, current) => accumulator += score_index.get(current)!, 0);
    }

    function part2(): number {
        const score_index = new Map<string, number>([
            ["A X", 3 + 0], ["A Y", 1 + 3], ["A Z", 2 + 6],
            ["B X", 1 + 0], ["B Y", 2 + 3], ["B Z", 3 + 6],
            ["C X", 2 + 0], ["C Y", 3 + 3], ["C Z", 1 + 6],
        ]);

        return input.reduce((accumulator, current) => accumulator += score_index.get(current)!, 0);
    }

    readInput();
    const results = [part1(), part2()];

    return results;
}