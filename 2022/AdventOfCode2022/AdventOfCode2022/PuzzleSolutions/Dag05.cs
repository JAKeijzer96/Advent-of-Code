using System.Text.RegularExpressions;
using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag05 : PuzzleSolution
{
    public void SolvePart1()
    {
        ReadFile(out string instructions, out string crates);
        var stacks = CreateStacksFromInput(crates);
        Console.WriteLine(MoveCrates(instructions, stacks, retainOrder: false));
    }

    public void SolvePart2()
    {
        ReadFile(out string instructions, out string crates);
        var stacks = CreateStacksFromInput(crates);
        Console.WriteLine(MoveCrates(instructions, stacks, retainOrder: true));
    }

    private void ReadFile(out string instructions, out string crates)
    {
        var input = File.ReadAllText("../../../Input/Dag05.txt").TrimEnd();
        var split = input.Split("\n\n");
        instructions = split[1];
        crates = split[0];
    }

    // Should work for any height and amount of initial stacks
    private static Stack<char>[] CreateStacksFromInput(string cratesString)
    {
        var splitCrates = cratesString.Split("\n");
        var lineWidth = splitCrates[^1].Length;
        var amountOfStacks = splitCrates[^1].Trim().Split("   ").Length;
        var stacks = new Stack<char>[amountOfStacks].Select(_ => new Stack<char>()).ToArray();
        for (var crateRow = 2; crateRow <= splitCrates.Length; crateRow++)
        {
            var stackToAddTo = 0;
            for (var crateColumn = 1; crateColumn < lineWidth; crateColumn += 4)
            {
                var letter = splitCrates[^crateRow][crateColumn];
                if (!char.IsWhiteSpace(letter)) stacks[stackToAddTo].Push(letter);
                stackToAddTo++;
            }
        }

        return stacks;
    }

    private string MoveCrates(string instructions, Stack<char>[] stacks, bool retainOrder)
    {
        foreach (var instruction in instructions.Split("\n"))
        {
            var match = Regex.Match(instruction, @"^move (\d+) from (\d+) to (\d+)$");
            var amountToMove = int.Parse(match.Groups[1].Value);
            var fromStack = int.Parse(match.Groups[2].Value);
            var toStack = int.Parse(match.Groups[3].Value);

            var tempStack = new Stack<char>();
            while (amountToMove > 0)
            {
                var item = stacks[fromStack - 1].Pop();
                if (retainOrder) tempStack.Push(item);
                else stacks[toStack - 1].Push(item);
                amountToMove--;
            }

            if (!retainOrder) continue;

            while (tempStack.TryPop(out var item)) stacks[toStack - 1].Push(item);
        }

        return stacks.Aggregate("", (current, stack) => current + stack.Pop());
    }
}