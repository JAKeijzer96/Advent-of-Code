﻿using AdventOfCode2022.PuzzleSolutions;
using AdventOfCode2022.Util;

namespace AdventOfCode2022;

public static class Program
{
    static void Main(string[] args)
    {
        PuzzleSolution puzzleSolution = new Dag09();
        puzzleSolution.SolvePart1();
        puzzleSolution.SolvePart2();
    }
}