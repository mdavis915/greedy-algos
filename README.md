## Greedy Algorithms

## Team Members:
    - Maria Davis: UFID: 97849528
    - Pamela Vishka: UFID: 79128424

## Project Structure

```
greedy-algos/
│
├── src/
│   └── cache_sim.py # implements cache eviction policies
│
├── data/ # input files for questions 1 and 2
│   ├── file1.in
│   ├── file2.in
│   ├── file3.in
│   └── question2.in
│
├── tests/ 
│   └── example.in # example to verify program runs properly
│
├── example.out # expected output for test/example.in
└── README.md
```
    

## Requirements
- Python 3.x
    
## How to Run

All commands should be executed from the root project directory.

### Getting started

Clone the repository

`git clone https://github.com/mdavis915/greedy-algos.git`

`cd greedy-algos`

### Run the program

The program takes an input file as a command-line argument.

`python3 src/cache_sim.py <input_file>`


Example:

`python3 src/cache_sim.py tests/example.in`

Expected output:
FIFO: 5
LRU: 5
OPTFF: 5

### Assumptions

Input files follow this format:

k m
r1 r2 ... rm

Where:
- `k` is the cache capacity
- `m` is the # of requests
- `r1 ... rm` is the sequence of integer IDs

Each ID in the sequence can be any integer, however, there must be exactly m values. The program outputs the number of misses found in the 3 eviction policies FIFO, LRU, and OPTFF.

### Question 1

| Input File | k | m | FIFO | LRU | OPTFF |
|------------|---|---|------|------|------|
| file1.in | 5 | 80 | 36 | 41 | 24 |
| file2.in | 4 | 70 | 43 | 44 | 30 |
| file3.in | 3 | 60 | 44 | 40 | 27 |

Yes, OPTFF has the fewest misses for all three files. This is expected because OPTFF is optimal and evicts pages with the furthest next usage. FIFO and LRU had mixed performances since in the first two files, FIFO performed better, but in the last file, LRU performed better. This goes to show that neither algorithm is consistent with outperforming the other, however, OPTFF had significantly better performance in all three files than FIFO and LRU. 

### Question 2

For k=3, there exists a request sequence for which OPTFF incurs strictly fewer misses than LRU and FIFO:


3 5 1 3 1 1 4 4 5 3 5 1

FIFO  : 7
LRU   : 7
OPTFF : 5

This sequence demonstrates that OPTFF is better on certain inputs due to knowing when future requests will occur and deciding which page to evict based on furthest next usage. FIFO and LRU are different since FIFO observes insertion order and LRU observes recent usage. Neither have the knowledge of future requests, so their evictions lead to more misses.

### Question 3

Claim: OPTFF incurs no more misses than any other offline algorithm A on any request sequence.

	Proof using the Exchange Argument:
	
There is an offline algorithm A and a request sequence. 
Suppose A and OPTFF process the sequence and agree on all decisions until time t. At time t, a miss occurs. Both algorithms have the same cache contents, but they differ on their eviction choices. 
OPTFF evicts element j (the one whose next request is furthest in the future).
Algorithm A evicts element i

Suppose we create a new algorithm called A’, which is the same as A until time t. At time t, A’ behaves the same as OPTFF by evicting j instead of i.
A and A’ differ by one element since A contains j and A’ contains i

To check that A’ doesn’t incur more misses than A, let ti and tj be the times of the next requests for i and j, respectively. 
By definition of OPTFF, ti < tj.
 Before ti
Besides an element that isn’t i or j, A and A’ will behave the same. If a request for j occurs, A’ might miss where A hit, but since j is the furthest in the future, there must be a request for i before that happens.
At time ti
A’ has i in its cache and makes a hit. Because A doesn’t have i, it may miss so A' has no more misses than A up to this point, and after this point we can repeat the same argument at the next divergence.. Therefore, A’ has just avoided a miss and we have shown that the swap never increases total misses. 
If this swap is done at every divergence point, A can be transformed into OPTFF without ever increasing the number of misses. 
Thus, the misses by the OPTFF algorithm will always be either less than or equal to the misses by any algorithm A. 
