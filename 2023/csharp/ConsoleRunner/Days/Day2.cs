namespace ConsoleRunner.Days;

internal readonly record struct SimpleGame(int Id, List<Cubes> Cubes);

internal readonly record struct Cubes(string Color, int Count);

public sealed class Day2 : DayBase
{
    private const int P1_MAX_RED = 12;
    private const int P1_MAX_GREEN = 13;
    private const int P1_MAX_BLUE = 14;

    private readonly List<SimpleGame> _games;

    public Day2()
    {
        _games = File.ReadAllLines("Inputs/day2.txt")
            .Select(
                l => l.Split(':')[1]
                    .Split(';')
                    .SelectMany(
                        s => s.Split(',', StringSplitOptions.TrimEntries)
                            .Select(c => c.Split(' '))
                    )
                    .Select(s => new Cubes(s[1], int.Parse(s[0])))
                    .ToList()
            )
            .Select((g, index) => new SimpleGame(index + 1, g))
            .ToList();
    }

    protected override long Part1() => _games.Where(IsValidGame).Sum(g => g.Id);

    protected override long Part2() =>
        _games.Select(g => new
            {
                Red = g.Cubes.Where(c => c.Color == "red").Max(c => c.Count),
                Green = g.Cubes.Where(c => c.Color == "green").Max(c => c.Count),
                Blue = g.Cubes.Where(c => c.Color == "blue").Max(c => c.Count),
            })
            .Sum(g => g.Red * g.Green * g.Blue);

    private static bool IsValidGame(SimpleGame game)
    {
        foreach (Cubes cubes in game.Cubes)
        {
            switch (cubes)
            {
                case { Color: "red", Count: > P1_MAX_RED }:
                case { Color: "green", Count: > P1_MAX_GREEN }:
                case { Color: "blue", Count: > P1_MAX_BLUE }:
                    return false;
            }
        }

        return true;
    }
}
