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