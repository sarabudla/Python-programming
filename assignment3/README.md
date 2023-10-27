Program 1 

Secondary structure splitter.py

This program distinguishes between the secondary structure information and the protein sequences.

1. Import sys and argparse

2. To get the command-line options, use argparse, which returns an instance of the argparse arguments.

3. The created a command to get filehandle function. This is given the file name and the opening mode.
Then, to identify issues like OSError and ValueError, try and except are utilized.

4. Following that, the get fasta lists function is developed.
One list for sequences and another for headers are returned by the application.

5. Next, to ensure that the size of the header and sequence list are similar in size, a function called _verify lists is created.

6. After calling the function, close the file. 


Program 2

nt fasta stats.py

This program will generate a file with the accession number, A, T. G. C, N, length, and the percentage of GC for each sequence's length.

1. Import sys and argparse

2. To get the command-line options, use argparse, which returns an instance of the argparse arguments.

3. The creation of the get filehandle function. This is given the file name and the opening mode. Then, to identify issues like OSError and ValueError, try and except are utilized.

4. Following that, the get fasta lists function is developed. One list for sequences and another for headers are returned by the application.

5. Next, the _verify lists function is developed to verify that the size of the header and sequence list are same in number.

6. After that, output seq statistics is a function that is generated.
Here, functions for calculating the number of A, G, T, and Cs, as well as GC content and length, are provided.

7. To calculate the number of nucleotides and the NCBI accession number, a new function called _get num nucleotides and _get ncbi accession is developed.

8. An output file is produced as soon as the write mode is selected.

9. After calling the function, close the file. 


Program 3

test_secondary_structure_splitter.py, 

For the files' pytest, assert statements are provided.

1. Tests such as test check size of lists and test verify lists not eq len4 are performed to ensure the list's accuracy.

2. Tests to determine whether the file handle can handle IOError and ValueError

3. A test is then conducted to obtain the fasta file.

program 4

test_nt_fasta_stats.py, 

For the files' pytest, assert statements are provided.

1. The list is tested using tools like test verify lists.

2. Tests to determine whether the file handle can handle IOError and ValueError

3. A test is then conducted to obtain the fasta file. 