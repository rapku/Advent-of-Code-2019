# Advent of Code 2019
https://adventofcode.com/2019

All solutions in notebook

Specific tools/methods used:
* Day 1: math package for rounding down
* Day 2: Developing IntCode class, brute forcing solution using randint (solution for part 2 had 2 variables, both integers from 0-99)
* Day 3: Numpy arrays for recording coordinates, itertools to determine which points are between each intersection  
* Day 4: Mainly booleans and if/for statements, using Counter from collections to check adjacent repeating numbers
* Day 5: Retooling IntCode class
* Day 6: NetworkX shortest path algorithm
* Day 7: 
  * Retooled IntCode class again (self.mem for current intcode command when stopped, halt instructions, inputs)
  * Created Amplif_ensem class to calculate 5 amplifiers, including functions to calculate output for manual input of intcode/phase code, and search for codes maximizing output
* Day 8: NumPy matrices and the product function from itertools, Pyplot used to display image
