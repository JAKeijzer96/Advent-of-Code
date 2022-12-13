using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions
{
    public class Dag09 : PuzzleSolution
    {
        // After a few hours of debugging my own solution and not finding the fix that caused the result for part 2
        // to be slightly off, I shamelessly stole https://github.com/ShootMe/AdventOfCode/blob/main/Y2022/Puzzle09.cs
        // and modified it to fit my own style of coding
        
        public void SolvePart1()
        {
            Console.WriteLine($"Rope length 2: Tail visited {CountPositionsTailVisisted(2)} positions");
        }

        public void SolvePart2()
        {
            Console.WriteLine($"Rope length 10: Tail visited {CountPositionsTailVisisted(10)} positions");
        }

        private int CountPositionsTailVisisted(int ropeLength)
        {
            var lines = File.ReadAllLines("../../../Input/Dag09.txt");

            HashSet<(int x, int y)> positions = new();
            List<(int x, int y)> rope = new();
            for (var i = 0; i < ropeLength; i++)
            {
                rope.Add((0, 0));
            }

            foreach (var line in lines)
            {
                var splitLine = line.Split();
                var direction = splitLine[0];
                var steps = int.Parse(splitLine[1]);
                var xChange = direction switch {"R" => 1, "L" => -1, _ => 0};
                var yChange = direction switch {"U" => 1, "D" => -1, _ => 0};

                while (steps > 0)
                {
                    rope[0] = (rope[0].x + xChange, rope[0].y + yChange);

                    for (var i = 1; i < rope.Count; i++)
                    {
                        var diffX = rope[i - 1].x - rope[i].x;
                        var diffY = rope[i - 1].y - rope[i].y;
                        if (Math.Abs(diffX) > 1 || Math.Abs(diffY) > 1)
                        {
                            rope[i] = (
                                rope[i].x + Math.Sign(diffX),
                                rope[i].y + Math.Sign(diffY)
                            );
                        }
                    }

                    positions.Add(rope[^1]);
                    steps--;
                }
            }

            return positions.Count;
        }
    }
}