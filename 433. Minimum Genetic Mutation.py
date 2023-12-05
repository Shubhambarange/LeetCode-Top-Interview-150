A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

class Solution:
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        #Corner case 1: if end gene is not in bank, return -1
        if endGene not in bank:
            return -1

        #Corner Case 2: if start gene==endgene no mutations required
        nmutations = 0
        if startGene==endGene:
            return nmutations

        #Corner Case 3: compute the number of gene mutations required if the rest of the string keeps unchanged and return  -1if the bank has less number of genes than the total number of mutations required.
        for ci in range(8):
            sc = startGene[ci]
            ec = endGene[ci]
            if sc!=ec:
                nmutations+=1
        #print(f'nmutations required: {nmutations}')

        if len(bank)<nmutations:
            return -1
        
        #BFS solution like Snakes and Laddes except now each position has 3 choices and there are 8 positions. You would add to the queue only if it is present in the bank and not seen yet.
        geneChoices = ['A', 'G', 'T', 'C']
        minMuts = [0]*len(startGene)
        seen = {}
        seen[startGene] = 1
        #for each mutation there are four possible moves and steps to get to.
        q = collections.deque()
        q.append((startGene, 0))
        while q:
            gene, step = q.popleft()
            
            if gene==endGene:
                return step
            
            #for each there are 4 possible changes
            #add all the possible 4 changes at each position that are in the bank.
            for ci in range(8):
                sc = gene[ci]
                for gc in geneChoices:
                    if gc!=sc:
                        mutGene = gene[:ci]+gc+gene[ci+1:]
                        if mutGene in bank and mutGene==endGene:
                            return step+1
                        if mutGene not in seen and mutGene in bank:
                            #print(f'mutGene: {mutGene}')
                            q.append((mutGene, step+1))
                            seen[mutGene] = 1
        return -1


