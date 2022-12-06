import fs from "node:fs";
import path from "node:path";

export default function (): Array<number> {
    const input: Array<number> = new Array();

    function readInput(): void {
        const inputPath = path.join(global.inputRoot, "day1");
        const fileContent = fs.readFileSync(inputPath, "utf-8");
        const tempCalorieSum = new Array<number>();

        fileContent.split(/\r?\n\r?\n/g).forEach(elfGroup => {
            const calorieCount = elfGroup.split(/\r?\n/g)
                .map(calorie => parseInt(calorie))
                .reduce((accumulator, current) => accumulator += current);
            tempCalorieSum.push(calorieCount);
        });
        tempCalorieSum.sort((a, b) => b - a).forEach(calorieSum => input.push(calorieSum));
    }

    function part1(): number {
        return input[0];
    }

    function part2(): number {
        return input[0] + input[1] + input[2];
    }

    readInput();
    const results = [part1(), part2()];

    return results;
}