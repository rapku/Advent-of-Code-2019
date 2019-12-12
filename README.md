# Advent of Code 2019
https://adventofcode.com/2019

All solutions in notebook

Specific tools/methods used:
* Day 1: math package for rounding down
* Day 2: Developing IntCode class, brute forcing solution using randint (solution for part 2 had 2 variables, both integers from 0-99)
* Day 3: Numpy arrays for recording coordinates, itertools to determine which points are between each intersection  
* Day 4: Mainly booleans and if/for statements, using Counter from collections to check adjacent repeating numbers
* Day 5: Refactored IntCode class >> IntCode_v2
* Day 6: NetworkX shortest path algorithm
* Day 7: 
  * Refactored IntCode_v2 class (self.mem for current intcode command when stopped, halt instructions, inputs)
  * Created Amplif_ensem class to calculate 5 amplifiers, including functions to calculate output for manual input of intcode/phase code, and search for codes maximizing output
* Day 8: NumPy matrices and the product function from itertools, Pyplot used to display image
* Day 9: IntCode program refactored again, new functionality:
  * spec_mode_manage for parameters referring to writing onto intcode (Thanks to [the post by u/Nexuist on "parameter mode modes](https://www.reddit.com/r/adventofcode/comments/e8aw9j/2019_day_9_part_1_how_to_fix_203_error/)
  * Changed work_intcode to be a dictionary to allow for intcode indexing of any length (anything indexing the intcode now uses **self.work_intcode.get(value, 0)**)
  * Adding opcode 9 functionality and adding 'relbase' for relative base storage in self.mem
* Day 10:
  * Checked line of sight using euclidean distance and angle (NumPy linalg.norm() and arctan2() respectively)
  * Part 2 solved mainly through reuse of distance/angle functions and list/dictionary manipulation
* Day 11: New Class paintBot
  * paintBot keeps memory of current board state (using (0,0) as start point)
  * Dictionary holds numpy arrays on how to move bot based on where it's placed (keys are integers 0-3, from up position moving clockwise)
  * Modulo (%) used whenever the paintbot changes where it faces, to prevent impossible keys
  * PLT imshow used to display numpy array based on paintBot's memory of current painted state
* Day 12: 
  * Part 1: Numpy array and where statements for managing position and vector arrays. 
  * Part 2: Used the same method, but for the 1D array representing each coordinate (x,y,z), iterating until it goes back to original state. Number of steps for all 3 coordinates recorded, and least common multiplier was taken to get point of convergence.
