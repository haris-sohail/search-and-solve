# search-and-solve

Implementation of BFS, UCS and DFS

## Graph structure

- The vertices and their parents (called as parent sets) are read from `data0.txt` 

- All of the vertices are read and made into objects like these:

![vertices-objects](https://github.com/haris-sohail/search-and-solve/blob/main/assets/vertices-objects.png)

## Permutations

After the generation of all the vertices from the data file, all permutations of these vertices are created
 
## Cost of each permutation

Each permutation's cost is calculated using this functionality:

Consider the following short data file:

![data-file](https://github.com/haris-sohail/search-and-solve/blob/main/assets/data-file.png)

which represents the following example:

![vertices-objects](https://github.com/haris-sohail/search-and-solve/blob/main/assets/vertices-objects.png)

Consider the ordering (5, 3, 1, 4, 2). With respect to vertex 1, the parent set {4} is not consistent with
the ordering. The parent sets {}, {3}, and {5} are consistent with the ordering
The ordering (5, 3, 1, 4, 2) has a total cost of 96.093 + 121.576 + 41.775 + 36.188 + 169.802 =
465.435. whereas the ordering (1, 2, 3, 4, 5) has a total cost of 153.466 + 141.022 + 107.516 + 51.680 + 36.508 = 490.192

## Graph generation

A graph is made for all permutation objects

## Search algorithms

Now BFS, DFS, and UCS are applied to find the minimum cost permutation

