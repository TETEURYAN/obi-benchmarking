$0 \cdot 2^{-1} + 1 \cdot 2^{-2} + 1 \cdot 2^{-3} = 0.25 + 0.125 = 0.375$.
Output matches test case 1: `0 1 1`.

Example 2:
$X = 1 0 1 1 1$
$Y = 0 0 0 1$
Let's align them for addition.
$X = 1 0 1 1 1$
$Y = 0 0 0 1$
We need to align the binary points (which are implicitly at the start).
$X$: $1 \cdot 2^{-1} + 0 \cdot 2^{-2} + 1 \cdot 2^{-3} + 1 \cdot 2^{-4} + 1 \cdot 2^{-5}$
$Y$: $0 \cdot 2^{-1} + 0 \cdot 2^{-2} + 0 \cdot 2^{-3} + 1 \cdot 2^{-4}$
Wait, $Y$ has length 4, so indices are $2^{-1}$ to $2^{-4}$.
Let's write them vertically:
  1 0 1 1 1
+ 0 0 0 1
-----------
We need to pad the shorter one with zeros to the right? No, standard binary addition aligns the binary point.
The powers of 2 must match.
$X$ has bits at positions $i=1..5$.
$Y$ has bits at positions $j=1..4$.
So we pad $Y$ with a 0 at position 5.
  1 0 1 1 1
+ 0 0 0 1 0
-----------
Let's add from right to left (least significant bit).
Pos 5: $1 + 0 = 1$. Carry 0.
Pos 4: $1 + 1 = 0$. Carry 1.
Pos 3: $1 + 0 + 1(\text{carry}) = 0$. Carry 1.
Pos 2: $0 + 0 + 1(\text{carry}) = 1$. Carry 0.
Pos 1: $1 + 0 = 1$. Carry 0.
Result: 1 1 0 0 1.
Matches test case 2 output.

Example 3:
$X = 0 1 1 1$
$Y = 0 0 1 1 1$
Align:
  0 1 1 1 0 (pad X with 0 at pos 5)
+ 0 0 1 1 1
-----------
Pos 5: $0 + 1 = 1$.
Pos 4: $1 + 1 = 0$, carry 1.
Pos 3: $1 + 1 + 1 = 1$, carry 1.
Pos 2: $1 + 0 + 1 = 0$, carry 1.
Pos 1: $0 + 0 + 1 = 1$, carry 0.
Result: 1 0 1 0 1.
Matches test case 3 output.

Algorithm:
1. Read $M$ and $N$.
2. Read the bits for $X$ and $Y$.
3. Since $M, N \le 1000$, we can store them in vectors or arrays.
4. The bits are given from most significant ($2^{-1}$) to least significant.
   Let's store them in vectors `vx` and `vy`.
   To make addition easier, it's often better to align them by size.
   Let $K = \max(M, N)$.
   Pad the shorter vector with zeros at the end (least significant positions) until size is $K$.
   Actually, since the input guarantees the last digit is 1, the lengths $M$ and $N$ define the precision.
   However, when adding, carries can propagate to the left.
   Since $X + Y < 1$, the integer part is 0. So no carry out of the $2^{-1}$ position.
   But carries can happen internally.
   
   Let's reverse the vectors to make index 0 the least significant bit (LSB).
   This makes addition logic standard (index $i$ corresponds to $2^{-(K-i)}$ roughly, or just standard array addition).
   
   Let's say we have `vx` (size $M$) and `vy` (size $N$).
   Reverse `vx` and `vy`.
   Now `vx[0]` is the coefficient of $2^{-M}$, `vx[M-1]` is coefficient of $2^{-1}$.
   `vy[0]` is coefficient of $2^{-N}$, `vy[N-1]` is coefficient of $2^{-1}$.
   
   We need to add these.
   Let's resize both to a common length. The result can have length up to $\max(M, N) + 1$.
   Wait, can the result be longer?
   Example: $0.1_2 + 0.1_2 = 1.0_2$. But constraint $X+Y < 1$ prevents this.
   Example: $0.01_2 + 0.01_2 = 0.10_2$. Length decreases? No, $0.10$ is not valid format (trailing zero). It becomes $0.1$. Length 2 -> Length 1.
   Example: $0.11_2 + 0.01_2 = 1.00_2$ (forbidden).
   Example: $0.01_2 + 0.11_2 = 1.00_2$ (forbidden).
   
   What if result has trailing zeros?
   The problem states: "a representação utiliza sempre o menor número de dígitos possível (ou seja, desta forma o dígito mais à direita é sempre 1)."
   So we must remove trailing zeros from the result.
   
   Let's implement the addition.
   Let $K = \max(M, N)$.
   Resize `vx` and `vy` to size $K+1$ (just in case, though carry won't go past $2^{-1}$, it might be useful for intermediate steps or if I reverse).
   Actually, let's just pad the shorter one with zeros up to $K$.
   Then perform addition from LSB (index $K-1$ if not reversed, or 0 if reversed).
   
   Let's stick to the "reverse" strategy.
   `vx` reversed: LSB is at index 0.
   `vy` reversed: LSB is at index 0.
   Pad the shorter one with zeros at the end of the vector (which are more significant bits) or beginning?
   If reversed:
   Original: $b_1 b_2 \dots b_M$ ($b_1$ is MSB, $b_M$ is LSB).
   Reversed: $b_M \dots b_2 b_1$ ($b_M$ is at index 0).
   If $N > M$, $Y$ has more bits. $Y$ has bits down to $2^{-N}$. $X$ only down to $2^{-M}$.
   So $X$ has implicit zeros for $2^{-(M+1)} \dots 2^{-N}$.
   In the reversed array, these correspond to indices $0 \dots N-M-1$.
   So we pad `vx` with zeros at the beginning (indices $0 \dots$).
   Actually, simpler:
   Create a result vector `res` of size $K+1$ initialized to 0.
   Iterate $i$ from 0 to $K-1$.
   Sum bits at position $i$ (where $i=0$ is $2^{-1}$).
   Wait, let's not reverse.
   
   Let's use indices $0 \dots M-1$ for $X$ and $0 \dots N-1$ for $Y$.
   $X[i]$ corresponds to $2^{-(i+1)}$.
   $Y[j]$ corresponds to $2^{-(j+1)}$.
   We want to add them.
   The LSB is at index $M-1$ for $X$ and $N-1$ for $Y$.
   Let's align them by the LSB? No, align by binary point (index 0).
   This is naturally handled by the indices.
   $X[i]$ and $Y[i]$ contribute to the same power of 2.
   If lengths are different, say $M < N$, then for $i \ge M$, $X[i]$ is 0.
   
   So, let `len = max(M, N)`.
   Create a vector `sum` of size `len + 1`.
   Initialize `carry = 0`.
   Iterate $i$ from `len - 1` down to 0.
   Current sum $S = carry$.
   If $i < M$, $S += X[i]$.
   If $i < N$, $S += Y[i]$.
   `sum[i+1] = S % 2`.
   `carry = S / 2`.
   After loop, `sum[0] = carry`.
   
   Since $X+Y < 1$, `sum[0]` (which represents $2^0$) must be 0.
   So the result bits are in `sum[1...len]`.
   However, we might have trailing zeros.
   The problem requires the last digit to be 1.
   So we iterate from the end of `sum` and remove zeros.
   Wait, the sum logic above puts the result in `sum`.
   Let's trace Example 2 again with this logic.
   $X = [1, 0, 1, 1, 1]$ ($M=5$)
   $Y = [0, 0, 0, 1]$ ($N=4$)
   `len` = 5.
   $i=4$: $S = 0 + X[4](1) + (i<4 \text{ false, so } 0) = 1$. `sum[5]=1`, `carry=0`.
   $i=3$: $S = 0 + X[3](1) + Y[3](1) = 2$. `sum[4]=0`, `carry=1`.
   $i=2$: $S = 1 + X[2](1) + Y[2](0) = 2$. `sum[3]=0`, `carry=1`.
   $i=1$: $S = 1 + X[1](0) + Y[1](0) = 1$. `sum[2]=1`, `carry=0`.
   $i=0$: $S = 0 + X[0](1) + Y[0](0) = 1$. `sum[1]=1`, `carry=0`.
   `sum[0] = 0`.
   Result vector `sum` (indices 1 to 5): `1 1 0 0 1`.
   Trailing zeros? Last is 1. No removal needed.
   Output: `1 1 0 0 1`. Correct.
   
   Trace Example 3:
   $X = [0, 1, 1, 1]$ ($M=4$)
   $Y = [0, 0, 1, 1, 1]$ ($N=5$)
   `len` = 5.
   $i=4$: $S = 0 + (i<4 \text{ false}) + Y[4](1) = 1$. `sum[5]=1`, `carry=0`.
   $i=3$: $S = 0 + X[3](1) + Y[3](1) = 2$. `sum[4]=0`, `carry=1`.
   $i=2$: $S = 1 + X[2](1) + Y[2](1) = 3$. `sum[3]=1`, `carry=1`.
   $i=1$: $S = 1 + X[1](1) + Y[1](0) = 2$. `sum[2]=0`, `carry=1`.
   $i=0$: $S = 1 + X[0](0) + Y[0](0) = 1$. `sum[1]=1`, `carry=0`.
   `sum[0]=0`.
   Result `sum` (indices 1 to 5): `1 0 1 0 1`.
   Last is 1. Correct.
   
   Case where trailing zeros appear:
   $X = [0, 1]$ (0.25), $Y = [0, 1]$ (0.25).
   Sum = 0.5 = $[1]$.
   $M=2, N=2$. `len`=2.
   $i=1$: $S = 0 + 1 + 1 = 2$. `sum[2]=0`, `carry=1`.
   $i=0$: $S = 1 + 0 + 0 = 1$. `sum[1]=1`, `carry=0`.
   `sum[0]=0`.
   Result `sum` (indices 1 to 2): `1 0`.
   We have a trailing zero at the end.
   We must remove it.
   So the output should be `1`.
   
   Implementation details:
   - Use `std::vector<int>` for storage.
   - Read inputs.
   - Perform addition.
   - Remove trailing zeros from the result.
   - Print the result separated by spaces.
   
   Corner case: Result is 0?
   Constraints say $X, Y > 0$, so $X+Y > 0$. The result will have at least one '1'.
   
   Max length of result:
   Max length of inputs is 1000.
   Result length can be at most 1000 (if no carry shortens it) or even 1001?
   Wait, if $X \approx 0.5$ and $Y \approx 0.5$, sum $\approx 1$.
   $X = 0.0111...1$, $Y = 0.0111...1$.
   Sum could be $0.111...10$.
   Carry propagates.
   Can the result be longer than inputs?
   $X = 0.1$ ($M=1$), $Y = 0.01$ ($N=2$). Sum = $0.11$ ($L=2$).
   $X = 0.01$ ($M=2$), $Y = 0.01$ ($N=2$). Sum = $0.10$ ($L=1$ after trim).
   $X = 0.11$ ($M=2$), $Y = 0.001$ ($N=3$). Sum = $0.111$ ($L=3$).
   Generally, the length of the sum is at most $\max(M, N) + 1$.
   Example: $X=0.01$ ($M=2$), $Y=0.001$ ($N=3$).
   $i=2: 1+1=0, c=1$.
   $i=1: 0+0+1=1, c=0$.
   $i=0: 0+0=0$.
   Result $0.010 \rightarrow 0.01$. Length 2.
   
   Is it possible to have length $\max(M, N) + 1$?
   $X = 0.1$ ($M=1$), $Y = 0.1$ ($N=1$). Sum $1.0$ (forbidden).
   $X = 0.01$ ($M=2$), $Y = 0.11$ ($N=2$). Sum $1.00$ (forbidden).
   $X = 0.011$ ($M=3$), $Y = 0.001$ ($N=3$).
   $i=2: 1+1=0, c=1$.
   $i=1: 1+0+1=0, c=1$.
   $i=0: 0+0+1=1, c=0$.
   Result $0.100 \rightarrow 0.1$. Length 1.
   
   It seems the length usually shrinks or stays same.
   Wait, consider $X = 0.1$ ($M=1$), $Y = 0.001$ ($N=3$).
   $i=2: 0+1=1$.
   $i=1: 0+0=0$.
   $i=0: 1+0=1$.
   Result $0.101$. Length 3.
   Here $N=3, M=1$. Result length 3.
   
   What about $X = 0.01$ ($M=2$), $Y = 0.0001$ ($N=4$).
   $i=3: 1$.
   $i=2: 0$.
   $i=1: 1$.
   $i=0: 0$.
   Result $0.0101$. Length 4.
   
   It seems the result length is bounded by $\max(M, N)$.
   Wait, can we extend length?
   $X = 0.011$ ($M=3$), $Y = 0.0001$ ($N=4$).
   $i=3: 1$.
   $i=2: 1$.
   $i=1: 1$.
   $i=0: 0$.
   Result $0.0111$. Length 4.
   
   Is it possible to have length $\max(M, N) + 1$?
   Suppose $X = 0.011$ ($M=3$), $Y = 0.0011$ ($N=4$).
   $i=3: 1$.
   $i=2: 1+1=0, c=1$.
   $i=1: 1+0+1=0, c=1$.
   $i=0: 0+0+1=1, c=0$.
   Result $0.1001$. Length 4.
   
   It seems the result length is at most $\max(M, N)$.
   Wait, let's check the logic.
   The sum is $S = X+Y$.
   $X < 2^{-1}$? No, $X < 1$.
   The LSB of $X$ is at $2^{-M}$.
   The LSB of $Y$ is at $2^{-N}$.
   The LSB of sum is at $2^{-\max(M, N)}$?
   Not necessarily. $2^{-M} + 2^{-N}$ could be $2^{-(\max(M,N)-1)}$ if they are equal and carry.
   But if they carry, the bit at that position becomes 0, and we carry to more significant bit.
   So the LSB of the sum is determined by the first position where the sum is odd.
   The maximum index needed is $\max(M, N)$.
   However, if we have a carry chain all the way to the front?
   $X = 0.0111$, $Y = 0.0001$.
   $i=3: 1+1=0, c=1$.
   $i=2: 1+0+1=0, c=1$.
   $i=1: 1+0+1=0, c=1$.
   $i=0: 0+0+1=1, c=0$.
   Result $0.1000 \rightarrow 0.1$. Length 1.
   
   So the result vector size should be $\max(M, N) + 1$ to handle the potential carry at the most significant bit position?
   Actually, the loop goes from `len-1` down to 0.
   The result is stored in `sum[1...len]`.
   `sum[0]` is the carry out of $2^{-1}$.
   Since $X+Y < 1$, `sum[0]` is always 0.
   So the result is contained within indices $1 \dots \max(M, N)$.
   Wait, what if the result has a bit at $2^{-(\max(M,N)+1)}$?
   Impossible. The smallest term in the sum is either $2^{-M}$ or $2^{-N}$.
   The sum of two such terms is at least $2^{-(\max(M,N))}$ (if one is zero) or $2^{-(\max(M,N)+1)}$?
   $2^{-k} + 0 = 2^{-k}$.
   $2^{-k} + 2^{-k} = 2^{-(k-1)}$.
   So the precision cannot increase beyond the max precision of the inputs.
   The LSB of the result will be at index $k \le \max(M, N)$.
   So allocating `max(M, N) + 1` for the sum vector is sufficient.
   Actually, `sum` vector size `max(M, N) + 1` is enough.
   Indices $0 \dots K$. $K = \max(M, N)$.
   $sum[0]$ is carry out (always 0).
   $sum[1 \dots K]$ are the bits.
   We iterate backwards to remove trailing zeros.
   
   Wait, is it possible that the result is just "0"?
   No, $X, Y > 0 \implies X+Y > 0$.
   
   Code structure:
   ```cpp
   #include <iostream>
   #include <vector>
   #include <algorithm>

   using namespace std;

   int main() {
       ios_base::sync_with_stdio(false);
       cin.tie(NULL);

       int M, N;
       if (!(cin >> M >> N)) return 0;

       vector<int> X(M);
       for (int i = 0; i < M; ++i) cin >> X[i];
       
       vector<int> Y(N);
       for (int i = 0; i < N; ++i) cin >> Y[i];

       int len = max(M, N);
       vector<int> sum(len + 1, 0); 
       // sum[0] is potential carry (2^0), sum[1] is 2^-1, ..., sum[len] is 2^-len
       // Wait, my previous indexing was:
       // sum[i+1] stores result for 2^{-(i+1)}.
       // So sum[1] to sum[len].
       // This matches.
       
       int carry = 0;
       for (int i = len - 1; i >= 0; --i) {
           int current_val = carry;
           if (i < M) current_val += X[i];
           if (i < N) current_val += Y[i];
           
           sum[i+1] = current_val % 2;
           carry = current_val / 2;
       }
       sum[0] = carry; // Should be 0
       
       // Find the actual end of the number (removing trailing zeros)
       // The bits are in sum[1...len].
       // We need to find the last index 'last_idx' such that sum[last_idx] == 1.
       int last_idx = -1;
       for (int i = len; i >= 1; --i) {
           if (sum[i] == 1) {
               last_idx = i;
               break;
           }
       }
       
       // Output
       // If last_idx == -1, it means sum is 0, which is impossible per constraints.
       // But handle just in case.
       if (last_idx == -1) {
           cout << "0" << endl; // Should not happen
       } else {
           for (int i = 1; i <= last_idx; ++i) {
               cout << sum[i] << (i == last_idx ? "" : " ");
           }
           cout << endl;
       }
       
       return 0;
   }
   ```
   
   Let's double check the indexing.
   $i$ goes from `len-1` down to 0.
   $i$ corresponds to the index in $X$ and $Y$.
   $X[i]$ is coefficient of $2^{-(i+1)}$.
   $Y[i]$ is coefficient of $2^{-(i+1)}$.
   We store result in `sum[i+1]`.
   So `sum[k]` is coefficient of $2^{-k}$.
   This is consistent.
   The loop for removing zeros starts at `len` down to 1.
   Correct.
   
   One detail: The problem says "A segunda linha contém M números Xi".
   The input format uses spaces.
   `cin >>` handles whitespace separation automatically.
   
   Constraints: $M, N \le 1000$.
   Time complexity: $O(\max(M, N))$.
   Space complexity: $O(\max(M, N))$.
   This is well within limits ($10^3$ is tiny).
   
   Let's re-verify the "remove trailing zeros" logic.
   Test case 1: `0 1` + `0 0 1`.
   $M=2, N=3$. `len`=3.
   $X=[0, 1]$. $Y=[0, 0, 1]$.
   $i=2$: $carry=0$. $i < M$ false. $Y[2]=1$. $val=1$. `sum[3]=1`, `carry=0`.
   $i=1$: $carry=0$. $X[1]=1$. $Y[1]=0$. $val=1$. `sum[2]=1`, `carry=0`.
   $i=0$: $carry=0$. $X[0]=0$. $Y[0]=0$. $val=0$. `sum[1]=0`, `carry=0`.
   `sum` = `[0, 0, 1, 1]`.
   Indices 1 to 3: `0 1 1`.
   Last 1 is at index 3.
   Output: `0 1 1`. Correct.
   
   Test case 2: `1 0 1 1 1` + `0 0 0 1`.
   $M=5, N=4$. `len`=5.
   $X=[1, 0, 1, 1, 1]$. $Y=[0, 0, 0, 1]$.
   $i=4$: $X[4]=1, Y$ out. $val=1$. `sum[5]=1`.
   $i=3$: $X[3]=1, Y[3]=1$. $val=2$. `sum[4]=0, c=1`.
   $i=2$: $X[2]=1, Y[2]=0, c=1$. $val=2$. `sum[3]=0, c=1`.
   $i=1$: $X[1]=0, Y[1]=0, c=1$. $val=1$. `sum[2]=1, c=0`.
   $i=0$: $X[0]=1, Y[0]=0, c=0$. $val=1$. `sum[1]=1`.
   `sum` = `[0, 1, 1, 0, 0, 1]`.
   Indices 1 to 5: `1 1 0 0 1`.
   Last 1 at 5.
   Output: `1 1 0 0 1`. Correct.
   
   Test case 3: `0 1 1 1` + `0 0 1 1 1`.
   $M=4, N=5$. `len`=5.
   $X=[0, 1, 1, 1]$. $Y=[0, 0, 1, 1, 1]$.
   $i=4$: $X$ out, $Y[4]=1$. `sum[5]=1`.
   $i=3$: $X[3]=1, Y[3]=1$. `sum[4]=0, c=1`.
   $i=2$: $X[2]=1, Y[2]=1, c=1$. $val=3$. `sum[3]=1, c=1`.
   $i=1$: $X[1]=1, Y[1]=0, c=1$. $val=2$. `sum[2]=0, c=1`.
   $i=0$: $X[0]=0, Y[0]=0, c=1$. $val=1$. `sum[1]=1`.
   `sum` = `[0, 1, 0, 1, 0, 1]`.
   Indices 1 to 5: `1 0 1 0 1`.
   Output: `1 0 1 0 1`. Correct.
   
   One edge case: $X=0.5 (1), Y=0.25 (01)$.
   $M=1, N=2$. `len`=2.
   $X=[1]$. $Y=[0, 1]$.
   $i=1$: $X$ out, $Y[1]=1$. `sum[2]=1`.
   $i=0$: $X[0]=1, Y[0]=0$. `sum[1]=1`.
   `sum` = `[0, 1, 1]`.
   Output: `1 1`. Correct ($0.75$).
   
   Another edge case: $X=0.5 (1), Y=0.5 (1)$.
   $M=1, N=1$. `len`=1.
   $i=0$: $X[0]=1, Y[0]=1$. $val=2$. `sum[1]=0, c=1`.
   `sum[0]=1`.
   `sum` = `[1, 0]`.
   Indices 1 to 1: `0`.
   Last 1 search:
   Loop $i$ from 1 down to 1.
   `sum[1]` is 0.
   Loop finishes. `last_idx` remains -1.
   Output logic: prints "0".
   But $X+Y = 1.0$. The problem says $X+Y < 1$.
   So this case is excluded by constraints.
   
   What if $X=0.25 (01), Y=0.25 (01)$?
   $M=2, N=2$.
   $i=1$: $1+1=2$. `sum[2]=0, c=1`.
   $i=0$: $0+0+1=1$. `sum[1]=1`.
   `sum` = `[0, 1, 0]`.
   Indices 1 to 2: `1 0`.
   Last 1 is at index 1.
   Output: `1`. Correct ($0.5$).
   
   The logic holds.
   
   Final check on input reading.
   "A segunda linha contém M números Xi"
   "A terceira linha contém