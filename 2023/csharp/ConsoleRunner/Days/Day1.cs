namespace ConsoleRunner.Days;

public sealed class Day1 : DayBase
{
    private readonly string[] _lines;

    public Day1() => _lines = File.ReadAllLines("Inputs/day1.txt");

    public override (long Part1, long Part2) Calculate() => (Part1(), Part2());

    // private long Part1(in string[] input) =>
    //     input.Select(l =>
    //         {
    //             char[] digits = l.Where(char.IsDigit).ToArray();
    //             
    //             return digits.Length == 0 ? 0 : int.Parse($"{digits.First()}{digits.Last()}");
    //         })
    //         .Sum(n => n);

    private long Part1() => _lines
        .Select(l => l.Where(char.IsDigit).ToArray())
        .Sum(d => d.Length > 0 ? int.Parse($"{d.First()}{d.Last()}") : 0);

    private long Part2() => _lines.Select(GetNumberFromMixedFormat).Sum(n => n);

    private static int GetNumberFromMixedFormat(string number)
    {
        Dictionary<string, char> numbersWritten = new()
        {
            { "one", '1' },
            { "two", '2' },
            { "three", '3' },
            { "four", '4' },
            { "five", '5' },
            { "six", '6' },
            { "seven", '7' },
            { "eight", '8' },
            { "nine", '9' },
        };

        List<char> digits = [];
        for (int i = 0; i < number.Length; i++)
        {
            if (char.IsDigit(number[i]))
                digits.Add(number[i]);

            // Check if the substring matches any number in written form
            foreach (var numberWritten in numbersWritten)
                if (number[i..].StartsWith(numberWritten.Key))
                    digits.Add(numberWritten.Value);
        }

        return int.Parse($"{digits.First()}{digits.Last()}");
    }
}
