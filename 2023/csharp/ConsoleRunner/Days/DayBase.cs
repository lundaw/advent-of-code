namespace ConsoleRunner.Days;

public abstract class DayBase
{
    public (long Part1, long Part2) Calculate() => (Part1(), Part2());

    protected abstract long Part1();

    protected abstract long Part2();
}
