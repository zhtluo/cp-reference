# cp-reference: Competitive Programming Reference

This competitive programming reference is based on my ICPC reference which my team used during my college years of 2016--2020 in Shanghai Jiao Tong University. We had the honor to win a Silver Medal in [ICPC World Final 2018](https://cphof.org/standings/icpc/2018).

## Download

Every release of the PDF file will be available under the [release](https://github.com/zhtluo/cp-reference/releases).

## Build

`make` should be sufficient to build the PDF.

## Design Rationales

ICPC has a maximum reference length of 25 pages for most regional championships (NAC, etc.) and the World Final. Therefore, the main goal of this reference is to cram as much knowledge as possible into 25 pages + 1 cover.

To achieve this goal, every code in this reference has been compressed to remove as much space as possible without sacrificing too much readability. You will see that the most common 'compression' is to move the closing brace to the end of the line rather than starting a new one. 

## Customization

You should customize the reference to your needs!

`main.tex` under the root stores the main LaTeX file, while all the code and other LaTeX files are stored under `src/`. All C++ code is formatted according to the style in `.vscode/settings.json`.

When `make` is executed, the compress script will create a compressed version of the code `.cpp.com` for every `.cpp` file found under `src/`. The LaTeX files can then reference these compressed files.

## FAQ

### Why is the code style so bad?

Every code in this reference has been compressed. See Design Rationales for the reasoning.

### How does this reference compare with KATCL?

You should definitely try both! In my opinion, [KATCL](https://github.com/kth-competitive-programming/kactl) is a more casual reference geared towards beginners. It has the following benefits.

- better description for algorithms in the document
- more robust testing script
- more beginner-oriented algorithms (e.g. Bellman-Ford, etc.)

In contrast, this reference is geared towards more advanced teams seeking to participate in regional championships (NAC, etc.) and the World Final. It focuses on these aspects.

- more content (roughly 20% more lines of code!)
- slightly better code highlighting
- more advanced algorithms (e.g. general weighted matching)

## Todo List

The following is a todo list. Feel free to submit pull requests for these items or other improvements you can think of!

### Content

- Add a link-cut tree implementation based on the Splay tree
- Condense & rewrite Delaunay triangulation explanation
- Verify Minkowski addition under 2D geometry
- Rewrite & condense K-shortest path solution
- Improve 2-SAT explanation
- Rewrite Hackenbush solution
- Write-up Lyndon word
- Add a pattern table for common patterns like Catalan, etc.

### Other

- Add a hash for every reference like KACTL