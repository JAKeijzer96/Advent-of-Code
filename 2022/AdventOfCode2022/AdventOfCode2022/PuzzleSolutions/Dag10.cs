using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag10 : PuzzleSolution
{
    public void SolvePart1()
    {
        var lines = File.ReadAllLines("../../../Input/Dag10.txt");
        var currentCycle = 0;
        var registerValue = 1;
        var sumOfSignalStrength = 0;
        foreach (var line in lines)
        {
            if (line == "noop")
            {
                currentCycle++;
                if ((currentCycle - 20) % 40 == 0)
                {
                    var signalStrength = currentCycle * registerValue;
                    sumOfSignalStrength += signalStrength;
                }
            }
            else
            {
                currentCycle++;
                if ((currentCycle - 20) % 40 == 0)
                {
                    var signalStrength = currentCycle * registerValue;
                    sumOfSignalStrength += signalStrength;
                }
                currentCycle++;
                if ((currentCycle - 20) % 40 == 0)
                {
                    var signalStrength = currentCycle * registerValue;
                    sumOfSignalStrength += signalStrength;
                }
                var valueToAdd = int.Parse(line.Split()[1]);
                registerValue += valueToAdd;
            }
        }

        Console.WriteLine($"Sum of signal strength: {sumOfSignalStrength}");
    }

    public void SolvePart2()
    {
        var lines = File.ReadAllLines("../../../Input/Dag10.txt");
        var currentCycle = 0;
        var registerValue = 1;
        var crtScreen = new char[241];
        foreach (var line in lines)
        {
            if (line == "noop")
            {
                currentCycle++;
                var shouldDrawPixel = registerValue - 1 <= currentCycle % 40 && currentCycle % 40 <= registerValue + 1;
                crtScreen[currentCycle] = shouldDrawPixel ? '#' : '.';
            }
            else
            {
                currentCycle++;
                var shouldDrawPixel = registerValue - 1 <= currentCycle % 40 && currentCycle % 40 <= registerValue + 1;
                crtScreen[currentCycle] = shouldDrawPixel ? '#' : '.';
                
                currentCycle++;
                
                var valueToAdd = int.Parse(line.Split()[1]);
                registerValue += valueToAdd;
                
                shouldDrawPixel = registerValue - 1 <= currentCycle % 40 && currentCycle % 40 <= registerValue + 1;
                crtScreen[currentCycle] = shouldDrawPixel ? '#' : '.';
            }
        }

        Console.WriteLine("CRT output:");
        for (var i = 0; i < 240; i++)
        {
            if (i > 0 && i % 40 == 0)
            {
                Console.WriteLine();
            }
            Console.Write(crtScreen[i]);
        }
        Console.WriteLine();
        Console.WriteLine("RZHFGJCB");
    }
}