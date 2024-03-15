# **Definition:** A null state represents the baseline or equilibrium condition of a system, against which deviations, changes, or interactions are defined, measured, and understood.

## **Logical Construct:** ∀s ∈ S, ∃ns ∈ NullState | (¬∃d ∈ D) ∧ (¬∃int ∈ Int) when s = ns

**Natural Language Explanation:** For every system (s) within the set of all systems (S), there exists a null state (ns) such that no deviation (d) or interaction (int) occurs when the system is in its null state.

## Proofs
### **Proof 1: Universality Across Systems**

**Formalization**

We can express this proof using concepts already defined in the framework:

* **Premise 1:** ∀s ∈ S, ∃d ∈ D  (For all systems, there exist deviations)  
* **Premise 2:**  ∀d ∈ D, ∃ns ∈ NullState | ¬d  (For all deviations, there exists a null state where the deviation does not occur)
* **Conclusion:**  ∀s ∈ S, ∃ns ∈ NullState (Therefore, for all systems, there exists a null state)

**Notes:**
* This formalization highlights the chain of dependencies between systems, deviations, and the null state.

### **Proof 2: Necessity for Observing Deviations**

**Formalization (Option 1):**

* **Premise:** ∀d ∈ D, ∃ns ∈ NullState, ∃s ∈ S  | (d occurs in s) ∧ (d is a deviation from ns)
    * (For all deviations, there exists a null state from which it deviates and a system where it occurs)  
* **Conclusion:**  ¬∃ns ∈ NullState  ⇒ ¬∃d ∈ D 
    * (I.e., if a null state doesn't exist, then deviations cannot exist.)

### **Proof by Contradiction**

* **Assume:** ¬∃ns ∈ NullState (There exists no null state.)
* **Contradiction:** This implies ¬∃d ∈ D (no deviations can exist), which contradicts our understanding of systems where deviations are necessary for describing dynamics and change.
* **Conclusion:** The assumption is false; therefore, ∃ns ∈ NullState (a null state must exist).

## **Test Cases:**

* **Physics:** A motionless object in a frictionless environment.
* **Chemistry:** A chemical reaction at equilibrium.
* **Biology:**  A cell in a state of  homeostasis.
* **Ecosystem:** A stable ecosystem with no major fluctuations in population or resources.

## **Relationships:**

* **System:** A null state is intrinsically tied to the concept of a system. It serves as the reference point for defining changes within the system.
* **Deviation:**  The concept of a deviation is meaningless without a null state as a baseline.
* **Information:** Information often represents deviations from a null state or leads to deviations from it.
* **Entity:** In some systems, entities might actively maintain a null state or work to move the system away from it. 

**Recursion:**  The null state concept can be applied recursively. Systems can have subsystems, each with its own relative null state.  

## **Entropy Connection** 
At its most fundamental level, a null state is a representation of maximum entropy.  Systems tend towards a null state, a state from which no meaningful information can be derived. 

### Axiom of a null state: 
Change is the most fundamental descriptor.