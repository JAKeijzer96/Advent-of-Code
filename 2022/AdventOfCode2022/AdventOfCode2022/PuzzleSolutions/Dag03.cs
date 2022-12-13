using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag03 : PuzzleSolution
{
    public void SolvePart1()
    {
        Console.WriteLine(
            File.ReadAllLines("../../../Input/Dag03.txt")
                .Select(line => line.Trim().Insert(line.Length / 2, "|").Split("|")) /*Split string in half*/
                .Select(splitLine => splitLine[0].First(character => splitLine[1].Contains(character)))
                .Select(character => char.IsUpper(character) ? character - 38 : character - 96)
                .Sum());
    }

    public void SolvePart2()
    {
        /* Credits voor Intersect inspiratie: https://github.com/rversteeg/AdventOfCode2020/blob/main/Y2022/Day03.cs */
        Console.WriteLine(
            Enumerable.Range(0, File.ReadAllLines("../../../Input/Dag03.txt").Length / 3)
                .Select(n =>
                    File.ReadAllLines("../../../Input/Dag03.txt")[3 * n]
                        .Intersect(File.ReadAllLines("../../../Input/Dag03.txt")[3 * n + 1])
                        .Intersect(File.ReadAllLines("../../../Input/Dag03.txt")[3 * n + 2])
                        .Single())
                .Select(c => char.IsUpper(c) ? c - 38 : c - 96)
                .Sum());
        /* Dag 3 deel 2 versie 2: Comprehension syntax */
        Console.WriteLine(
            (from n in Enumerable.Range(0, File.ReadAllLines("../../../Input/Dag03.txt").Length / 3)
                let input = File.ReadAllLines("../../../Input/Dag03.txt")
                let character = input[3 * n].Intersect(input[3 * n + 1]).Intersect(input[3 * n + 2]).Single()
                select char.IsUpper(character) ? character - 38 : character - 96)
            .Sum());
    }
}