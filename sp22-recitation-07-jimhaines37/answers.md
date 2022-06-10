# CMPS 2200 Recitation 7
## Answers

**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |1340|826|0.61641791


alice29.txt    |         1039367            |      676374          | 0.65075570


asyoulik.txt    |           873253          |        606448        | 0.69209235


grammar.lsp    |         26047            |        17356        | 0.66633393


fields.c    |          78050           |        56206        | 0.72012812

Yes, Huffman coding always seems to cost less than fixed length encoding. It seems that Huffman coding takes about 65% of the cost that it takes fixed length coding to do the same task.


- **e.**

length of alphabet to the n where n is the common frequency of each element
I expect it to cost len(alphabet)^n, where n is the frequency that all of the letters each have. This is because to obtain the Huffman cost we determine the number of binary digits required to make up 1 character and multiply this by the frequency of that character.

