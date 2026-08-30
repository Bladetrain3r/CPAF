# Information

- **Status:** Draft 0.1
- **Dependencies:** analysis context, processability, state or trajectory
  variation, deviation criterion
- **Primary adjacent concepts:** interaction, deviation, entity, memory

## Intent

Define information as a context-relative, processable difference with
counterfactual effect, while separating that abstract property from measures
such as mutual information or transfer entropy.

## Typed abstract definition

Let `j` be a candidate difference, signal, record, or internal state feature.

```text
Processable_s(j; C)
Effect_s(j; C)

Info_s(j; C) ≔
    Processable_s(j; C)
    ∧ ∃ admissible context variation v:
        Effect_s(j; v, C) > ε_info
```

`Processable` means that an entity or system can receive, distinguish, retain,
transform, or use `j` under the declared context. `Effect` compares the
resulting trajectory, state distribution, decision, or available action with a
specified counterfactual in which the relevant difference is absent or altered.
The effect criterion and its threshold are part of the claim.

Information is therefore neither every physical difference nor only a difference
that produces an effect on every presentation.

## Natural-language bridge

Information is a difference that can matter to a specified system because the
system can process it and would behave differently under a relevant alternative.
The same signal can be information for one system and noise for another.

## Necessary and sufficient conditions

A canonical information claim requires:

1. a candidate difference `j`;
2. a processing entity or system;
3. an observation and representation sufficient to identify `j`;
4. an admissible counterfactual or comparison;
5. a declared effect variable and criterion;
6. a scale and time window.

These conditions are sufficient for the stipulated context-relative class. They
do not establish that `j` is intrinsically informative independent of a system,
observer, or task.

## Subtypes

- **Transient information:** available through an input or event during a
  bounded interval.
- **Embedded information:** stored in a state, structure, or policy and capable
  of changing a future response under an admissible trigger.
- **Relational information:** dependence between variables or entities.
- **Directed information:** evidence that one variable improves prediction of
  another under a declared direction and lag.
- **Action-relevant information:** information whose processing changes an
  available action, policy, or control trajectory.
- **Identity information:** information sufficient to distinguish a stored or
  recoverable pattern from alternatives.

“Embedded” and “relational” describe roles, not evidence levels. A stored
parameter is not automatically information until its processability and
counterfactual effect are shown.

## Information certificates

Claims about information on a particular edge require a certificate level:

```text
RELATED   — statistical dependence
DIRECTED  — predictive direction under a declared lag/model
CONNECTED — direct-edge claim relative to observed conditioning variables
```

The ladder is ordered by evidential burden, not by amount of information.
`CONNECTED` is conditional on the available variables and does not mean absolute
metaphysical causation.

## Relation to adjacent concepts

- A **deviation** can make a difference detectable, be caused by processing it,
  or be the counterfactual effect that certifies it.
- An **interaction** is a possible pathway for information; a channel may exist
  without a certified information effect.
- An **entity** supplies processing, storage, or action capacity.
- **Memory** is a candidate mechanism for retaining embedded information, not a
  synonym for information.

## Operationalization contract

A substrate-specific report must state:

1. the variables and representation used for `j`;
2. the processing entity and accessible inputs;
3. the counterfactual or comparison condition;
4. the effect measure, estimator, threshold, and uncertainty treatment;
5. the certificate level if an interaction edge is claimed;
6. conditioning variables and possible common causes;
7. scale, physical time, observer clock, sampling, and feature map;
8. falsification or negative-control checks.

Mutual information, transfer entropy, conditional transfer entropy, prediction
loss, and intervention effects are candidate operationalizations. None is the
abstract definition by itself.

## Known computational witness

K-SOM-Heb provides a bounded witness:

- iteration 7 measures mutual information appearing at the pair-locking
  transition and separates it from global coherence;
- iteration 8 demonstrates the related/directed/connected certificate ladder;
- iteration 11 shows transfer through a latent channel before a locking
  deviation;
- iterations 13–14 show identity information through recovery of stored
  patterns;
- iteration 16 shows that certificate verdicts and magnitudes can respond
  differently to observer re-expression.

These results establish realizability and useful distinctions in one substrate,
not universality.

## Non-claims and counterexamples

This definition does not claim:

- all data, signals, or correlations are information;
- information must produce an observed deviation;
- mutual information establishes direction or causation;
- information quantity is a universal scalar of cognitive value;
- embedded information is accessible or useful without a trigger;
- a changed measurement magnitude is a physical change in the system;
- information implies awareness, meaning, or agency.

## Open decisions

1. Choose a standard counterfactual protocol for domains where intervention is
   impossible.
2. Specify how information certificates degrade under partial observability.
3. Decide whether information should be typed separately as ontic, epistemic,
   and operational.
4. Define cross-substrate reporting conventions without forcing a universal
   normalization.

## Legacy crosswalk

- `Framework/information.md`: replaces the universal “processes and causes a
  deviation” reading with processability plus counterfactual effect.
- `Framework/interaction.md`: separates information candidates from their
  transmission channels.
- `Framework/ComputationalProofs.md` §3 and §7.3: evidence and certificate
  refinement history.

## Change log

- **Draft 0.1:** introduces a typed, context-relative information definition and
  certificate ladder.
