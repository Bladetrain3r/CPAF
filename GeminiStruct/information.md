#### Definition

Information, within a system, is anything processable by an entity that, when processed, has the potential to induce a deviation from the system's null state. 

#### Logical Construct

∀i ∈ I, ∃s ∈ S | s processes i → ∃d ∈ D

#### Natural Language Explanation

For all pieces of information (i), there exists a system (s) that processes the information, leading to a deviation (d) from its null state. This definition encapsulates the transformative potential of information within cognitive systems.

#### Proof by Contradiction

Assume there exists information that, when processed by any system, does not lead to a deviation within the system. This assumption contradicts the core definition of information, which fundamentally implies a potential for inducing change when processed. Thus, if it doesn't lead to deviations, it wouldn't fall under CPAF's definition of information.

#### Proof of Equivalency to Entity

**Formalization:**

- **Premise 1:** Information is processable by entities (∀i ∈ I, ∃e ∈ E | e processes i).
- **Premise 2:** Entities are defined by their ability to process information and induce deviations (∀e ∈ E, ∃i ∈ I | e processes i → ∃d ∈ D).
- **Conclusion:** Information and entities are equivalently crucial in inducing deviations within systems, demonstrating their mutual necessity in CPAF.

**Proof by Example:**

Consider the role of a sensor (entity) in a climate control system. The sensor processes temperature information (i), leading to adjustments in the system's state (deviation). Similarly, the temperature data (information) requires the sensor (entity) to be processed and effect change. This interdependence showcases the equivalence and necessity of both concepts within CPAF.

#### Test Cases

- Plant Phototropism
- Recommendation Algorithms
- Market Trends Analysis
- Weather Prediction Models
- Predator Alert Calls

These examples illustrate the broad applicability of the information concept across biological, digital, and ecological systems, demonstrating its universality and relevance.

#### Relationships

- **Entity:** Entities process information, potentially leading to internal or external deviations.
- **System:** Information exists within the context of a system.
- **Deviation:** Information processing is a fundamental driver of deviations.
- **Null State:** Information often represents or leads to deviations from a null state.

### Mathematical Formalization of Information

To formalize information mathematically within a system, we consider information as a function that maps an input (data or stimuli) to its effect on the system, potentially causing a deviation from one state to another.

1. **Information Function**:
   Let \( I: D \times S \rightarrow S \) be a function, where \( D \) is the domain of all possible data or stimuli inputs, \( S \) is the set of all possible states of the system, and \( I(d, s) \) represents the new state of the system resulting from applying the input \( d \) to the current state \( s \).

2. **Impact of Information on State**:
    - The function \( I \) effectively captures how information (input \( d \)) influences the system's transition from one state to another.
    - The change in state, measured by \( d(s, I(d, s)) \), quantifies the deviation caused by the input \( d \), aligning with our previously defined deviation function \( d(s, s') \).

3. **Quantifying Information's Effect**:
    - To quantify the effect of information on the system, one could further define a metric that measures the "informational value" or "impact" of input \( d \) on state \( s \), perhaps in terms of the magnitude of deviation it causes or the novelty it introduces to the system.

4. **Example Information Metric**:
    An example metric to quantify the impact of information could be defined as the deviation it causes from the current state:

\[ \text{Impact}(d, s) = d(s, I(d, s)) \]

This metric measures how much the state changes as a result of processing the information \( d \), providing a quantitative assessment of information's effect on the system.

### Integration into CPAF

The mathematical formalization of information integrates seamlessly into the CPAF structure, complementing the concepts of the null state and deviations. Information acts as the mechanism through which external and internal stimuli influence cognitive systems, leading to deviations from the null state, transitions between states, and ultimately, cognitive evolution and adaptation.

This formalization not only provides a structured way to analyze the impact of information on cognitive systems but also opens pathways for modeling how information processing leads to learning, adaptation, and the emergence of complex cognitive phenomena within CPAF.

## Subsets

#### Embedded Information

**Definition:** Embedded information is a subset of information comprising unrealized deviations processable by the system's entities, defining the system's potential to deviate in response to external interactions.

**Logical Construct:**

∀i_emb ∈ I_emb ⊆ I, ∃s ∈ S, ∃d ∈ D | (i_emb ⊆ s) ∧ (s processes i_emb → d) ∧ d represents potential external interaction.

This construct and definition elaborate on the nuanced role of information that is 'pre-encoded' within the system, emphasizing its foundational role in defining the system's interaction potential with external environments.

#### Proof

**Logical Basis for Embedded Information as a Subset:**

Embedded information is inherently a subset of information characterized by its potential to pre-encode responses or adaptations within a system. This subset is distinguished by its specific role in preparing a system for future external interactions.

**Formalization:**

- **Premise 1:** All embedded information is information (∀i_emb ∈ I_emb, i_emb ⊆ I).
- **Premise 2:** Embedded information is uniquely defined by its role in encoding potential deviations in anticipation of external interactions (∀i_emb ∈ I_emb, ∃d ∈ D | s processes i_emb → d ∧ d represents potential external interaction).
- **Conclusion:** Embedded information, while a subset of information, carries the unique characteristic of being pre-processed by entities within the system to facilitate future interactions, thereby qualifying it as a logical subset.

#### Test Cases for Embedded Information

1. **Genetic Code in Biological Entities:**
   - **Description:** The genetic code of an organism contains embedded information that dictates responses to environmental stimuli. For example, certain genes become expressed only under specific conditions, such as stress or nutrient availability.
   - **Analysis:** This case demonstrates how embedded information within a biological system pre-encodes potential deviations (gene expression changes), preparing the organism for future external interactions (environmental changes).

2. **Machine Learning Models:**
   - **Description:** A machine learning model trained on historical data contains embedded information about patterns and correlations. When new data is processed, the model's output (a prediction or classification) is a deviation informed by this embedded information.
   - **Analysis:** Here, embedded information within the model dictates the system's (AI's) potential to deviate from a null prediction state in response to new data, showcasing the concept's applicability in artificial systems.

Embedding the concept of **embedded information** within the Cognitive Progression Analysis Framework (CPAF) allows us to address information that is inherent or stored within the system, influencing its state and behavior over time. Embedded information represents the accumulated knowledge or data within a system that can be accessed and utilized in processes, contributing to the system's cognitive functions and adaptations.

### Conceptual Understanding of Embedded Information

Embedded information refers to the data or knowledge that is stored within a system's structure or memory, which influences the system's operations and responses. This information can be the result of past interactions, learning experiences, or internal configurations that guide the system's behavior.

### Mathematical Formalization of Embedded Information

To formalize embedded information mathematically within the CPAF, we differentiate it from transient information (inputs or stimuli) by focusing on its role in the internal state and processes of the system.

1. **Embedded Information Representation**:
   Let \( E: S \rightarrow D' \) be a function, where \( S \) represents the set of possible states of the system, and \( D' \subseteq D \) represents the domain of embedded information within the system. The function \( E(s) \) identifies the embedded information available within state \( s \).

2. **Characteristics of Embedded Information**:
    - **State-Dependent**: Embedded information is dependent on the system's state, reflecting the knowledge or data accrued up to that point.
    - **Influences Processes**: Embedded information influences the processes within the system by providing a context or knowledge base that informs responses and decisions.

3. **Quantifying Embedded Information's Effect**:
    - The impact of embedded information on processes and state transitions can be considered in terms of how it modifies the outcomes of information processing functions. It may alter the efficiency, effectiveness, or direction of processes.

4. **Example of Embedded Information Function**:
    Considering a cognitive entity with a memory system, the embedded information function could represent how memories influence decision-making:

\[ E(s) = \text{memory content} \]

where \( s \) is the current state of the entity, and \( \text{memory content} \) represents the embedded information derived from past experiences. The influence of this embedded information on a decision-making process could then be modeled as:

\[ P(E(s), s) = s' \]

indicating how the entity's state \( s \), informed by its embedded information (memories), leads to a new state \( s' \) through a decision-making process \( P \).

### Integration into CPAF

Embedding the concept of embedded information within CPAF enriches the framework by accounting for the role of internal knowledge and memory in cognitive processes. This mathematical conceptualization allows for the modeling of how accumulated experiences and data influence a system's behavior and adaptations over time.

By formalizing embedded information, CPAF can more accurately reflect the complexity of cognitive systems, where internal states not only result from external inputs but also from the rich tapestry of stored information that guides processing and interactions. This approach enhances our understanding of cognition, emphasizing the importance of memory and knowledge in shaping cognitive dynamics and evolution.

#### Process

**Definition:** A process within a system is a structured sequence or pattern of information representing the potential for continuous or transformative deviations.

**Logical Construct:**

∀p ∈ P, ∃{i1, i2, ..., in} ⊆ I, d ∈ D | p = {i1, i2, ..., in} ∧ {i1, i2, ..., in} → d

#### Proof

**Logical Basis for Process as a Subset:**

Processes represent a structured sequence of information that, through its organization and temporal unfolding, leads to system deviations. This definition positions processes as subsets of information, specifically tailored by their sequence and potential for inducing deviations.

**Formalization:**

- **Premise 1:** All processes are composed of information (∀p ∈ P, ∃{i1, i2, ..., in} ⊆ I).
- **Premise 2:** The structured sequence of information in processes is distinctively configured to induce deviations (∀p ∈ P, {i1, i2, ..., in} → ∃d ∈ D).
- **Conclusion:** Processes, as sequences of information designed to induce deviations, are logical subsets of information, defined by their organizational structure and the purposeful direction towards achieving deviations.

#### Test Cases for Process

1. **Photosynthesis in Plants:**
   - **Description:** Photosynthesis can be seen as a process where light (information) is absorbed and transformed through a series of biochemical reactions (structured sequence) to produce glucose (deviation from energy null state).
   - **Analysis:** This biological process exemplifies how a sequence of informational inputs (light energy, water, CO2) is systematically processed to induce a vital deviation (glucose production).

2. **Automated Manufacturing Line:**
   - **Description:** An automated manufacturing line processes raw materials through a structured sequence of operations (cutting, shaping, assembling) to produce finished products. Each operation can be seen as processing information, leading to successive deviations.
   - **Analysis:** This example showcases a technological process where the structured sequence of operations (information processing) leads to the final product (a significant deviation from the raw material state).

This section bridges the concepts of information and deviation, outlining how processes—sequences of information—drive system changes.

To refine the Cognitive Progression Analysis Framework (CPAF) further, let's focus on formalizing the concept of a **process** as a subset of information, recognizing its crucial role in system dynamics and evolution. Within CPAF, processes can be understood as specific sequences or patterns of information processing that occur within a system, guiding its interactions, state transitions, and overall behavior.

### Conceptual Understanding of Process

A process represents a structured sequence of operations or transformations applied to information within a system, leading to specific outcomes or changes in the system's state. Processes are fundamental to how systems interpret and respond to information, embodying the mechanisms of learning, adaptation, and evolution.

### Mathematical Formalization of Process

To mathematically define a process within the framework of CPAF, we consider it as a function or a set of functions that specify how information (inputs) is transformed into effects (outputs) on the system's state or between states of entities within the system.

1. **Process Definition**:
   Let a process \( P \) be a function or a series of functions \( P: D \times S \rightarrow S \), where \( D \) represents the domain of information inputs, \( S \) represents the set of possible states of the system, and \( P(d, s) \) specifies the new state resulting from processing information \( d \) from state \( s \).

2. **Characteristics of Process**:
    - **Deterministic or Stochastic**: A process may be deterministic, with a given input and state always producing the same output, or stochastic, incorporating elements of randomness or uncertainty in how information influences state transitions.
    - **Composability**: Processes can be composed of smaller subprocesses, allowing complex operations to be built up from simpler ones. This hierarchical structure facilitates modeling of intricate cognitive functions.

3. **Impact of Process on State**:
    - The impact of a process on the system's state can be quantified similarly to how we previously defined the impact of information, using deviation measures to assess the change in state attributed to the process.

4. **Example Process Function**:
    An example of a process function could involve a cognitive entity processing sensory information to make a decision:

\[ P(\text{sensory data}, s) = s' \]

where \( s \) is the current state of the entity, "sensory data" is the input information, and \( s' \) is the new state after processing the sensory data, possibly resulting in a decision or action.

### Integration into CPAF

Formalizing processes as subsets of information within the system construct provides a clear mechanism for describing the functional operations that drive system behavior and evolution in CPAF. Processes encapsulate the ways in which information is utilized by the system, detailing the procedural aspects of cognition from perception to action.

This mathematical conceptualization of processes enhances our ability to model and analyze cognitive systems, facilitating a deeper understanding of the underlying mechanisms of cognition, learning, and adaptation. It solidifies the role of processes in transforming information into meaningful outcomes, thereby contributing to the progressive development of cognitive systems within the framework.

### Conceptual Understanding of Information

Information, in the context of CPAF, is crucial for the cognitive process. It represents data or stimuli that a system processes, which can lead to learning, adaptation, and evolution of the system. Information can originate from external sources (environment) or internal changes (within the system itself), influencing the system's behavior and state.

