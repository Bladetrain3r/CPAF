### Definition

An interaction is an event within a system where information is generated or transmitted, leading to a deviation in one or more entities.

### Logical Construct

```plaintext
∀int ∈ Int, ∃i ∈ I, ∃d ∈ D, ∃e ∈ E | int causes i → d in e
```

### Natural Language Explanation

For all interactions (int) within a system, there exists information (i) and a deviation (d) associated with an entity (e). This means that whenever an interaction occurs, it facilitates the generation or transmission of information, which subsequently leads to a change or deviation in at least one entity within the system.

### Proof by Contradiction

- **Assumption:** Assume there exists an interaction within a system that, despite causing the generation or transmission of information, does not lead to any deviation in entities.
  
- **Contradiction:** This assumption contradicts the foundational definition of an interaction within CPAF, which inherently links interactions to the generation of deviations via information processing. Therefore, by definition, an interaction must induce a deviation.

### Test Cases

- **Predator-Prey Dynamics:** Demonstrates interactions within ecological systems, where the predator's attempt to catch prey and the prey's evasion tactics lead to deviations in each entity's state.
  
- **Social Communication:** Highlights how information exchange in social interactions can alter perceptions, knowledge, or behavior of individuals or groups.
  
- **Algorithmic Trading:** In financial systems, the interaction between trading algorithms can lead to significant market deviations based on information exchange and processing.

### Relationships

- **Entity:** Entities are the subjects or objects within a system that participate in and are affected by interactions.
  
- **System:** Interactions are events that occur within the boundaries of a defined system, affecting its state or the state of its entities.
  
- **Information:** The essence of interactions involves the generation, transmission, or processing of information.
  
- **Deviation:** The purpose and outcome of interactions often culminate in deviations, marking changes within the system or its entities.

### External Interaction

#### Definition

An external interaction is a specialized form of interaction occurring between entities of different systems, facilitating the exchange or transmission of information that results in deviations within one or both systems.

#### Logical Construct

```plaintext
∀int_ext ∈ Int_ext ⊆ Int, ∃i ∈ I, d1 ∈ D, d2 ∈ D, e1 ∈ E, e2 ∈ E, s1 ∈ S, s2 ∈ S | (int_ext causes i → d1 in e1 in s1) ∧ (int_ext causes i → d2 in e2 in s2)  ∧ (s1 ≠ s2)
```

#### Natural Language Explanation

For every external interaction (int_ext), there exists information (i) that leads to deviations (d1, d2) in entities (e1, e2) belonging to different systems (s1, s2). This means that external interactions are those where the information exchange crosses the boundaries of individual systems, influencing changes beyond a single system's confines.

### Proof by Contradiction for External Interactions

- **Assumption:** Suppose an external interaction between entities of different systems does not result in any deviation within the entities involved.
  
- **Contradiction:** This assumption directly contradicts the definition of external interaction, which is characterized by its capacity to induce deviations across systems through information exchange. Thus, by definition, an external interaction must lead to deviation(s).

### Notes

- External interactions can vary in complexity and directionality, such as one-way or bidirectional exchanges, illustrating the diversity of interactions within and across systems.

Building upon the formalizations of null state, deviation, and information, we can extend our mathematical framework to incorporate the concept of **interaction**. In the Cognitive Progression Analysis Framework (CPAF), interactions are fundamental processes through which entities within a system or between systems exchange information, leading to changes or deviations in their states. Interactions can be between cognitive entities and their environment or among entities within a system, influencing the system's evolution and adaptation.

### Conceptual Understanding of Interaction

Interactions are the mechanisms through which entities affect each other's states by exchanging information. This exchange can lead to learning, adaptation, and the development of complex behaviors in cognitive systems. Interactions are pivotal for understanding the dynamics of cognitive systems and their capacity to process information and evolve.

### Mathematical Formalization of Interaction

To formalize interactions mathematically within a system, we define interactions in terms of their effects on the states of the entities involved, considering the information exchanged during the interaction and the resulting state changes.

1. **Interaction Function**:
   Let \( I_n: S \times S \times D \rightarrow S \times S \) be a function, where \( S \) is the set of all possible states of entities within the system, \( D \) is the domain of all possible data or stimuli inputs that could be exchanged during an interaction, and \( I_n(s_1, s_2, d) \) represents the new states of the entities \( s_1 \) and \( s_2 \) after interacting with the exchange of information \( d \).

2. **Effect of Interaction on States**:
    - The function \( I_n \) captures how the exchange of information \( d \) during an interaction between two entities in states \( s_1 \) and \( s_2 \) leads to transitions to new states \( s_1' \) and \( s_2' \).
    - The changes in states, measured by \( d(s_1, s_1') \) and \( d(s_2, s_2') \), quantify the deviations caused by the interaction on each entity.

3. **Quantifying Interaction's Effect**:
    - The impact of an interaction on an entity can be quantified by the deviation it causes in the entity's state as a result of the interaction. This can be further generalized to measure the collective impact on a system of entities.

4. **Example Interaction Function**:
    An example formulation to capture the impact of an interaction could be:

\[ I_n(s_1, s_2, d) = (s_1', s_2') \]

where \( s_1' = I(d, s_1) \) and \( s_2' = I(d, s_2) \), and \( I(d, s) \) is the information function defined earlier that maps the influence of information \( d \) on state \( s \) to a new state.

### Integration into CPAF

This formalization of interaction integrates into the CPAF by providing a structured way to analyze how entities within cognitive systems exchange information and influence each other's states. It highlights the importance of interactions in driving the evolution and adaptation of cognitive systems, shaping their behavior and capabilities over time.

By mathematically modeling interactions, we can better understand the mechanisms underlying cognitive processes, including communication, learning, and collective behavior. This approach enables the simulation and analysis of complex cognitive systems, offering insights into the dynamics of cognition and consciousness within the framework of CPAF.