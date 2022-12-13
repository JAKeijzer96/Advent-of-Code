using System.Diagnostics;
using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag08 : PuzzleSolution
{
    private int[,] _arr = null!;
    private int _lineLength;
    
    public void SolvePart1()
    {
        ReadFileInto2DArray();
        
        var stopwatch = new Stopwatch();
        stopwatch.Start();
        var treesOnPerimeter = 4 * (_lineLength - 1);
        var visibleInteriorTrees = 0;
        var highestTreesUp = Enumerable.Range(0, _lineLength).Select(col => _arr[0, col]).ToArray();
        for (var row = 1; row < _lineLength - 1; row++)
        {
            var highestTreeToTheLeft = _arr[row, 0];
            for (var col = 1; col < _lineLength - 1; col++)
            {
                var currentTree = _arr[row, col];
                // Check to the left (fast)
                if (currentTree > highestTreeToTheLeft)
                {
                    highestTreeToTheLeft = currentTree;
                    visibleInteriorTrees++;
                    if (currentTree > highestTreesUp[col]) // don't forget to update highestTreesUp _array
                    {
                        highestTreesUp[col] = currentTree;
                    }
                    continue;
                }
                // Check up (fast)
                if (currentTree > highestTreesUp[col])
                {
                    highestTreesUp[col] = currentTree;
                    visibleInteriorTrees++;
                    continue;
                }
                // Check to the right (slow)
                var highestTreeToTheRight = _arr[row, _lineLength - 1];
                for (var i = col + 1; i < _lineLength; i++)
                {
                    if (_arr[row, i] > highestTreeToTheRight)
                    {
                        highestTreeToTheRight = _arr[row, i];
                    }
                }
                if (currentTree > highestTreeToTheRight)
                {
                    visibleInteriorTrees++;
                    continue;
                }
                // Check down (slow)
                var highestTreeDown = _arr[_lineLength - 1, col];
                for (var i = row + 1; i < _lineLength; i++)
                {
                    if (_arr[i, col] > highestTreeDown)
                    {
                        highestTreeDown = _arr[i, col];
                    }
                }
                if (currentTree > highestTreeDown)
                {
                    visibleInteriorTrees++;
                }
            }
        }

        stopwatch.Stop();
        Console.WriteLine($"Elapsed milliseconds: {stopwatch.ElapsedMilliseconds}");
        Console.WriteLine($"Total visible trees: {visibleInteriorTrees + treesOnPerimeter}");
    }

    public void SolvePart2()
    {
        ReadFileInto2DArray();
        
        var stopwatch = new Stopwatch();
        stopwatch.Start();
        var highestScenicScore = 0;

        for (var row = 0; row < _lineLength; row++)
        {
            for (var col = 0; col < _lineLength; col++)
            {
                var viewingDistanceLeft = 0;
                var viewingDistanceRight = 0;
                var viewingDistanceUp = 0;
                var viewingDistanceDown = 0;
                var currentTree = _arr[row, col];
                // check left
                for (var i = col - 1; i >= 0; i--)
                {
                    viewingDistanceLeft++;
                    if (_arr[row, i] >= currentTree)
                    {
                        break;
                    }
                }
                // check right
                for (var i = col + 1; i < _lineLength; i++)
                {
                    viewingDistanceRight++;
                    if (_arr[row, i] >= currentTree)
                    {
                        break;
                    }
                }
                // check up
                for (var i = row - 1; i >= 0; i--)
                {
                    viewingDistanceUp++;
                    if (_arr[i, col] >= currentTree)
                    {
                        break;
                    }
                }
                // check down
                for (var i = row + 1; i < _lineLength; i++)
                {
                    viewingDistanceDown++;
                    if (_arr[i, col] >= currentTree)
                    {
                        break;
                    }
                }

                var scenicScore = viewingDistanceLeft * viewingDistanceRight * viewingDistanceUp * viewingDistanceDown;
                if (scenicScore > highestScenicScore)
                {
                    highestScenicScore = scenicScore;
                }
            }
        }
        
        stopwatch.Stop();
        Console.WriteLine($"Elapsed milliseconds: {stopwatch.ElapsedMilliseconds}");
        Console.WriteLine($"Highest scenic score: {highestScenicScore}");
    }

    private void ReadFileInto2DArray()
    {
        var lines = File.ReadAllLines("../../../Input/Dag08.txt");
        _lineLength = lines[0].Length;
        _arr = new int[_lineLength, _lineLength];
        for (var row = 0; row < _lineLength; row++)
        {
            for (var col = 0; col < _lineLength; col++)
            {
                _arr[row, col] = lines[row][col] - '0';
            }
        }
    }
}