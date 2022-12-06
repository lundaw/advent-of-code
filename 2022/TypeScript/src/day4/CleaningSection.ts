class CleaningSection {
    start: number;
    end: number;

    constructor(start: number, end: number) {
        if (start <= 0) {
            throw RangeError("Start section must be at least 1");
        }

        if (end < start) {
            throw RangeError("End section cannot be lower than start");
        }

        this.start = start;
        this.end = end;
    }
}

export default CleaningSection;