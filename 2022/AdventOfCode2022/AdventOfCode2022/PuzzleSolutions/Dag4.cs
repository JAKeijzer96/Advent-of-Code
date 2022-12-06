using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag4 : PuzzleSolution
{
    public void SolvePart1()
    {
        Console.WriteLine(
            File.ReadAllLines("../../../Input/Dag04.txt")
                .Select(line => new
                {
                    Left = Array.ConvertAll(line.Split(",")[0].Split("-"), int.Parse),
                    Right = Array.ConvertAll(line.Split(",")[1].Split("-"), int.Parse)
                })
                .Count(obj => obj.Left[0] >= obj.Right[0] && obj.Left[1] <= obj.Right[1] /*Left contained in Right*/ ||
                              obj.Left[0] <= obj.Right[0] && obj.Left[1] >= obj.Right[1] /*Right contained in Left*/));
    }

    public void SolvePart2()
    {
        Console.WriteLine(
            File.ReadAllLines("../../../Input/Dag04.txt")
                .Select(line => new
                {
                    Left = Array.ConvertAll(line.Split(",")[0].Split("-"), int.Parse),
                    Right = Array.ConvertAll(line.Split(",")[1].Split("-"), int.Parse)
                })
                .Count(obj => obj.Left[0] <= obj.Right[0] && obj.Left[1] >= obj.Right[0] /*3-35,31-34*/ ||
                              obj.Left[0] >= obj.Right[0] && obj.Left[0] <= obj.Right[1] /*11-98,9-12*/));
    }
}