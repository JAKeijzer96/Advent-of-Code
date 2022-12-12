using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag9 : PuzzleSolution
{
    public void SolvePart1()
    {
        // Read file into 2D array
        var lines = File.ReadAllLines("../../../Input/Dag09.txt");
        var vert = 0;
        var furthestUp = 0;
        var furthestDown = 0;
        var hor = 0;
        var furthestLeft = 0;
        var furthestRight = 0;
        foreach (var line in lines)
        {
            var splitLine = line.Split();
            var direction = splitLine[0];
            var steps = int.Parse(splitLine[1]);
            switch (direction)
            {
                case "U":
                    vert -= steps;
                    if (vert < furthestUp) furthestUp = vert;
                    break;
                case "D":
                    vert += steps;
                    if (vert > furthestDown) furthestDown = vert;
                    break;
                case "L":
                    hor -= steps;
                    if (hor < furthestLeft) furthestLeft = hor;
                    break;
                case "R":
                    hor += steps;
                    if (hor > furthestRight) furthestRight = hor;
                    break;
            }
        }

        Console.WriteLine(furthestUp);
        Console.WriteLine(furthestDown);
        Console.WriteLine(furthestLeft);
        Console.WriteLine(furthestRight);

        var amountOfRows = furthestDown - furthestUp + 1;
        var amountOfCols = furthestRight - furthestLeft + 1;
        var arr = new int[amountOfRows, amountOfCols];
        var headRow = -furthestUp;
        var headCol = -furthestLeft;
        var tailRow = headRow;
        var tailCol = headCol;
        Console.WriteLine(headRow);
        Console.WriteLine(headCol);
        
        // Start solving
        arr[tailRow, tailCol]++; // Mark starting position as visited
        foreach (var line in lines)
        {
            var splitLine = line.Split();
            var direction = splitLine[0];
            var steps = int.Parse(splitLine[1]);
            while (steps > 0)
            {
                switch (direction)
                {
                    case "U":
                        headRow--;
                        if (tailRow - headRow > 1)
                        {
                            tailRow--;
                            if (tailCol < headCol)
                            {
                                tailCol++;
                            }
                            else if (tailCol > headCol)
                            {
                                tailCol--;
                            }
                            arr[tailRow, tailCol]++;
                        }
                        break;
                    case "D":
                        headRow++;
                        if (headRow - tailRow > 1)
                        {
                            tailRow++;
                            if (tailCol < headCol)
                            {
                                tailCol++;
                            }
                            else if (tailCol > headCol)
                            {
                                tailCol--;
                            }
                            arr[tailRow, tailCol]++;
                        }
                        break;
                    case "L":
                        headCol--;
                        if (tailCol - headCol > 1)
                        {
                            tailCol--;
                            if (tailRow < headRow)
                            {
                                tailRow++;
                            }
                            else if (tailRow > headRow)
                            {
                                tailRow--;
                            }
                            arr[tailRow, tailCol]++;
                        }
                        break;
                    case "R":
                        headCol++;
                        if (headCol - tailCol > 1)
                        {
                            tailCol++;
                            if (tailRow < headRow)
                            {
                                tailRow++;
                            }
                            else if (tailRow > headRow)
                            {
                                tailRow--;
                            }
                            arr[tailRow, tailCol]++;
                        }
                        break;
                    default:
                        Console.WriteLine($"Error: can't parse line:  {{{line}}}.");
                        break;
                }

                steps--;
            }
        }

        var visitedPlaces = 0;
        for (int row = 0; row < arr.GetLength(0); row++)
        {
            for (int col = 0; col < arr.GetLength(1); col++)
            {
                if (arr[row, col] > 0)
                {
                    visitedPlaces++;
                }
            }
        }

        Console.WriteLine(visitedPlaces);
    }

    public void SolvePart2()
    {
    }
}