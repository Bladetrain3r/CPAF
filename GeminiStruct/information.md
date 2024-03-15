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