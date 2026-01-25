# Kang et al. Paper 2: Macro-Level Structure Analysis

**Paper Title**: Agentic Feedback Loop Modeling Improves Recommendation and User Simulation
**Authors**: Shihao Cai, Jizhi Zhang, Keqin Bao, Chongming Gao, Qifan Wang, Fuli Feng, Xiangnan He
**Venue**: SIGIR 2025
**DOI**: 10.1145/3726302.3729893
**Field**: Recommender Systems / Information Retrieval
**Structure Type**: IMRaD (Introduction, Related Work, Method, Experiments, Conclusion)

---

## Overall Macro-Level Assessment

### Structural Framework
**IMRaD Adaptation**: Introduction → Related Work → Method → Experiments → Conclusion
- **Total Length**: ~10 pages (conference paper format)
- **Citation Style**: ACM numeric system
- **Disciplinary Conventions**: Strong emphasis on technical methodology, agent architecture, and empirical evaluation
- **Rhetorical Style**: Problem-solution structure with feedback loop as central innovation

### Hourglass Flow Analysis
**General → Specific → General** progression:
- **Introduction**: Broad applications of LLM-based agents → Specific gap (feedback loop) → Contribution (AFL framework)
- **Related Work**: Broad field overview (LLMs for recommendation, agent-based recommendation) → Specific gaps → Positioning
- **Method**: Technical specificity with modular agent architecture
- **Experiments**: Specific evaluation across three datasets → General implications
- **Conclusion**: Specific findings → Broad impact

---

## Section-by-Section Macro Analysis

### Section 1: Introduction (CARS Model Application)

#### Move 1: Establishing Territory (Paragraphs 1-2)
**Content**: Claims centrality of LLM-based agents in recommendation domain
**Strengths**:
- Uses evaluative language: "substantial efforts," "revolutionized," "extensive capabilities"
- Establishes broad significance: "wide range of tasks," "simulating human behavior"
- Present/present perfect tense: "are increasingly applied," "have revolutionized"

**Excerpt**: "In recent years, substantial efforts have been dedicated to developing agents based on large language models (LLMs), aiming at simulating human behavior to enhance the performance across a wide range of tasks."

**Analysis**: Strong centrality claims establishing LLM-based agents as important paradigm. Connects technical capabilities (memory, tools, reasoning) to practical applications.

#### Move 2: Establishing Niche (Paragraphs 4-5)
**Content**: Identifies specific gap in collaborative interaction between agents
**Strengths**:
- Clear gap identification: "primarily focuses on optimizing either the recommendation agent or the user agent separately"
- Specific technical challenge: "overlooking the critical role of the feedback loop"
- Opposing viewpoint: contrasts separate optimization with collaborative feedback loop

**Excerpt**: "Existing research primarily focuses on optimizing either the recommendation agent or the user agent separately, overlooking the critical role of the feedback loop between the user and the recommender."

**Analysis**: Gap is highly specific and researchable. The problem is framed as missing collaborative interaction rather than individual component improvement.

#### Move 3: Occupying Niche (Paragraphs 5-7)
**Content**: Presents AFL (Agentic Feedback Loop) as solution with specific contributions
**Strengths**:
- Clear objectives: "simultaneously enhances the ability of both agents"
- Specific outcomes: "average improvement of 11.52% over the single recommendation agent and 21.12% over the single user agent"
- Roadmap: outlines paper organization and contributions

**Excerpt**: "To this end, we introduce the **A**gentic **F**eedback **L**oop (AFL) modeling. AFL simultaneously constructs both a recommendation agent and a user agent, using textual communication to simulate the feedback loop."

**Analysis**: Strong positioning with acronym introduction (AFL) and clear contribution claims. Notice the emphasis on "simultaneously" improving both agents through collaboration.

**Key Linguistic Features**:
- **Nominalization**: "optimization," "collaboration," "simulation" - creates technical formality
- **Technical Terminology**: LLMs, agents, feedback loop, memory modules - assumes expert audience
- **Contribution Enumeration**: Numbered contributions for clarity

---

### Section 2: Related Work (Literature Review Structure)

#### Move 1: Thematic Overview (Paragraph 1)
**Content**: Broad overview of LLMs for recommendation field
**Strengths**:
- Establishes scope: "LLMs for recommendation" and "agent-based recommendation"
- Thematic grouping: feature enhancement vs. direct recommendation
- Temporal progression: "recent years," "have begun exploring"

**Excerpt**: "Due to LLMs' extensive knowledge and strong reasoning capabilities, researchers have begun exploring their application in recommendation systems."

**Analysis**: Clear positioning relative to existing work. Two main categories identified (feature enhancement, direct recommendation).

#### Move 2: Critical Analysis (Paragraphs 2-4)
**Content**: Detailed evaluation of related approaches
**Strengths**:
- Thematic organization: LLMs for recommendation, agent-based recommendation
- Critical evaluation: contrasts different approaches (RecMind, MACRec, Agent4Rec)
- Gap identification: "have not considered the feedback loop between them"

**Excerpt**: "The recommendation agent focuses on tackling recommendation tasks... The user agent focuses on simulating user behavior... However, the existing recommendation agent and user agent approaches have not considered the feedback loop between them, which is a crucial feature in recommendation systems, to simultaneously enhance the performance for both the recommendation and user simulation."

**Analysis**: Strong critical analysis with clear limitations identified. Systematic review of both recommendation agents and user agents reveals the gap.

#### Move 3: Research Gaps (Final paragraph)
**Content**: Synthesis and positioning
**Strengths**:
- Connects back to introduction gap
- Establishes methodological foundation
- Sets up technical contribution

**Analysis**: Literature review concludes by explicitly identifying the feedback loop as missing element, directly motivating the proposed AFL approach.

---

### Section 3: Method (Core Technical Contribution)

#### Macro-Level Organization
**Content**: Technical methodology presentation
**Strengths**:
- Clear problem statement: "formalize the feedback loop between recommendation and user agents"
- Modular architecture explanation: Recommendation Agent, User Agent, Feedback Loop
- Mathematical formalism: input-output formalization with interaction history

**Excerpt**: "As shown in Figure 2, AFL consists of: (1) a recommendation agent (Section §3.2), (2) a user agent (Section §3.3), and (3) the feedback loop between the two agents (Section §3.4)."

**Analysis**: Highly technical section with strong architectural foundation. Notice the clear separation of components with dedicated subsections.

#### Key Components:

**3.1 Overview**
- **Input-Output Specification**: Formal definition of interaction history [I₁, I₂, ..., Iₙ] and prediction task
- **Process Flow**: Detailed description of iterative feedback loop mechanism
- **Termination Condition**: Clear stopping criteria (user satisfaction)

**Excerpt**: "The input to AFL is the user-item interaction history, formalized as [I₁, I₂, ⋯, Iₙ], where Iᵢ represents the i-th item the user interacts with. The output is AFL's prediction of the next item, Iₙ₊₁, that the user is likely to interact with."

**3.2 Recommendation Agent**
- **Components**: Recommendation model, memory module, prompt template
- **Functionality**: Generates recommendations with rationale
- **Adaptability**: Flexible architecture supporting various base models

**3.3 User Agent**
- **Components**: Reward model, memory module, prompt template
- **Functionality**: Evaluates recommendations and provides feedback
- **Simulation Capability**: Models user preferences and behaviors

**3.4 Feedback Loop**
- **Iterative Process**: Multi-round interaction between agents
- **Memory Management**: Stores interaction history for both agents
- **Adaptation Mechanism**: Both agents improve based on feedback

**Excerpt**: "In each iteration, the recommendation agent suggests an item and provides a rationale. The user agent then responds with feedback, indicating whether it likes the item. If the user agent is satisfied, the loop terminates; otherwise, both the recommendation rationale and user feedback are stored in memory, and the process repeats."

---

### Section 4: Experiments (Evaluation)

#### Macro-Level Organization
**Content**: Comprehensive evaluation across three research questions
**Strengths**:
- Clear evaluation metrics: HitRatio@1 for recommendation, Precision/Recall/F1 for user simulation
- Systematic comparison: Base Model vs. Rec Agent vs. AFL
- Ablation studies: Component analysis and iteration impact
- Bias analysis: Popularity and position bias investigation

**Excerpt**: "To assess the effectiveness of the proposed framework, we conducted comprehensive experiments on three widely used recommendation datasets: LastFM, Steam, and MovieLens. The experimental results show that AFL simultaneously enhances the performance of both the recommendation agent and the user agent, with larger improvements as the maximum number of iterations increases."

**Analysis**: Strong empirical evaluation with appropriate statistical measures. Notice the dual-task evaluation (recommendation + user simulation) and comprehensive ablation studies.

#### Research Questions Addressed:

**RQ1: Effectiveness of AFL**
- **Recommendation Performance**: Systematic comparison across multiple base models (traditional: SASRec, GRU4Rec, Caser; LLM-based: MoRec, Llama3, GPT-4o-mini, LLaRA)
- **User Simulation Performance**: Evaluation across different imbalance ratios (1:1, 1:3, 1:9)
- **Case Study**: Illustrative examples of agent collaboration

**Excerpt**: "Based on the experimental results presented in Table 4, we have drawn the following findings and conclusions: (1) First, the recommendation agent equipped with the recommendation model outperforms or performs equally well compared to the original base model in most cases. (2) Moreover, the AFL, which is based on the feedback loop, demonstrates a significantly greater improvement than the use of a standalone recommendation agent."

**RQ2: Impact of Key Components**
- **User Agent Feedback**: Ablation study removing user feedback
- **Recommendation/Reward Model Impact**: Analysis of different model architectures
- **Feedback Loop Iterations**: Impact of iteration number on performance

**Excerpt**: "Furthermore, the results show that the agentic feedback loop does not exacerbate popularity or position bias, which are typically amplified by the real-world feedback loop, highlighting its robustness."

**RQ3: Biases in Feedback Loop**
- **Popularity Bias**: Analysis of bias amplification
- **Position Bias**: Examination of positional effects

**Analysis**: Comprehensive evaluation addressing both effectiveness and potential negative consequences (biases), demonstrating thorough experimental design.

---

### Section 5: Conclusion and Future Work

#### Macro-Level Organization
**Content**: Synthesis, limitations, and future directions
**Strengths**:
- Clear contribution summary
- Balanced limitations discussion
- Future directions identified
- Broader impact consideration

**Excerpt**: "Extensive experiments on three datasets demonstrate the effectiveness of the agentic feedback loop: the agentic feedback loop yields an average improvement of 11.52% over the single recommendation agent and 21.12% over the single user agent."

**Analysis**: Strong conclusion that quantifies contributions and addresses robustness (bias analysis). Connects technical contribution to practical implications.

---

## Cross-Disciplinary Comparison

### Computer Science vs. Traditional Academic Writing

| Aspect | Cai et al. Paper | Traditional Academic |
|---|---|---|
| **Literature Review Location** | Separate section after introduction | Integrated into introduction |
| **Technical Detail Level** | Very high (agent architecture, algorithms) | Medium (methods overview) |
| **Evaluation Focus** | Dual-task evaluation (recommendation + simulation) | Single-task validation |
| **Contribution Claims** | Quantitative performance + architectural framework | Theoretical advancement + empirical evidence |
| **Bias Analysis** | Explicit bias investigation | Implicit or omitted |

### Key Learning Points for Imitation

1. **Modular Architecture**: Clear separation of components (agents, memory, feedback loop)
2. **Dual-Task Evaluation**: Simultaneous evaluation of recommendation and user simulation
3. **Comprehensive Ablation**: Systematic component analysis
4. **Bias Investigation**: Explicit analysis of potential negative consequences
5. **Architectural Flexibility**: Framework adaptable to various base models

---

## Imitation Opportunities for Future Papers

### Structural Elements to Adapt
- **Agent Architecture**: Modular design with clear component interfaces
- **Feedback Loop Mechanism**: Iterative refinement through interaction
- **Memory Management**: Explicit handling of interaction history
- **Dual-Task Framework**: Simultaneous optimization of multiple objectives
- **Bias Analysis**: Systematic investigation of fairness and robustness

### Rhetorical Strategies
- **Collaboration Emphasis**: "Simultaneously" enhancing multiple components
- **Gap Identification**: Missing interaction rather than component deficiency
- **Real-World Connection**: Feedback loops as fundamental system feature
- **Quantitative Positioning**: Specific performance improvements in introduction
- **Robustness Claims**: Bias analysis demonstrating system reliability

### Quality Indicators
- **Architectural Rigor**: Clear formalization of agent components
- **Empirical Validation**: Multiple datasets, metrics, and baselines
- **Ablation Studies**: Systematic component analysis
- **Bias Investigation**: Explicit fairness analysis
- **Reproducibility**: Detailed implementation and publicly available code
- **Generalizability**: Validation across multiple base models and domains

---

## Notable Excerpts for Analysis

### Centrality Claims
"In recent years, substantial efforts have been dedicated to developing agents based on large language models (LLMs), aiming at simulating human behavior to enhance the performance across a wide range of tasks. These LLM-based agents typically integrate memory modules, utilize tools, and perform advanced reasoning."

### Gap Identification
"Existing research primarily focuses on optimizing either the recommendation agent or the user agent separately, overlooking the critical role of the feedback loop between the user and the recommender. However, in real-world recommendation scenarios, the recommender aids users in discovering their interests and preferences. Simultaneously, users, through multi-round interactions with the recommender, provide feedback that enables the system to better understand their preferences."

### Solution Presentation
"AFL simultaneously constructs both a recommendation agent and a user agent, using textual communication to simulate the feedback loop. In each iteration, the recommendation agent suggests an item and provides a rationale. The user agent then responds with feedback, indicating whether it likes the item."

### Methodological Precision
"The input to AFL is the user-item interaction history, formalized as [I₁, I₂, ⋯, Iₙ], where Iᵢ represents the i-th item the user interacts with. The output is AFL's prediction of the next item, Iₙ₊₁, that the user is likely to interact with. Specifically, the user-item interaction history initializes the user agent and serves as input to the recommendation agent."

### Quantitative Results
"Extensive experiments on three datasets demonstrate the effectiveness of the agentic feedback loop: the agentic feedback loop yields an average improvement of 11.52% over the single recommendation agent and 21.12% over the single user agent. Furthermore, the results show that the agentic feedback loop does not exacerbate popularity or position bias, which are typically amplified by the real-world feedback loop, highlighting its robustness."

### Robustness Claims
"Furthermore, unlike real-world feedback loops that often amplify popularity and position biases, the experimental results show that AFL does not exacerbate these biases, demonstrating its robustness."

### Contribution Summary
"In conclusion, our main contributions are summarized as follows:
- To our knowledge, our work is the first to highlight the significance of modeling the feedback loop between the recommendation agent and the user agent in LLM-based recommendation.
- We propose a novel framework, AFL, which establishes an agentic feedback loop to facilitate the cooperation and reciprocity between the recommendation agent and the user agent.
- Extensive experiments validate the effectiveness of the proposed AFL approach, underscoring the potential and importance of the feedback loop in agent-based recommendation systems."

---

## Comparison with Paper 1

### Structural Differences
1. **Organization**: Paper 1 uses RQ-driven structure; Paper 2 uses traditional IMRaD
2. **Literature Review**: Paper 1 places it after results; Paper 2 follows convention
3. **Methodology Placement**: Paper 1 has methodology before results; Paper 2 follows standard order

### Common Strengths
1. **Quantitative Positioning**: Both papers provide specific performance metrics in introduction
2. **Comprehensive Evaluation**: Multiple datasets, metrics, and baselines
3. **Practical Focus**: Consideration of real-world deployment factors
4. **Reproducibility**: Publicly available code and detailed protocols

### Different Approaches
1. **Problem Framing**: Paper 1 focuses on evaluation methodology; Paper 2 on system architecture
2. **Evaluation Scope**: Paper 1 evaluates evaluators; Paper 2 evaluates recommendation systems
3. **Contribution Type**: Paper 1 provides evaluation framework; Paper 2 provides system framework
