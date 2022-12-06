import fs from "node:fs";
import path from "node:path";

import CleaningSection from "./CleaningSection.js";

export default function (): Array<number> {
    const input: Array<[CleaningSection, CleaningSection]> = new Array();

    function readInput(): void {
        const inputPath = path.join(global.inputRoot, "day4");
        const fileContent = fs.readFileSync(inputPath, "utf-8");
        fileContent.split("\n").forEach((row: string) => {
            const groups = row.split(",").map(group => group.split("-").map(g => Number.parseInt(g)));
            const first_elf = new CleaningSection(groups[0][0], groups[0][1]);
            const second_elf = new CleaningSection(groups[1][0], groups[1][1]);
            input.push([first_elf, second_elf]);
        });
    }

    function part1(): number {
        let full_overlap_count = 0;
        input.forEach(group => {
            if (
                (group[0].start <= group[1].start && group[0].end >= group[1].end)
                || (group[1].start <= group[0].start && group[1].end >= group[0].end)
            ) {
                full_overlap_count++;
            }
        });

        return full_overlap_count;
    }

    function part2(): number {
        let partial_overlap_count = 0;
        input.forEach(group => {
            if (
                (group[0].end >= group[1].start && group[1].start >= group[0].start)
                || (group[1].end >= group[0].start && group[0].start >= group[1].start)
            ) {
                partial_overlap_count++;
            }
        });

        return partial_overlap_count;
    }

    readInput();
    const results = [part1(), part2()];

    return results;
}