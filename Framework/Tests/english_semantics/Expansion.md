### Formal Definition of Logical Constructs

1. **Entities (\(E\))**: In the context of the English language evolution, entities are defined as whole words. Each word \(e_i \in E\) represents a discrete unit of language with specific semantic value(s).

2. **Information (\(I\))**: Information is twofold:
   - **Letters (\(i_1\))**: The composition of letters in a word, contributing to its form but not directly to its meaning.
   - **Meanings (\(i_2\))**: The semantic content of a word, quantified by the number of canonical definitions \(n_d\) it possesses. Each definition adds to the word's semantic breadth.

3. **Interactions (\(Int\))**:
   - **Archaism (\(Int_{a}\))**: The process by which words become archaic, effectively removing one or more of their definitions from common usage.
   - **Slang Introduction (\(Int_{s}\))**: The addition of new words or new meanings to existing words, representing deviation towards complete language change (\(d=1\)).

4. **Deviation (\(d\))**: The measure of change in the language's semantic landscape over time, reflecting alterations in vocabulary and meanings.

### Formal Mathematical Formula

The semantic deviation \(d\) of the English language over a specified interval can be quantified as a function of changes in information (\(i_2\)) due to interactions (\(Int\)):

\[ d = \frac{\Delta i_2}{i_{2_{baseline}}} \]

Where:

- \(\Delta i_2\) represents the change in semantic information due to archaism and the introduction of slang.
- \(i_{2_{baseline}}\) is the total semantic information at the baseline year.

### Breakdown for Accessibility

1. **Establishing Baseline Information (\(i_{2_{baseline}}\))**:
   - Determine the total number of canonical definitions across all words in the English language at the baseline year. This serves as our reference point for measuring semantic change.

2. **Calculating Change in Information (\(\Delta i_2\))**:
   - For each word that becomes archaic, subtract the number of definitions lost from \(\Delta i_2\).
   - For each instance of slang introduction or meaning change, add the new definitions to \(\Delta i_2\).

3. **Quantifying Deviation (\(d\))**:
   - The ratio of \(\Delta i_2\) to \(i_{2_{baseline}}\) provides a measure of semantic deviation. A higher \(d\) value indicates greater change in the language's semantic structure over the interval.

### Example Application

Consider a simplified example where the English language has 10,000 definitions across all words at the baseline. Over 50 years, 500 definitions become archaic, and 200 new definitions are introduced through slang. The change in information is \(\Delta i_2 = 200 - 500 = -300\), and the baseline information is \(i_{2_{baseline}} = 10,000\). Thus, the deviation is:

\[ d = \frac{-300}{10,000} = -0.03 \]

This negative deviation indicates a net loss in semantic breadth over the period, highlighting the dynamic and evolving nature of language as a cognitive system.

This structured approach provides a clear and quantifiable method to analyze the semantic evolution of the English language, offering insights into linguistic changes from a cognitive perspective.