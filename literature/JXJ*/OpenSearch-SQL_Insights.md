# OpenSearch-SQL Paper Macro-Level Structure Analysis

**Paper Title**: OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment
**Authors**: Xie et al. (2025)
**Conference**: (Submitted)
**Field**: Natural Language Processing / Database Systems / Text-to-SQL
**Structure Type**: IMRaD (Introduction, Preliminary, Methodology, Experiments, Conclusion)

---

## Overall Macro-Level Assessment

### Structural Framework
**IMRaD Adaptation**: Introduction → Preliminary → Methodology → Experiments → Related Work → Conclusion
- **Total Length**: ~15 pages (conference paper format)
- **Citation Style**: Numeric citation system (ACM format)
- **Disciplinary Conventions**: Heavy emphasis on technical methodology, framework design, experimental evaluation, and benchmark comparisons
- **Rhetorical Style**: Problem-solution structure with strong technical justification and empirical validation

### Hourglass Flow Analysis
**General → Specific → General** progression is well-executed:
- **Introduction**: Broad Text-to-SQL applications → Specific limitations (L1, L2, L3) → Framework and contribution claims
- **Preliminary**: General LLM and Text-to-SQL background → Specific framework categorization
- **Methodology**: Technical specificity with algorithmic descriptions and framework details
- **Experiments**: Specific evaluation metrics → General implications
- **Conclusion**: Specific findings → Broad impact on Text-to-SQL field

---

## Section-by-Section Macro Analysis

### Section 1: Introduction (CARS Model Application)

#### Move 1: Establishing Territory (Paragraph 1)
**Content**: Claims centrality of Text-to-SQL systems and their importance
**Strengths**:
- Uses evaluative language: "crucial," "holy grail," "significantly raised"
- Establishes historical context and significance
- Present/present perfect tense: "is notoriously hard," "have been," "have increasingly accomplished"

**Excerpt**: "Text-to-SQL task attempts to automatically generate Structured Query Language (SQL) queries from Natural Language Queries (NLQ). This task can improve the ability to access databases without the need for knowledge of SQL."

**Analysis**: Strong centrality claims with clear problem statement. Notice the emphasis on accessibility ("without the need for knowledge of SQL") connecting technical capability to user empowerment.

**Excerpt**: "As the text-to-SQL problem is notoriously hard, these systems have been the holy grail of the database community for several decades."

**Analysis**: Excellent use of metaphor ("holy grail") to emphasize importance and difficulty. Notice the temporal perspective ("several decades") establishing historical significance.

**Excerpt**: "Recently, with the development of large language models, researchers have increasingly accomplished the task through methods such as the use of supervised fine-tuning (SFT), Chain-of-Thought(CoT), Agents, and In-Context Learning, achieving results that greatly surpass previous methods."

**Analysis**: Clear temporal progression ("Recently") with enumeration of methods. Notice the strong claim ("greatly surpass") supported by methodological advancement.

#### Move 2: Establishing Niche (Paragraphs 2-3: Limitations L1, L2, L3)
**Content**: Identifies specific limitations in current Text-to-SQL approaches
**Strengths**:
- Systematic gap identification: Three numbered limitations (L1, L2, L3)
- Specific technical challenges for each limitation
- Clear enumeration format

**Excerpt**: "Limitation. Although the methods driven by LLMs have significantly raised the upper limits of the Text-to-SQL task capabilities, our analysis of previous work reveals that: L1 Due to the ambiguity of the overarching framework, there are some gaps at the methodological level. This has prevented these methods from reaching their potential. For example, there is a lack of verification of the stored information in the database, no error correction for the generated results, and issues related to the absence of few-shot learning."

**Analysis**: Excellent systematic approach - uses "Limitation" as section header, then enumerates three specific gaps. Notice the hedging ("Although...significantly raised") followed by clear problem identification. Uses specific examples ("lack of verification," "no error correction," "absence of few-shot learning").

**Excerpt**: "L2 LLM-driven approaches often rely on multi-agent collaboration. However, due to the instability of LLMs and the lack of guaranteed coherence and coupling between agents, later-executing agents may not use or only partially use the outputs of previously running agents. This leads to accumulated hallucinations and performance loss."

**Analysis**: Strong technical analysis - identifies specific mechanism (multi-agent collaboration) and specific problem (instability, lack of coherence, accumulated hallucinations). Notice the cause-effect chain ("leads to").

**Excerpt**: "L3 The instructions and steps that guide the LLMs significantly affect the quality of the generated SQLs. In the pre-LLM era, methods employing intermediate languages to generate SQL were developed to address this issue, but current research on instruction construction remains insufficient."

**Analysis**: Excellent temporal contrast ("pre-LLM era" vs. "current research") to establish gap. Notice the reference to historical solutions ("intermediate languages") showing awareness of prior work.

#### Move 3: Occupying Niche (Paragraphs 4-6: Framework and Contributions)
**Content**: Presents OpenSearch-SQL as solution with specific contributions
**Strengths**:
- Clear connection to identified limitations (L1, L2, L3)
- Systematic solution presentation
- Explicit contribution enumeration
- Strong positioning claims

**Excerpt**: "Inspired by the aforementioned challenges, we conducted a detailed analysis of the human workflow in completing the Text-to-SQL task: understanding the database structure and selecting the specific tables, columns, and values needed to get the SQL."

**Analysis**: Strong positioning - uses "Inspired by the aforementioned challenges" to connect solution to identified problems. Notice the human-centered approach ("human workflow") as motivation.

**Excerpt**: "Framework. To address L1, our research defines a Standard Text-to-SQL framework based on the process humans use to complete SQL construction. This can cover current research on LLM-driven Text-to-SQL tasks. We believe that a complete Text-to-SQL task framework should include four steps: Preprocessing, Extraction, Generation, Refine:"

**Analysis**: Excellent systematic approach - explicitly connects to L1 ("To address L1"), provides rationale ("based on the process humans use"), then enumerates four steps. Notice the use of "We believe" for positioning statement.

**Excerpt**: "For L2, we analyzed common hallucinations in multi-agent collaboration-driven Text-to-SQL tasks and designed a consistency alignment-based alignment agent for these hallucinations. By ensuring consistency in the functions, inputs, and outputs of specific agents, our aim is to reduce hallucinations during the model generation process."

**Analysis**: Clear connection to L2 with specific solution ("consistency alignment-based alignment agent"). Notice the mechanism description ("ensuring consistency in functions, inputs, and outputs").

**Excerpt**: "For L3, we developed a self-taught few-shot augmentation mechanism that supplements query-SQL pairs with Chain-of-Thought(CoT) information, creating Query-CoT-SQL pairs. This enriched few-shot approach can enhance the performance of LLMs."

**Analysis**: Clear connection to L3 with specific technical solution ("self-taught few-shot augmentation mechanism"). Notice the technical terminology ("Query-CoT-SQL pairs").

**Excerpt**: "Contribution In summary, our contributions are as follows. • To the best of our knowledge, we are the first to propose a multi-agent cooperative framework based on consistency alignment for the Text-to-SQL task. This alignment mechanism significantly reduces the loss of information transmission between Agents and the hallucinations in the results generated by the Agents."

**Analysis**: Strong contribution claims with explicit enumeration. Uses "To the best of our knowledge" for academic hedging while making strong novelty claim ("first to propose"). Notice the quantitative claim ("significantly reduces").

**Excerpt**: "Our proposed method, OpenSearch-SQL, did not utilize fine-tuning or introduce any specialized datasets. At the time of submission, it achieved 69.3% EX on the BIRD benchmark validation set, 72.28% EX on the test set, and R-VES of 69.36%, all ranking first."

**Analysis**: Excellent positioning - emphasizes transferability ("did not utilize fine-tuning") and empirical results ("all ranking first"). Notice the specific metrics and temporal qualification ("At the time of submission").

#### Key Linguistic Features
- **Nominalization**: "alignment," "generation," "refinement" - creates technical formality
- **Passive Voice**: "are generated," "is selected" - emphasizes processes over agents
- **Technical Terminology**: LLM, Text-to-SQL, CoT, alignment, hallucination - assumes expert audience
- **Quantitative Precision**: "69.3% EX," "72.28% EX," "69.36%" - emphasizes empirical rigor
- **Enumeration**: L1, L2, L3; Preprocessing, Extraction, Generation, Refine - creates systematic organization

---

### Section 2: Preliminary

#### Macro-Level Organization
**Content**: Background on LLMs and Text-to-SQL, framework categorization
**Structure**: 2.1 Large Language Models → 2.2 Text-to-SQL → 2.3 Hallucination

**Strengths**:
- Clear background section
- Technical definitions
- Framework categorization

**Excerpt**: "Pre-trained large language models have acquired extensive language knowledge and semantic information through unsupervised learning on large-scale textual data. This pre-training typically employs autoregressive architectures (such as GPT-like models) or autoencoding structures (such as BERT-like models)."

**Analysis**: Strong technical background with clear definitions. Notice the use of examples ("GPT-like models," "BERT-like models") for clarity.

**Excerpt**: "The Text-to-SQL task can be defined as: a task that translates a NLQ Q into an SQL query Y based on database information S, a specific model F(·|θ), and a particular prompt P."

**Analysis**: Clear formal definition with mathematical notation (Q, Y, S, F(·|θ), P). Notice the systematic approach - defines components explicitly.

**Excerpt**: "Inspired by these methods, this paper first systematically organizes these modules. We categorize existing methods into four stages: Preprocessing, Extraction, Generation, and Refinement."

**Analysis**: Excellent positioning - "systematically organizes" and "categorize" shows contribution. Notice the enumeration ("four stages") creating clear structure.

---

### Section 3: Methodology

#### Macro-Level Organization
**Content**: Technical methodology presentation with detailed framework components
**Structure**: 3.1 Alignments → 3.2 Self-Taught Fewshot → 3.3 Preprocessing → 3.4 Extraction → 3.5 Generation → 3.6 Refinement → 3.7 Algorithm → 3.8 Optimization

**Strengths**:
- Comprehensive technical coverage
- Clear component descriptions
- Algorithmic specifications
- Mathematical formulations

#### Subsection 3.1: Alignments
**Content**: Consistency alignment mechanism for multi-agent collaboration
**Strengths**:
- Mathematical formulation (Equation 2)
- Clear problem motivation (hallucination reduction)
- Specific mechanism description

**Excerpt**: "LLM hallucination is a critical problem affecting the usability of LLMs, and it is also present in the Text-to-SQL task. Furthermore, the cumulative errors that arise from multi-agent collaboration exacerbate the hallucination problem in LLMs."

**Analysis**: Strong problem motivation with clear mechanism ("cumulative errors," "exacerbate"). Notice the emphasis on practical impact ("affecting the usability").

**Excerpt**: "Based on this phenomenon, we define the Alignment Agent as: A_Alignment(x + A'(x)) = A(x) - A'(x), The input for the agent is the input x for the agent to be aligned, along with A'(x). The output is A_Alignment(x + A'(x)), which is obtained through optimization by a large model and rules."

**Analysis**: Clear mathematical formulation with formal notation. Notice the systematic definition of inputs and outputs.

**Excerpt**: "In the Text-to-SQL task, common hallucination phenomena mainly refer to failures in instruction following and instability in output results. This is specifically manifested as: generating non-existent columns, changing database column names, syntax errors, mismatching database values with columns, and failing to adhere to the rules set in the prompt."

**Analysis**: Excellent specific enumeration of problems ("generating non-existent columns," "syntax errors," etc.). Notice the systematic approach to problem identification.

#### Subsection 3.2: Self-Taught Fewshot
**Content**: Dynamic few-shot generation with CoT augmentation
**Strengths**:
- Clear motivation (few-shot importance)
- Technical description (Query-CoT-SQL format)
- Specific examples (Listings 1, 2, 3)

**Excerpt**: "Few-shot is an important method to assist LLMs in generation, MCS-SQL, DAIL-SQL studied the critical role of problem representation in the Text-to-SQL task and proposed using question similarity to select appropriate few-shots to drive LLMs in generating SQL, achieving notable results."

**Analysis**: Strong positioning relative to prior work ("MCS-SQL, DAIL-SQL studied...achieving notable results"). Notice the acknowledgment of existing work before differentiation.

**Excerpt**: "Inspired by this, we attempted to use dynamic few-shots to enhance the efficiency of agents in the Text-to-SQL task. Additionally, we considered how to better leverage few-shots by extracting more information from the samples. Therefore, in OpenSearch-SQL, we first used Masked Question Similarity (MQs) to select similar queries. Then, we upgraded the few-shots in the Query-SQL format by self-taught."

**Analysis**: Clear positioning ("Inspired by this") with specific differentiation ("upgraded the few-shots...by self-taught"). Notice the systematic approach ("first used...Then, we upgraded").

#### Subsection 3.3-3.6: Framework Components
**Content**: Detailed description of Preprocessing, Extraction, Generation, and Refinement stages
**Strengths**:
- Clear stage-by-stage organization
- Technical details for each component
- Integration with alignment mechanism

**Excerpt**: "Preprocessing. Processing and constructing all auxiliary information that is insensitive to the NLQs, including database schema information, embedding databases, few-shot libraries, etc."

**Analysis**: Clear definition with specific examples. Notice the emphasis on "insensitive to the NLQs" showing design consideration.

**Excerpt**: "Refinement. Check and optimize the SQL based on the execution results using alignment strategies and rules. Then, select the final SQL based on self-consistency and voting results."

**Analysis**: Clear two-step process description ("Check and optimize...Then, select"). Notice the use of "self-consistency and voting" showing integration with existing techniques.

#### Subsection 3.7: Algorithm
**Content**: Overall algorithm specification (Algorithm 1)
**Strengths**:
- Complete algorithmic description
- Clear input/output specification
- Process flow description

**Excerpt**: "In this section, we provide an overall summary of OpenSearch-SQL and present the entire framework in Algorithm 1. In this algorithm, we take an NLQ as an example, encompassing each specific step from preprocessing to the final generation of SQL."

**Analysis**: Clear algorithmic presentation with comprehensive coverage ("each specific step"). Notice the systematic approach.

---

### Section 4: Experiments

#### Macro-Level Organization
**Content**: Comprehensive experimental evaluation
**Structure**: 4.1 Experimental Setup → 4.2 Main Results → 4.3 Ablation Studies → 4.4 Discussion

**Strengths**:
- Comprehensive dataset description
- Multiple evaluation metrics
- Ablation studies
- Discussion of results

**Excerpt**: "In this section, we demonstrate the effectiveness of OpenSearch-SQL through experiments and explore the role of its various module."

**Analysis**: Clear objective statement ("demonstrate effectiveness," "explore the role"). Notice the systematic approach.

**Excerpt**: "Our experimental results indicate that we achieved 69.3% EX on the Dev set, 72.28% EX on the Test set, and an R-VES score of 69.3%. All three metrics ranked first on the leaderboard at the time of submission, demonstrating that our method not only generates accurate SQL statements but also has a clear advantage in terms of time efficiency."

**Analysis**: Strong empirical validation with specific quantitative results. Notice the dual emphasis on accuracy ("accurate SQL statements") and efficiency ("time efficiency"). Temporal qualification ("at the time of submission") shows careful positioning.

---

## Cross-Disciplinary Comparison

### Computer Science (NLP/Database) vs. Traditional Academic Writing

| Aspect | OpenSearch-SQL Paper | Traditional Academic |
|---|---|---|
| **Literature Review Location** | Separate section (Section 5: Related Work) | Separate section after introduction |
| **Technical Detail Level** | Very high (algorithms, mathematical formulations, framework descriptions) | Medium (methods overview) |
| **Evaluation Focus** | Quantitative metrics, ablation studies, benchmark comparisons | Theoretical validation, qualitative analysis |
| **Contribution Claims** | Technical novelty + state-of-the-art performance + framework design | Theoretical advancement + empirical evidence |
| **Mathematical Formalism** | Extensive (equations, algorithms, formal notation) | Minimal to moderate |
| **Experimental Rigor** | Multiple datasets, ablation studies, comparison tables | Single study, qualitative results |
| **Framework Emphasis** | Strong focus on systematic framework design and component integration | Methods presented as techniques |

### Key Learning Points for Imitation

1. **Framework Thinking**: Systematic organization of components into clear stages (Preprocessing, Extraction, Generation, Refinement)
2. **Alignment Mechanism**: Novel approach to addressing multi-agent collaboration issues through consistency alignment
3. **Transferability Emphasis**: Strong focus on methods that don't require fine-tuning, emphasizing applicability
4. **Systematic Problem Identification**: Clear enumeration of limitations (L1, L2, L3) with specific examples
5. **Human-Centered Design**: Using human workflow as inspiration for framework design
6. **Mathematical Precision**: Formal definitions and algorithmic specifications

---

## Imitation Opportunities for Future Papers

### Structural Elements to Adapt
- **Systematic Framework Organization**: Breaking complex systems into well-defined stages (Preprocessing → Extraction → Generation → Refinement)
- **Mathematical Formulation**: Formal definitions of key concepts (Alignment Agent equation, Text-to-SQL task definition)
- **Algorithmic Descriptions**: Complete algorithm specifications (Algorithm 1) with clear input/output
- **Limitation Enumeration**: Clear numbering and categorization of identified problems (L1, L2, L3)
- **Multi-Component Integration**: Showing how different components work together through alignment mechanisms

### Rhetorical Strategies
- **Problem-Solution Mapping**: Explicitly connecting solutions to identified limitations ("To address L1," "For L2," "For L3")
- **Human-Centered Motivation**: Using human workflow as inspiration for technical design
- **Transferability Emphasis**: Highlighting methods that don't require fine-tuning or specialized datasets
- **Contribution Enumeration**: Clear listing of contributions with specific technical descriptions
- **State-of-the-Art Positioning**: Strong claims backed by quantitative results and benchmark rankings

### Quality Indicators
- **Mathematical Rigor**: Formal notation, algorithmic descriptions, mathematical formulations
- **Empirical Validation**: Multiple evaluation metrics, ablation studies, comprehensive comparisons
- **Framework Design**: Clear component separation with systematic integration
- **Transferability**: Emphasis on methods applicable without fine-tuning
- **Benchmark Performance**: State-of-the-art results with clear quantitative claims

---

## Key Excerpts from Original Paper

### Introduction Excerpts
1. "Text-to-SQL task attempts to automatically generate Structured Query Language (SQL) queries from Natural Language Queries (NLQ). This task can improve the ability to access databases without the need for knowledge of SQL."

2. "As the text-to-SQL problem is notoriously hard, these systems have been the holy grail of the database community for several decades."

3. "Limitation. Although the methods driven by LLMs have significantly raised the upper limits of the Text-to-SQL task capabilities, our analysis of previous work reveals that: L1 Due to the ambiguity of the overarching framework, there are some gaps at the methodological level."

4. "L2 LLM-driven approaches often rely on multi-agent collaboration. However, due to the instability of LLMs and the lack of guaranteed coherence and coupling between agents, later-executing agents may not use or only partially use the outputs of previously running agents. This leads to accumulated hallucinations and performance loss."

5. "Framework. To address L1, our research defines a Standard Text-to-SQL framework based on the process humans use to complete SQL construction. This can cover current research on LLM-driven Text-to-SQL tasks. We believe that a complete Text-to-SQL task framework should include four steps: Preprocessing, Extraction, Generation, Refine."

6. "For L2, we analyzed common hallucinations in multi-agent collaboration-driven Text-to-SQL tasks and designed a consistency alignment-based alignment agent for these hallucinations. By ensuring consistency in the functions, inputs, and outputs of specific agents, our aim is to reduce hallucinations during the model generation process."

7. "Contribution In summary, our contributions are as follows. • To the best of our knowledge, we are the first to propose a multi-agent cooperative framework based on consistency alignment for the Text-to-SQL task."

### Methodology Excerpts
8. "Based on this phenomenon, we define the Alignment Agent as: A_Alignment(x + A'(x)) = A(x) - A'(x), The input for the agent is the input x for the agent to be aligned, along with A'(x)."

9. "Inspired by this, we attempted to use dynamic few-shots to enhance the efficiency of agents in the Text-to-SQL task. Additionally, we considered how to better leverage few-shots by extracting more information from the samples."

10. "The Text-to-SQL task can be defined as: a task that translates a NLQ Q into an SQL query Y based on database information S, a specific model F(·|θ), and a particular prompt P."

11. "Inspired by these methods, this paper first systematically organizes these modules. We categorize existing methods into four stages: Preprocessing, Extraction, Generation, and Refinement."

### Experiments Excerpts
12. "Our experimental results indicate that we achieved 69.3% EX on the Dev set, 72.28% EX on the Test set, and an R-VES score of 69.3%. All three metrics ranked first on the leaderboard at the time of submission, demonstrating that our method not only generates accurate SQL statements but also has a clear advantage in terms of time efficiency."

---
