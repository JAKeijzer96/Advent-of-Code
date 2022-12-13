using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag02 : PuzzleSolution
{
    public void SolvePart1()
    {
        Console.WriteLine(
            File.ReadAllLines("../../../Input/Dag02.txt")
                .Select(line => line.Split())
                .Select(splitLine => new
                {
                    TheirLetter = char.Parse(splitLine[0]),
                    MyLetter = (char) (char.Parse(splitLine[1]) - 23) /*X->A,Y->B,Z->C*/
                })
                .Select(obj =>
                    obj.MyLetter - 64 + ((obj.TheirLetter - 64) % 3 + 1 == obj.MyLetter - 64 ? 6 /*Win*/
                        : obj.TheirLetter == obj.MyLetter ? 3 /*Draw*/ : 0 /*Loss*/))
                .Sum());
    }

    public void SolvePart2()
    {
        Console.WriteLine(
            File.ReadAllLines("../../../Input/Dag02.txt")
                .Select(line => line.Split())
                .Select(splitLine => new
                {
                    TheirLetter = char.Parse(splitLine[0]), MyLetter = char.Parse(splitLine[1])
                })
                .Select(
                    obj => obj.MyLetter == 'Z' ? 6 + (obj.TheirLetter - 64) % 3 + 1 /*Win*/
                        : obj.MyLetter == 'Y' ? 3 + obj.TheirLetter - 64 /*Draw*/
                        : obj.TheirLetter % 3 + 1 /*Loss*/)
                .Sum());
    }
}