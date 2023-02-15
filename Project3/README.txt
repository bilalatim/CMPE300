# Various Versions of Quick Sort Performance Testing

This ptyhon code is a program to test the performance of the Quick Sort algorithm with different input sizes, ranges, cases, and versions of the algorithm.
There are four version of algorithm:

1) **Classical Deterministic Quicksort Algorithm**: The pivot is chosen as the first element of the list. 
2) **Quicksort (1st version) Algorithm**: The pivot is chosen randomly.
3) **Quicksort (2st version) Algorithm**: The list is first randomly generated and then the classical deterministic algorithm is called where the pivot is chosen as the first element of the list.
4) **The Deterministic Quicksort Algorithm**: The pivot is chosen according to the **“median of three”** rule.

## Dependencies

This code requires the following python libraries:

* argparse
* random
* sys
* time

## Usage

To run the code, first go directory of file and use the following command:

- python main.py

To test spesific size, case or version you can use following optional arguments:

**-v**  type: String    (the version of the Quick Sort algorithm to use, options: {classical, randomized_pivot, randomized_permutation, median, all}, default : all)

**-n**  type: Integer   (the size of the input data, default: -1 (works for 100, 1000, and 10000 in default case))

**-r**  type: Float     (the range rate of the input data, each number is in between 1 - r*n, default: -1 (works for 10, 0.75, 0.25, 1/n in default case))

**-c**  type: String    (the case of the input data, options: {average, worst, both}, default: both)

**-p**  type: Boolean   (True: if the inputs are wanted to be printed, False: otherwise, default: False)

## Output

The code will print the results of the Quick Sort performance tests to the console. The results will include the input size, range, case, and version of the Quick Sort algorithm, as well as the time it took to run the algorithm on the input data and also input array.

The output can be printed to a specified file by adding " > < directory\of\the\output\file >" to the end of the command

Example: python main.py -v classical -n 10 -r 10 -c average > C:\output.txt

Warning: The output file must be created before the run

For big input sizes, output file is suggested.

## Example Run Command

python main.py -v classical -n 10 -r 10 -c average

## Example Output
Data size 10:
        Input type InpType1 with range [1, 100]:
                Algorithm classical as version of Ver1:
                        Duration for Case1 (average case): 10340.0
