# Modeling Quake 3 Bot AI as a Cognitive System within CPAF

## **1. Introduction**

Quake 3 Arena, known for its fast-paced action and competitive gameplay, also features sophisticated bot AI that simulates human-like opponents. The bots demonstrate various cognitive capabilities through their interactions within the game, making them an intriguing subject for analysis within the Cognitive Progression Analysis Framework (CPAF). This document aims to qualitatively describe Quake 3 bot AI to identify metrics for quantitative analysis.

## **2. Qualitative Exploration of Quake 3 Bot AI**

### **Cognitive Capabilities and Behaviors**

- **Navigation and Spatial Awareness**: Quake 3 bots exhibit advanced navigation skills, moving through complex 3D environments while avoiding obstacles and seeking advantageous positions.
  
- **Tactical Decision-Making**: Bots make real-time decisions based on the game state, including weapon selection, engaging or retreating from combat, and item acquisition strategies.

- **Adaptation and Learning**: While the bots' learning capabilities are pre-programmed and do not evolve during gameplay, their behavior adjustment based on predefined difficulty levels simulates a form of adaptation.

- **Simulated Social Interaction**: Bots use text chat to simulate communication with players, contributing to the illusion of playing against human opponents.

### **Underlying Code and Mechanisms**

- **Rule-Based Logic**: The AI's decision-making process is driven by a complex set of rules that govern behavior under various conditions.

- **Pathfinding Algorithms**: Utilize the game's map geometry to navigate efficiently, seeking objectives and tracking opponents.

- **Simulated Perception**: Bots have a field of view and can "hear" sounds within the game, dictating their awareness of other players' positions and actions.

## **3. Towards Quantitative Modeling**

To model Quake 3 bot AI within CPAF quantitatively, we need to derive metrics from the qualitative capabilities identified. This involves analyzing the source code to understand the algorithms and data structures that underpin the bots' cognitive processes.

### **Potential Metrics for Analysis**

- **Decision-Making Efficiency**: Time and accuracy in tactical decision-making.
  
- **Spatial Navigation Proficiency**: Ability to navigate maps without error and efficiency in reaching objectives.
  
- **Adaptive Behavior**: Changes in tactical approaches based on the game state or player actions.
  
- **Simulated Social Interaction Frequency**: Use of text chat in response to game events.

### **Data Retrieval and Simulation**

- **Source Code Analysis**: Examine the AI programming for insights into rule-based logic and pathfinding algorithms.
  
- **Match Simulations**: Run simulated matches under various conditions to observe and record bot behaviors and decision-making processes.

## **4. Conclusion**

The qualitative exploration of Quake 3 bot AI lays the groundwork for a comprehensive analysis within the CPAF. By transitioning from qualitative descriptions to quantitative metrics, we aim to model the bot AI as a cognitive system, providing insights into how programmed algorithms simulate cognitive processes in a competitive gaming environment. Future work will focus on retrieving specific data from source code analysis and simulated matches to develop a detailed transition function that models the bots' cognitive evolution over time.

---

To define and quantify the proposed metrics within the context of Quake 3 as a system, leveraging the game's structure and bot AI behavior, let's outline a structure for each metric, including how they relate to the game's difficulty settings (null states) and the potential formulas or methods for initial quantification. This approach will allow us to measure and analyze bot behavior in a structured manner, providing insights into their cognitive modeling within CPAF.

### Decision Making: Weapon Selection

**Definition**: The process by which bots decide which weapon to use or pursue based on the game context (e.g., enemy distance, available ammunition, map layout).

**Null State**: Predetermined weapon preferences that correspond to different difficulty levels.

**Quantification Formula**:
- **Input Variables**: Enemy distance (`D`), current ammunition levels (`A`), map control points or items proximity (`P`), and current health level (`H`).
- **Decision Function**: `WeaponChoice = f(D, A, P, H)`, where `f` determines the optimal weapon based on a weighted analysis of input variables.
- **Measurement**: Compare chosen weapon to an optimal weapon selection model for given situations to rate decision-making efficiency.

### Pathfinding: Navigation Efficiency

**Definition**: The ability of bots to navigate through the game's maps using BSP trees and dynamically weighted nodes to reach objectives or engage opponents.

**Null State**: Basic pathfinding abilities adjusted per difficulty settings, affecting how dynamically bots can weight their pathfinding nodes.

**Quantification Method**:
- **Path Efficiency Score (PES)**: Calculate the actual path length taken by a bot to reach a target vs. the optimal path length, normalized by the optimal path length. A score closer to 1 indicates higher efficiency.

### Adaptability: Relative Performance

**Definition**: The bot's ability to adjust its strategies or behaviors based on the game state and performance against other bots or players.

**Null State**: Base performance metrics (e.g., kill-death ratio) set for each difficulty level without adaptation.

**Quantification**:
- **Adaptation Index (AI)**: Measure the change in performance metrics (e.g., kill-death ratio) relative to the starting state over the course of a match. A positive change indicates adaptability.

### Social Interaction: Shit-Talk Frequency

**Definition**: Frequency and type of scripted phrases ("shit-talk") used by bots during a match, potentially indicative of simulated social interaction or psychological tactics.

**Null State**: A base frequency of phrases used, modified by difficulty level.

**Quantification**:
- **Phrase Frequency (PF)**: Count of specific phrases used per minute.
- **Deviation in Phrase Use (DP)**: Change in the type and frequency of phrases during key game events (e.g., gaining a lead, losing an item) compared to the null state.

### Conclusion

By defining these metrics within the context of Quake 3 and outlining initial quantification methods, we can systematically analyze bot behavior and cognitive modeling. This framework not only allows for the assessment of decision-making, pathfinding, adaptability, and social interaction but also aligns with the CPAF's approach to evaluating cognitive systems. Future work will involve detailed source code analysis and match simulations to refine these quantification methods and validate the proposed models.