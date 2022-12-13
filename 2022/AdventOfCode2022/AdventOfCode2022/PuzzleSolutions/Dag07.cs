using AdventOfCode2022.Util;

namespace AdventOfCode2022.PuzzleSolutions;

public class Dag07 : PuzzleSolution
{
    public void SolvePart1()
    {
        var fileTree = BuildFileTree();

        var total = 0;
        foreach (var dirSize in GetDirSize(fileTree.RootDirectory))
        {
            if (dirSize <= 100_000) total += dirSize;
        }

        Console.WriteLine(total);
    }

    public void SolvePart2()
    {
        var fileTree = BuildFileTree();

        var currentUpForDeletion = Int32.MaxValue;
        var amountToDelete = fileTree.RootDirectory.GetSize() - 40_000_000;

        foreach (var dirSize in GetDirSize(fileTree.RootDirectory))
        {
            if (dirSize >= amountToDelete && dirSize < currentUpForDeletion) currentUpForDeletion = dirSize;
        }

        Console.WriteLine(currentUpForDeletion);
    }

    private FileTree BuildFileTree()
    {
        var lines = File.ReadAllLines("../../../Input/Dag07.txt");
        var fileTree = new FileTree {RootDirectory = new Directory("/", null!)};
        var currentDir = fileTree.RootDirectory;
        foreach (var line in lines[1..])
        {
            if (line == "$ ls") continue;
            if (line.StartsWith("$ cd"))
            {
                var dirName = line.Split()[^1];
                if (dirName == "..")
                {
                    currentDir = currentDir.Parent;
                    continue;
                }

                currentDir = currentDir.Subdirectories.Single(n => n.Name == dirName);
            }
            else if (line.StartsWith("dir"))
            {
                var dirName = line.Split()[^1];
                currentDir.Subdirectories.Add(new Directory(dirName, parent: currentDir));
            }
            else
            {
                var fileSize = int.Parse(line.Split()[0]);
                currentDir.SizeOfFilesDirectlyInDir += fileSize;
            }
        }

        return fileTree;
    }

    private IEnumerable<int> GetDirSize(Directory dir)
    {
        foreach (var subDir in dir.Subdirectories)
        {
            yield return subDir.GetSize();
            foreach (var i in GetDirSize(subDir)) yield return i;
        }
    }
}

public class FileTree
{
    public Directory RootDirectory { get; set; }
}

public class Directory
{
    public string Name { get; }
    public List<Directory> Subdirectories { get; }
    public Directory Parent { get; }
    public int SizeOfFilesDirectlyInDir { get; set; }

    public Directory(string name, Directory parent)
    {
        Subdirectories = new List<Directory>();
        Name = name;
        Parent = parent;
    }

    public int GetSize()
    {
        return SizeOfFilesDirectlyInDir + Subdirectories.Sum(dir => dir.GetSize());
    }
}