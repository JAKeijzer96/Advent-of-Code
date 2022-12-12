using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag11 : PuzzleSolution
{
    private Monkey[] _monkeys = null!;
    private int _productOfDivisors;

    public void SolvePart1()
    {
        CreateMonkeyList();
        for (var i = 0; i < 20; i++)
        {
            foreach (var monkey in _monkeys)
            {
                while (monkey.Items.Count > 0)
                {
                    var nextItem = monkey.Items.Dequeue();
                    var operatedItem = monkey.Operate(nextItem);
                    var itemDividedByThree = operatedItem / 3;
                    var monkeyToThrowTo = monkey.Test(itemDividedByThree);
                    _monkeys[monkeyToThrowTo].Items.Enqueue(itemDividedByThree);
                    monkey.OperatedItems++;
                }
            }
        }

        var top2 = _monkeys.Select(m => m.OperatedItems).OrderByDescending(n => n).Take(2).ToList();
        Console.WriteLine($"Monkey business after 20 rounds: {top2[0] * top2[1]}");
    }

    public void SolvePart2()
    {
        CreateMonkeyList();

        for (var i = 0; i < 10_000; i++)
        {
            foreach (var monkey in _monkeys)
            {
                while (monkey.Items.Count > 0)
                {
                    var nextItem = monkey.Items.Dequeue();
                    var operatedItem = monkey.Operate(nextItem);
                    var monkeyToThrowTo = monkey.Test(operatedItem);
                    operatedItem %= _productOfDivisors;
                    _monkeys[monkeyToThrowTo].Items.Enqueue(operatedItem);
                    monkey.OperatedItems++;
                }
            }
        }

        var top2 = _monkeys.Select(m => m.OperatedItems).OrderByDescending(n => n).Take(2).ToList();
        Console.WriteLine(
            $"Monkey business after 10_000 rounds: {Convert.ToInt64(top2[0]) * Convert.ToInt64(top2[1])}");
    }

    private void CreateMonkeyList()
    {
        var text = File.ReadAllText("../../../Input/Dag11.txt");
        var monkeyDescriptions = text.Split("\n\n");
        var monkeys = new List<Monkey>();
        var productOfDivisors = 1;
        foreach (var description in monkeyDescriptions)
        {
            var descriptionLines = description.Split("\n");
            var id = int.Parse(descriptionLines[0].Split()[1][..^1]);
            var items = new Queue<long>(Array.ConvertAll(descriptionLines[1].Split(": ")[1].Split(", "), long.Parse));
            var operationAsText = descriptionLines[2].Split("= old ")[1];
            Func<long, long> operate = null!;
            if (operationAsText.StartsWith("*"))
            {
                if (operationAsText.EndsWith("old"))
                {
                    operate = old => old * old;
                }
                else
                {
                    operate = old => old * int.Parse(operationAsText[2..]);
                }
            }
            else if (operationAsText.StartsWith("+"))
            {
                operate = old => old + int.Parse(operationAsText[2..]);
            }

            var divisibleBy = int.Parse(descriptionLines[3].Split("divisible by ")[1]);
            var monkeyIdIfTrue = int.Parse(descriptionLines[4].Split("monkey ")[1]);
            var monkeyIdIfFalse = int.Parse(descriptionLines[5].Split("monkey ")[1]);
            Func<long, int> test = value => value % divisibleBy == 0 ? monkeyIdIfTrue : monkeyIdIfFalse;
            var monkey = new Monkey
            {
                Id = id,
                Items = items,
                Operate = operate,
                Test = test
            };
            productOfDivisors *= divisibleBy;
            monkeys.Add(monkey);
        }

        _productOfDivisors = productOfDivisors;
        _monkeys = monkeys.ToArray();
    }
}

class Monkey
{
    public int Id { get; set; }
    public Queue<long> Items { get; set; }
    public Func<long, long> Operate { get; set; }
    public Func<long, int> Test { get; set; }
    public int OperatedItems { get; set; } = 0;
}