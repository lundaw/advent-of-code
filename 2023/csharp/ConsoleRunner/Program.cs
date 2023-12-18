using System.Diagnostics;
using ConsoleRunner.Days;

var stopwatch = new Stopwatch();

var days = typeof(DayBase).Assembly.GetExportedTypes().Where(t => !t.IsAbstract)
    .OrderBy(d => int.Parse(d.Name.Where(char.IsDigit).ToArray()))
    .ToArray();
for (var i = 0; i < days.Length; i++)
{
    var dayInstance = (DayBase)Activator.CreateInstance(days[i])!;

    stopwatch.Start();
    var results = dayInstance.Calculate();
    stopwatch.Stop();

    Console.WriteLine($"Day {i + 1}: {results}; time: {stopwatch.ElapsedMilliseconds} ms");
    stopwatch.Reset();
}
