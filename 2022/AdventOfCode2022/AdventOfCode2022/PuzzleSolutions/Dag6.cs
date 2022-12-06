using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag6 : PuzzleSolution
{
    public void SolvePart1()
    {
        var input = File.ReadAllText("../../../Input/Dag06.txt").TrimEnd();
        FindDistinctLetters(input, 4, out var letters, out var position);
        Console.WriteLine($"Found '{letters}' at position {position}");
    }

    public void SolvePart2()
    {
        var input = File.ReadAllText("../../../Input/Dag06.txt").TrimEnd();
        FindDistinctLetters(input, 14, out var letters, out var position);
        Console.WriteLine($"Found '{letters}' at position {position}");
    }

    private static void FindDistinctLetters(string input, int amountOfLetters, out string letters, out int position)
    {
        position = amountOfLetters - 1;
        letters = input[..position];
        foreach (var character in input[position..])
        {
            letters += character;
            position++;
            if (letters.Distinct().Count() == amountOfLetters) break;
            letters = letters.Substring(1);
        }
    }
}