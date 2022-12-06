import fs from "node:fs";
import path from "node:path";

export default function (): Array<number> {
    let input: string;

    function readInput(): void {
        const inputFile = path.join(global.inputRoot, "day6");
        input = fs.readFileSync(inputFile, "utf-8");
    }

    function part1(): number {
        return find_correct_subset(4);
    }

    function part2(): number {
        return find_correct_subset(14);
    }

    function find_correct_subset(length: number): number {
        if (length <= 0) {
            throw RangeError(`Subset length ${length} is invalid`);
        }

        for (let i = 0; i < input.length - length; i++) {
            const subset = new Set(input.slice(i, i + length).split(""));
            if (subset.size == length) {
                return i + length;
            }
        }

        throw Error(`Somehow there was no matching subset with length of ${length}`);
    }

    readInput();
    const results = [part1(), part2()];
    
    return results;
}