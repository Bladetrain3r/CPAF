**Definition:**

A deviation is a **distinguishable** change from a system's baseline state, prompted by internal or external information processing.

**Logical Construct:**

∀d ∈ D, ∃s ∈ S, i ∈ I | s processes i → d is distinguishable

**Natural Language Explanation:**

For all deviations (d), there exists a system (s) and information (i) such that when the system processes the information, the deviation becomes distinguishable. The deviation itself might not be actively observed, but it has the potential to be distinguished through its effects or the possibility of measurement. 

**Proof by Contradiction:**

Assume there exists a deviation that is not observed when any system processes any information. This contradicts the definition of deviation as an observable change from a system's baseline state, prompted by internal or external information processing.

**Test Cases:**

* **Circadian Rhythms:** Daily fluctuations in hormone levels represent deviations from a system's baseline physiological state. These deviations are distinguishable through observable changes in sleep patterns, body temperature, and hormone level measurements.

* **Autonomous Robots:** A robot encountering an unexpected obstacle deviates from its planned path. This deviation is distinguishable through sensor data indicating a discrepancy between the planned route and the actual environment.

* **Spontaneous Thoughts:** The emergence of a new thought during a conversation deviates from the previously established thought flow. While not directly observable by an external party, the deviation is distinguishable through the shift in the conversation's direction or the person's verbal and nonverbal cues.

* **Market Corrections:** A sudden drop in stock prices deviates from a market's expected trajectory. This deviation is distinguishable through market data analysis and its impact on investor behavior.

* **Transient System Failure:** A brief malfunction within an application stack causes a temporary slowdown in processing. This deviation might not be immediately noticeable by users, but it's distinguishable through performance logs or application monitoring tools.

* **Undetected Cancer:** The presence of cancerous cells in an organism deviates from a healthy cellular state.  Initially, this deviation might be  undetectable due to the limited sensitivity of diagnostic tools or the cancer's early stage. However, with more sophisticated diagnostic techniques or as the cancer progresses, the deviation becomes distinguishable through biopsies or imaging tests. 

**Relationships:**

* **System:** A deviation occurs within the context of a system.
* **Null State:** Deviations are defined in contrast to a system's null state.
* **Information:** Information processing triggers deviations.
* **Entity:** Entities can cause or respond to deviations.

**Recursion:** Deviations can occur at different hierarchical levels within a complex system. One system's deviation might be an element of a larger-scale deviation.

**Additional Notes:**

The concept of "distinguishable" allows for the possibility of latent deviations that might not be actively observed but have the potential to be detected through appropriate means. This aligns with CPAF's focus on potential changes within a system.

Given the conceptual framework for deviations as outlined in the "deviation.md" document and the mathematical formulation of the null state, we indeed can extend and mirror this approach to formally define deviations within a system mathematically. The key is to establish a generalized function that quantifies deviations not just from the null state but as a general property of system state changes.

### Deviations in CPAF Context

Deviations represent changes or departures from a system's null state, which are critical for understanding cognitive processes, learning, and adaptation. These deviations can be due to internal dynamics or responses to external stimuli.

### Mathematical Formulation of Deviations

To mathematically formalize deviations within a system, we consider the function \( f(s) \) introduced previously, which measures the deviation of a state \( s \) from the null state \( s_0 \). To expand this into a more general framework for deviations, we can introduce the concept of a deviation function \( d(s, s') \) that measures the deviation between any two states of the system, not just between a given state and the null state.

1. **General Deviation Function**:
   Let \( d: S \times S \rightarrow [0,1] \) be a function where \( S \) is the set of all possible states of a system, and \( d(s, s') \) measures the deviation between two states \( s \) and \( s' \) in the system.

2. **Properties of Deviation Function**:
    - **Null State Deviation**: For the null state \( s_0 \), and any state \( s \), \( d(s_0, s) = f(s) \), ensuring consistency with the null state deviation function.
    - **Symmetry**: Ideally, \( d(s, s') = d(s', s) \), meaning the deviation measure is the same regardless of the order of the states.
    - **Non-negativity and Boundedness**: \( d(s, s') \geq 0 \) for all \( s, s' \in S \), and is bounded by 1, consistent with the range of \( f(s) \).

3. **Example Deviation Function**:
   An example formulation could extend the linear model used for \( f(s) \) to account for deviations between any two states based on their measurable properties:

\[ d(s, s') = \min\left(\frac{\|s - s'\|}{\max_{s, s' \in S} \|s - s'\|}, 1\right) \]

where \( \|s - s'\| \) measures some form of distance or difference between the states \( s \) and \( s' \), normalized by the maximum observed or theoretical distance between any two states in the system to ensure the deviation remains within the interval \([0,1]\).

This formulation captures the essence of deviations as changes between states within a system, providing a quantitative measure that can be applied universally across the system's states. It aligns with the CPAF's focus on understanding cognitive systems' dynamics, allowing for the modeling and analysis of cognitive processes and their evolution over time.