Reverse bits of a given 32 bits unsigned integer.

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0  # Initialize output to store the reversed bits
        for i in range(0, 32):  # Iterate 32 times (32-bit integer)
            output = output << 1  # Left shift output by 1 bit to make room for the next bit

            if n & 1:  # Check if the least significant bit of 'n' is 1
                output += 1  # If it is, set the least significant bit of 'output' to 1

            print(f"Iteration {i + 1}: Output = {output:032b}")  # Print the output in binary format
            n = n >> 1  # Right shift 'n' by 1 to get the next bit ready for checking in the next iteration

        return output  # Return the reversed bits stored in 'output'
