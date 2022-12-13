using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag01 : PuzzleSolution
{
    public void SolvePart1()
    {
        Console.WriteLine(
            File.ReadAllText("../../../Input/Dag01.txt")
                .Trim()
                .Split("\n\n")
                .Select(blocks => Array.ConvertAll(blocks.Split("\n"), int.Parse).Sum())
                .Max());
    }

    public void SolvePart2()
    {
        Console.WriteLine(
            File.ReadAllText("../../../Input/Dag01.txt")
                .Trim()
                .Split("\n\n")
                .Select(blocks => Array.ConvertAll(blocks.Split("\n"), int.Parse).Sum())
                .OrderByDescending(n => n)
                .Take(3)
                .Sum());
    }
}