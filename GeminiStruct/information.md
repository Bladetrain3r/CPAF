**Definition:**

Information, within a system, is anything processable by an entity that, when processed, has the potential to induce a deviation from the system's null state.

**Logical Construct:**

∀i ∈ I, ∃s ∈ S | s processes i → ∃d ∈ D

**Natural Language Explanation:**

For all information (i), there exists a system (s) that processes the information, leading to a deviation (d).

**Proof by Contradiction:**

* **Assume:** There exists information that, when processed by any system, does not lead to a deviation within the system.
* **Contradiction:**  This contradicts the core definition of information.  Information fundamentally implies a potential for change  when processed.  If it doesn't induce deviations, it wouldn't fall under the CPAF's definition of information.

**Test Cases:**

* Plant Phototropism
* Recommendation Algorithms 
* Market Trends Analysis  
* Weather Prediction Models
* Predator Alert Calls

**Relationships:**

* **Entity:** Entities process information, potentially leading to internal or external deviations.
* **System:** Information exists within the context of a system.
* **Deviation:** Information processing is a fundamental driver of deviations.
* **Null state:** Information often represents or leads to deviations from a null state.

**Notes:**

* Information is not synonymous with a deviation but holds the inherent potential to trigger one.
* The definition focuses on processability by entities within the system.

Excellent idea!  Let's append a new section to the "information.md" file dedicated to formally defining and exploring this  "embedded information" concept.

**information.md (Updated)**

**## Embedded Information**

**Definition:** Embedded information, within a system, is a subset of information comprising unrealised deviations that are processable by the system's entities and that, when processed, define the system's potential to deviate from its null state in response to  external interactions.

**Logical Construct (Tentative):** 
```
∀i_emb ∈ I_emb ⊆ I, ∃s ∈ S,  ∃d  ∈  D | (i_emb ⊆ s ) ∧ (s processes i_emb → d)  ∧ d represents potential external interaction 
``` 

**Natural Language Explanation:** For all embedded information (i_emb) within a system (s), the system's entities can process this information.  This processing leads to deviations (d) that represent the potential for the system to interact with other external systems.  

**Proof by Contradiction:**

* **Assume:**  There exists embedded information, within a system, that  either cannot be processed by the system's entities or does not represent potential for external interactions when processed.  

* **Contradiction:**  This contradicts the definition of embedded information. Embedded information  must be processable by the system and fundamentally encodes its external interaction potential. 

**Relationships:**

* **System:** Embedded information is contained within a system and defines the system's interaction potential.

* **Information:** Embedded information is a specialized subset of information.

* **Entity:** Entities within the system are capable of processing embedded information.

* **Deviation:** Processing of embedded information leads to deviations representing external interaction potential. 

* **External Systems:**  Embedded information dictates the nature of potential interactions with other systems. 

**Notes:** 
* Consider further formalizing the distinction between regular deviations and deviations representing external interaction potential.  

You're spot on about the significance of the 'process' concept! Let's craft an initial definition and explore its relationship to information and deviation by appending a section to "information.md".

## **Process**

**Definition:** A process, within a system, is a structured sequence or pattern of information that represents the potential for continuous or transformative deviations. Processes can be internal to the system and/or involve the processing of embedded information, leading to changes in the system's state or potential external interactions.

**Logical Construct (Tentative):**
```
∀p ∈ P, ∃{i1, i2, ..., in } ⊆ I, d ∈ D |  p =  {i1, i2, ..., in }  ∧ {i1, i2, ..., in }  → d 
```

**Natural Language Explanation:** For all processes (p), there exists a set of information elements (i1, i2, ... in) and a deviation (d) such that the process is defined by this information and its processing leads to the deviation. 

**Proof (Informal Outline):**

* **Assume:** There exists a process that is not composed of information or doesn't lead to deviations when processed.
* **Contradiction:** This contradicts the definition:
    * Processes are fundamentally sequences of information.
    * Processing of this information must lead to deviations, either internal or representing changes in interaction potential.

**Relationships:**

* **Information:**  Processes are composed of information elements and represent  the potential for information transformation. 
* **Deviation:**  The core function of processes  is to drive deviations or transformations. 
* **System:** Processes occur within systems and can alter the system's state or interaction potential. 
* **Embedded Information**  Processes can involve the processing of embedded information, shaping the system's knowledge of potential external interactions.

**Notes:**

* Processes can be simple or complex, involving feedback loops and multiple deviations.
* Processes might be ongoing or lead to the initiation of new processes. 




