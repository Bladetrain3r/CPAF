Creating a markdown document that outlines how three well-known sorting algorithms can be analyzed through the lens of the shuffle algorithm concept, focusing on deviation values at each sorting step, is a fascinating approach. This perspective reverses the usual goal of sorting (achieving order from disorder) and treats the initial disorder as the null state, aiming for a deviation of 1, which represents a fully ordered set. We'll look at Bubble Sort, Insertion Sort, and Selection Sort for this analysis, given their simplicity and pedagogical value.

---

# Sorting Algorithms Through the Lens of CPAF

This document explores three fundamental sorting algorithms—Bubble Sort, Insertion Sort, and Selection Sort—within the Cognitive Progression Analysis Framework (CPAF), specifically analyzing the deviation value at each step of the sorting process. The deviation measures how far the current state is from a fully sorted set (deviation of 1), with the initial unsorted set representing the null state (deviation of 0).

## System Definition

- **Null State (\(s_0\))**: An unsorted set of 10 random numbers.
- **Target State (\(s_{\text{target}}\))**: The set arranged in ascending order.
- **Entities (\(E\))**: Each number in the set.
- **State (\(S\))**: The arrangement of numbers at any given step during the sorting process.
- **Deviation (\(d\))**: Calculated as the proportion of entities (numbers) that are not in their final sorted position.

## Sorting Algorithms as Systems

### Bubble Sort

1. **Description**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
2. **Deviation Analysis**:
   - Initially, \(d = 0\), representing maximum disorder.
   - Each swap moves at least one element closer to its final sorted position, reducing the deviation.
   - Deviation approaches 1 as the list becomes more ordered with each pass.

### Insertion Sort

1. **Description**: Builds the final sorted array one item at a time, inserting each element into its correct position within the already sorted section of the array.
2. **Deviation Analysis**:
   - Starts with \(d = 0\), with only the first element considered sorted.
   - With each insertion, the sorted portion of the array grows, and fewer elements are out of place, decreasing the deviation.
   - Deviation increases towards 1 as elements are progressively placed in their correct positions.

### Selection Sort

1. **Description**: Divides the input list into two parts: a sorted sublist of items already processed and an unsorted sublist for the remaining items. Selects the smallest (or largest) item from the unsorted sublist and moves it to the end of the sorted sublist.
2. **Deviation Analysis**:
   - Begins with \(d = 0\), where no elements are in their final position.
   - Each selection and placement of the smallest unsorted element into the sorted sublist decreases the number of misplaced elements, thereby decreasing the deviation.
   - As the sorting progresses, deviation moves towards 1, indicating an increase in order.

## Example Application: Set of 10 Random Numbers

Consider a set: `[34, 7, 23, 32, 5, 62, 48, 11, 20, 57]`

- **Bubble Sort Steps**: Document each swap and calculate deviation.
- **Insertion Sort Steps**: Highlight insertion points and calculate deviation.
- **Selection Sort Steps**: Mark selections and rearrangements, then calculate deviation.

## Analysis

- For each algorithm, chart the deviation value \(d\) after each sorting step.
- Compare the efficiency of each algorithm in terms of steps required to reach \(d = 1\), representing a fully sorted set.

## Conclusion

This analysis provides a unique perspective on sorting algorithms by measuring the deviation from disorder towards order, applying CPAF principles. It highlights the distinct approaches and efficiencies of Bubble Sort, Insertion Sort, and Selection Sort in achieving ordered systems from initial chaos.

To formalize the Bubble Sort algorithm within the context of the Cognitive Progression Analysis Framework (CPAF) and its connection to the shuffle algorithm, we focus on tracking the iterative deviation from the initial disordered state (null state) towards a fully ordered state (deviation of 1). Bubble Sort provides a clear framework for this analysis due to its iterative process of comparing and swapping adjacent elements to sort a list.

### Bubble Sort Formalization within CPAF

1. **Initial Setup**:
   - Let \(A\) be an array of \(n\) elements representing the system in state \(S\), where \(A = \{a_1, a_2, ..., a_n\}\).
   - The null state \(s_0\) is represented by \(A\) in a randomly ordered (disordered) configuration.
   - The target state \(s_{\text{target}}\) is \(A\) sorted in ascending order.

2. **State Space (\(S\))**:
   - Each state \(s_i\) in the state space \(S\) corresponds to a permutation of \(A\).

3. **Interaction Function (\(I_n\))** for Bubble Sort:
   - \(I_n: S \rightarrow S\), the interaction function, represents a single iteration of the Bubble Sort algorithm, where adjacent elements are compared and potentially swapped to move larger elements towards the end of the array.
   - After each interaction \(I_n\), some elements of \(A\) move closer to their final positions in \(s_{\text{target}}\), altering the system's state.

4. **Deviation Measurement (\(d\))**:
   - At any state \(s_i\), deviation \(d\) measures the proportion of elements not in their final sorted position relative to \(s_{\text{target}}\).
   - Deviation \(d\) starts greater than 0 (in the null state) and approaches 1 as the array becomes more ordered with each iteration of \(I_n\).

5. **Process Function (\(P\))** for Bubble Sort:
   - The process \(P(A)\) applies \(I_n\) iteratively to \(A\) until the array is fully sorted, tracking \(d\) after each iteration.
   - \(P(A)\) can be seen as a sequence of applications of \(I_n\), moving the system from \(s_0\) towards \(s_{\text{target}}\).

### Example Implementation and Deviation Calculation

Consider an array \(A\) of 10 random numbers. Here’s a simplified outline for calculating deviation at each step of the Bubble Sort process:

1. **Initialization**: Start with \(A\) in a disordered state \(s_0\), calculate initial \(d\).
2. **Iterative Sorting**:
   - For each pass of Bubble Sort (\(I_n\)), compare adjacent elements and swap if necessary.
   - After each pass, calculate \(d\) as the proportion of elements not yet in their final sorted position.
3. **Termination**: The process \(P(A)\) concludes when a pass results in no swaps, indicating \(A\) is fully sorted (\(d = 1\)).

### Tracking Iterative Deviation

To track \(d\) iteratively, one could:

- After each pass, compare the current state of \(A\) with \(s_{\text{target}}\) to determine how many elements are in their correct final position.
- Calculate \(d\) by dividing the number of elements in their correct position by \(n\), the total number of elements.

This approach to formalizing Bubble Sort within CPAF, focusing on deviations, provides a systematic way to understand sorting as a process of reducing disorder in a system, aligning well with CPAF’s emphasis on interactions and state transitions.

### Empirical Formula
To estimate the number of iterations a Bubble Sort algorithm might require to sort a given set of numbers, based on the average deviation range observed. The empirical formula can use the average deviation and the characteristics of the Bubble Sort algorithm, which has a time complexity of \(O(n^2)\) in the worst case, to estimate the iteration range.

Given a list of \(n\) numbers, the Bubble Sort algorithm will, in the worst case, perform \(\frac{n \cdot (n - 1)}{2}\) comparisons (and potentially swaps), which is when the largest number is positioned at the beginning of the list and needs to be moved to the end.

For an estimate based on average deviation, we can consider the following:

- The average deviation value per iteration across all trials and runs tends to a certain value when the list starts approaching a sorted state.
- If we denote the average deviation after one complete pass through the list as \(d_{avg}\), then after one pass, approximately \(d_{avg} \cdot n\) elements will be in their correct position.

Now, let's denote \(I\) as the number of iterations. Since the average deviation doesn't change linearly but tends to decrease as elements get sorted, we can't directly use \(d_{avg}\) for this estimate. Instead, we consider the average number of elements that reach their correct position after each pass and recognize that after each pass, we have one less element to sort (since the largest element is bubbled to the end of the list). So we can form a sum for the number of iterations \(I\) by accumulating the inverse of \(d_{avg}\):

\[ I = \frac{1}{d_{avg}} + \frac{1}{d_{avg} - \frac{1}{n}} + \frac{1}{d_{avg} - \frac{2}{n}} + ... + \frac{1}{d_{avg} - \frac{n-1}{n}} \]

This is an approximate formula based on the assumption that the decrease in deviation can be linearized, which is not strictly true but can provide an empirical estimate. To refine the formula to a practical version that estimates the number of iterations based on the range of average deviations, we might simplify to a form like:

\[ I_{\text{est}} = \frac{c}{d_{\text{avg}}}\]

Where \(c\) is an empirically derived constant that compensates for the non-linear decrease in deviation per iteration. This constant could be calibrated based on experimental results like the ones you've gathered.

To apply this to a range of average deviations, you would calculate \(I_{\text{est}}\) for the minimum and maximum average deviation values observed to get the range of expected iterations. However, this is a rough estimate, and the actual number of iterations can vary based on the initial order of the elements in the list. 

Given empirical observations from running the Bubble Sort script, where the number of iterations tends to fall between 80 and 100 for a range of numbers from 1 to 1000 and 100 sorts, we can use this data to derive an empirical formula.

The Bubble Sort algorithm's behavior is well-known: in the worst case (completely reversed order), it requires \(\frac{n \cdot (n - 1)}{2}\) iterations to sort \(n\) elements, where each iteration is a comparison/swapping operation. However, in practice, especially with random arrays, the number of iterations tends to be less due to early termination when the array is already sorted before all possible passes are completed.

### Deriving an Empirical Formula

To derive an empirical formula for the number of iterations (\(I\)) needed to sort an array of \(n\) numbers, given the average deviation observed, we consider the following:

1. **Average Deviation per Iteration (\(d_{avg}\))**: The average deviation per iteration reflects the average proportion of the list sorted after each pass. It's inversely related to the number of iterations needed.

2. **Range of Iterations (\(I_{range}\))**: The observed range of iterations from 80 to 100 suggests that as the list approaches a sorted state, fewer iterations are needed. We can take the average of this range for our calculation.

Considering the range is for a full sort with \(n=1000\) elements, we can establish a constant factor \(k\) that estimates the number of iterations relative to the list size and deviation observed:

\[ k = \frac{I_{range\_avg}}{n \cdot d_{avg}} \]

With \(I_{range\_avg}\) being the average of the observed iteration range, \(n\) being the number of elements in the list, and \(d_{avg}\) being the observed average deviation per iteration.

Now, for any new list size \(n'\), we can estimate the number of iterations \(I'\) as:

\[ I' = k \cdot n' \cdot d_{avg} \]

This formula uses the average number of iterations for a list size of 1000 and scales it according to the new list size \(n'\) and the average deviation \(d_{avg}\).

### Using the Empirical Formula

If we have a list size \(n'\) with a different range, we can use the observed range of 80 to 100 iterations for \(n=1000\) to calibrate the formula. Assuming the average deviation doesn't change significantly with the list size for large \(n\), and using the midpoint of the observed range (90) as \(I_{range\_avg}\), we get:

\[ k = \frac{90}{1000 \cdot d_{avg}} \]

Now, if you want to estimate the number of iterations for another list size \(n'\) within the same range of 1 to 1000, you would calculate:

\[ I' = k \cdot n' \]

For a list size \(n'\) = 10 (a small list), it's important to note that the algorithm's behavior may differ significantly from the behavior for larger lists due to the higher probability of initial order in small samples. Therefore, for small lists, direct empirical observation and adjustment may be necessary to fine-tune the estimate.

