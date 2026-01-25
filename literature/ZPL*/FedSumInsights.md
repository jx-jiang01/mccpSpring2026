# FedSum Paper Macro-Level Structure Analysis

**Paper Title**: FedSum: Data-Efficient Federated Learning Under Data Scarcity Scenario For Text Summarization  
**Authors**: Ma, Li, Shi, Chen (2025)  
**Journal**: AAAI 2025  
**Field**: Federated Learning / Natural Language Processing  
**Structure Type**: IMRaD (Introduction, Background, Methods, Experiments, Conclusion)

---

## Overall Macro-Level Assessment

### Structural Framework
**IMRaD Adaptation**: Introduction → Background → Task Definition → Method → Experiments → Conclusion
- **Total Length**: ~10 pages (conference paper format)
- **Citation Style**: AAAI format
- **Disciplinary Conventions**: Heavy emphasis on algorithmic methodology, federated learning frameworks, and quantitative evaluation metrics
- **Rhetorical Style**: Problem-solution structure with strong technical justification and empirical validation

### Hourglass Flow Analysis
**General → Specific → General** progression is well-executed:
- **Introduction**: Broad applications (text summarization, privacy concerns) → Specific technical problem (data scarcity in FL) → Contribution claims
- **Background**: Broad field overview → Specific gaps → Positioning of current work
- **Methods**: Technical specificity with algorithmic formalism
- **Experiments**: Specific evaluation → General implications
- **Conclusion**: Specific findings → Broad impact

---

## Section-by-Section Macro Analysis

### Section 1: Introduction (CARS Model Application)

#### Move 1: Establishing Territory (Paragraphs 1-3)
**Content**: Claims centrality of text summarization and federated learning
**Strengths**:
- Uses evaluative language: "explosively," "productivity enhancement," "crucial"
- Establishes broad significance across multiple domains
- Present/present perfect tense: "has grown," "prohibiting access"

**Excerpt**: "The amount of text data has grown explosively in various domains, such as journalism, medicine, and entertainment. For productivity enhancement, the summarization model, namely summarizer, compresses textual content into shorter versions while retaining key concepts from input content."

**Analysis**: Strong centrality claims supported by practical applications. Notice the interdisciplinary appeal - connects technical CS work to real-world domains like journalism and medicine.

#### Move 2: Establishing Niche (Paragraphs 4-5)
**Content**: Identifies specific gaps in current approaches
**Strengths**:
- Clear gap identification: "private and sensitive," "infeasible to collect," "data scarcity"
- Specific technical challenge: "less than 500 samples" with "over 10M parameters"
- Opposing viewpoint: contrasts centralized methods with privacy-preserving FL needs

**Excerpt**: "Nevertheless, when the FL system is plagued by data scarcity (e.g., under edge computing or cold starting settings, where each FL client trains a common and basic summarization model with over 10M parameters with less than 500 samples), it is intractable for the summarizer to get adequate knowledge and vulnerable to data bias, such as Leading Bias, resulting in performance degradation."

**Excerpt**: "Then a natural question is: {\it How to derive a well-behaved summarizer in data scarcity FL?}"

**Analysis**: Gap is highly specific and researchable. Uses explicit question format ("Then a natural question is") for academic emphasis while making strong novelty claim. Notice the specific numerical constraints (500 samples, 10M parameters) that make the problem concrete.

#### Move 3: Occupying Niche (Paragraphs 6-9)
**Content**: Presents FedSum as solution with specific contributions
**Strengths**:
- Clear objectives: "maximize the data efficiency"
- Specific outcomes: "depth and breadth extensions"
- Roadmap: outlines paper organization and technical approach

**Excerpt**: "To find an effective solution for the degeneration, we propose to maximize the data efficiency in model training. We study the strategy of sample weighting, and mining hidden knowledge from different aspects. We propose FedSum which extends the standard FL framework from depth and breadth to further extract prime and diversified knowledge for constructing the summarizer."

**Excerpt**: "For depth extension, inspired by hard sample mining and bias elimination \cite{ chen2023bias}, we introduce the Data Partition method to recognize the prime samples, and adjust the weight of data by the proposed Data skip mechanism, to further mining prime knowledge. Specifically, we refer to the samples with more unbiased and higher loss samples as prime samples, while pronounced data bias and low supervised loss as normal samples."

**Excerpt**: "For breadth extension, inspired by Multi-Task learning \cite{NEURIPS2021_82599a4e,Fed-CO2}, we extend the source of knowledge in training. FedSum not only learns from data but also from hidden spaces and parameters."

**Analysis**: Strong positioning with enumerated challenges and solutions. Notice the two-pronged approach (depth and breadth) and the explicit connection to prior work through citations.

#### Key Linguistic Features
- **Nominalization**: "compression," "summarization," "degeneration" - creates technical formality
- **Passive Voice**: "is plagued by," "are generally private" - emphasizes processes over agents
- **Technical Terminology**: FL, Leading Bias, BERTSUM - assumes expert audience
- **Mathematical Precision**: Specific numbers (500 samples, 10M parameters, ≤ 2.6%) for credibility

---

### Section 2: Background (Literature Review Structure)

#### Move 1: Thematic Overview (Paragraphs 1-2)
**Content**: Broad overview of extractive summarization and federated learning fields
**Strengths**:
- Establishes scope: "text summarization," "privacy-preserving"
- Temporal progression: "Inspired by the success of BERT"
- Thematic grouping: extractive summarization methods, FL algorithms

**Excerpt**: "Inspired by the success of BERT, a summarizer with an enlightening pattern has been proposed \cite{liu-lapata-2019-text}, namely BERTSUM. It leverages BERT to represent the input content and then recognizes the most salient sentences by classification modules."

**Analysis**: Clear positioning relative to existing work. Notice how authors establish BERTSUM as a foundational work before introducing their approach.

#### Move 2: Critical Analysis (Paragraphs 3-5)
**Content**: Detailed evaluation of related FL approaches
**Strengths**:
- Thematic organization: heterogeneity solutions, data scarcity solutions
- Critical evaluation: "might have difficulty," "not always behave outstanding"
- Comparative analysis: strengths/weaknesses of different approaches

**Excerpt**: "To alleviate the degradation due to heterogeneity, FedProx \cite{FedProx} introduces a proximal term to restrain the local drift. SCAFFOLD \cite{SCAFFOLD} learns personalized control variates referring directions of global updates to guide the local training."

**Excerpt**: "These above methods mitigate the negative effects of data heterogeneity and scarcity, but not always behave outstanding in the summarization task, due to the neglect of data bias."

**Analysis**: Strong critical analysis with clear limitations identified. Uses "but not always behave outstanding" for academic hedging while emphasizing the gap their work addresses. Notice the specific critique: "due to the neglect of data bias" - this directly sets up their contribution.

#### Move 3: Research Gaps (Implicit throughout)
**Content**: Gaps emerge through critique of existing work
**Strengths**:
- Gap identification through limitation analysis
- Data bias emphasis: "neglect of data bias"
- Specific technical gaps: multi-knowledge extraction, data partition methods

**Analysis**: Gaps are established through systematic critique rather than explicit "gap" section. Notice the repeated emphasis on data bias, which becomes a key contribution of their work.

---

### Section 3: Task Definition and Notations (Methodological Foundation)

#### Macro-Level Organization
**Content**: Formal mathematical definitions and notation system
**Strengths**:
- Clear mathematical formalism
- Systematic notation: consistent use of symbols throughout
- Task-specific definitions: extractive summarization formulation

**Excerpt**: "Given a document (data sample) $d=\{u_1,\cdots,u_S\}$ with $S$ sentences from dataset $D=\{d_1,\cdots,d_n\}$, each sentence is assigned a result $\hat{\phi} \in [0, 1]$ through the model (summarizer), representing the probability that the sentence should be extracted."

**Excerpt**: "General extractive summarizer $f(\Omega, \cdot)$ parametered by $\Omega=\{\theta, \omega\}$ can be divided into the representation model $r(\theta, \cdot) $ and the classification head $h(\omega, \cdot)$, where $f(\Omega, \cdot) = h(\omega, r(\theta, \cdot))$."

**Analysis**: Strong methodological section with clear mathematical foundation. Notice the decomposition of the model into representation and classification components, which becomes important for their federated approach.

---

### Section 4: Method (Core Technical Contribution)

#### Macro-Level Organization
**Content**: Technical methodology presentation with two main innovations
**Strengths**:
- Clear problem statement: "knowledge shortage problem"
- Modular architecture explanation: Data Partition, Multi-knowledge Local Training
- Mathematical formalism: loss functions, algorithmic procedures
- Algorithm presentation: Detailed pseudocode in algorithms

**Excerpt**: "The data scarcity leads to the knowledge shortage problem, affecting the performance of the summarizer. To address this problem by maximizing the data efficiency, we propose FedSum with two innovative modules: Data Partition and Multi-knowledge Local Training, for depth and breadth extensions, as concluded in Alg.\ref{alg:FedSum} and Alg. \ref{alg:FedSum Client}."

**Excerpt**: "For depth extension, inspired by hard sample mining and bias elimination \cite{ chen2023bias}, we introduce the Data Partition method to recognize the prime samples, and adjust the weight of data by the proposed Data skip mechanism, to further mining prime knowledge."

**Excerpt**: "For breadth extension, inspired by Multi-Task learning \cite{NEURIPS2021_82599a4e,Fed-CO2}, we extend the source of knowledge in training. FedSum not only learns from data but also from hidden spaces and parameters."

**Excerpt**: "Since the prototype is generally regarded as the carrier of semantic information in hidden space \cite{Prototypical2}, we leverage different prototypes to build prototype loss, improving the generalization and discrimination of features."

**Excerpt**: "Then, FedSum constructs the semantic portraits for FL clients by their specific prototypes, and measures the semantic distances between them to maintain the Portrait Distance Table (PDT) on the server."

**Analysis**: Highly technical section with strong mathematical foundation. Notice the use of algorithmic references and the systematic approach to knowledge extraction from multiple sources (data, hidden spaces, parameters).

#### Subsection 4.1: Data Partition
**Content**: Methodology for identifying prime vs. normal samples
**Strengths**:
- Sentence-level granularity: "detailed down to the sentence level"
- Bias-aware: considers "leading bias"
- Collaborative approach: combines local and global information

**Excerpt**: "Similar to recognizing noisy samples \cite{FedDiv}, data can be allocated to normal and prime subsets according to their significance for better exploration. In ML, the sample with large training loss is generally considered as a prime sample \cite{wang2023hard}, which can reflect more guidance about the task."

**Excerpt**: "Considering the characteristics of ExtSum, that the extractive summarization can be decomposed to the classification of multiple sentences \cite{0A}, we propose that the criterion for the prime sample should be detailed down to the sentence level."

**Excerpt**: "Since the amount of key sentences is much less than the ordinary, the loss of sentences labeled with ``1'' is more valuable, which can precisely reflect the dilemma in classification."

**Excerpt**: "Meanwhile, the label distribution can intuitively reflect the degree of leading bias in the data batch. Thus we refer to the samples with pronounced leading bias and low supervised loss as normal samples, while more unbiased and higher loss samples as prime samples."

**Analysis**: Strong technical justification with domain-specific insights. Notice how they adapt general ML concepts (hard sample mining) to the specific task (extractive summarization).

#### Subsection 4.2: Multi-knowledge Local Training
**Content**: Three-pronged knowledge extraction approach
**Strengths**:
- Comprehensive coverage: data, hidden space, parameters
- Technical detail: prototype construction, PDT maintenance
- Privacy consideration: "perturbated by Bernoulli noise"

**Excerpt**: "For the lack of knowledge problem caused by data scarcity, FedSum maximizes data efficiency by mining diversified knowledge from three aspects: data, hidden space, and received parameters."

**Excerpt**: "Since the proportion of normal samples is more than the proportion of prime, it's common for the model to ignore those prime data, threatening the generalization \cite{kawaguchi2020orderedsgdnewstochastic,xing2021demoting}."

**Excerpt**: "Due to data scarcity, FedSum does not discard all normal samples to avoid exacerbating degradation. Instead, we propose the Data skip mechanism to skip normal samples according to the skipping probability $\rho_{(i,j)}$ which increases with training progress."

**Excerpt**: "Given $j$-th batch $\mathcal B_j$ from $i$-th client belongs to normal subset $D_{(i,N)}$,  the skipping probability $\rho_{(i,j)} = \frac{t}{T} \cdot \frac{e}{E} \cdot \frac{j}{\tau_i}$ is determined by the progress in communication, epoch, and local update."

**Excerpt**: "To extract knowledge from hidden space, we take the prototype as the carrier. Following the definition of the class prototype presented in literature \cite{FedProto,FedCluster,chen2023evolvingsemanticprototypeimproves}, we denote the class $\xi$ prototype of $D_{(i,F)}$ in $t$-th communication round as $P_{(i,c)}^{(\xi,t)}$"

**Analysis**: Excellent technical detail with mathematical precision. Notice the progressive probability mechanism and the careful consideration of privacy constraints.

---

### Section 5: Experiments (Evaluation)

#### Macro-Level Organization
**Content**: Comprehensive quantitative and qualitative evaluation
**Strengths**:
- Clear evaluation metrics: ROUGE scores (R-F, R-R)
- Multiple baselines: FedAvg, FedProx, SCAFFOLD, FedNova, FedProto, FedDC
- Multiple datasets: CNN/DailyMail, PubMed, WikiHow, Reddit
- Heterogeneity analysis: Different Dirichlet parameters

**Excerpt**: "We investigate the milestone model, BERTSUM, in FL experiments. Several representative algorithms are adopted as baselines: FedAvg \cite{mcmahan2017communication}, FedProx \cite{FedProx}, SCAFFOLD \cite{SCAFFOLD}, FedNova \cite{FedNova}, FedProto \cite{FedProto}, and FedDC \cite{FedDC}."

**Excerpt**: "To simulate the data scarcity scenarios, only 2K training samples can be accessed by the FL system. To simulate the non-IID setting, we construct the quantity skew following \cite{li2022federated,cai2023efficient} and control the heterogeneity levels through $Dir$. Smaller $Dir$ indicates a more imbalanced scenario about clients' data quantity, and $Dir=+\infty$ represents the uniform case."

**Excerpt**: "Overall, FedSum obtains significant improvement in performance over baselines. The most obvious improvements compared to FedAvg are $1.6\%/1.31\%/1.52\%$ in R-F and $2.18\%/1.82\%/2.05\%$ in R-R on CNNM."

**Excerpt**: "Under data heterogeneity, comparing FedSum with the optimal baseline, there exists 0.15\% total improvement at least, and 29.9\% total improvement at most over ROUGE metrics on two datasets. These results demonstrate the effectiveness of FedSum."

**Excerpt**: "The performance of FedSum fluctuates slightly ($\leq 2.6 \%$ on CNNDM) as $Dir$ increases. When $Dir$ is 8, the FedSum ranks second with small gaps from the highest ($\leq 1.5\%$), verifying the generalization of FedSum under different heterogeneous."

**Excerpt**: "To verify the efficacy of tackling the degeneration caused by leading bias, we compare the position of the exacted sentences in the summaries generated between FedSum, FedAvg, and Oracle, following the setting of \citet{liu-lapata-2019-text}, where the Oracle stands for the ground-true summaries. As shown in Fig.~\ref{fig:labeldistribution}, the distribution of the extracted proportion about FedSum is more similar to the same of Oracle than FedAvg."

**Analysis**: Strong empirical evaluation with appropriate statistical measures. Notice the comparison baselines, ablation studies, and comprehensive evaluation across multiple dimensions (heterogeneity, bias, scalability).

---

### Section 6: Conclusion and Limitation

#### Macro-Level Organization
**Content**: Synthesis, contributions, limitations, and future work
**Strengths**:
- Clear contribution summary
- Balanced limitations discussion
- Future directions identified
- Broader impact consideration

**Excerpt**: "In this paper, we explore the text summarization task in FL, which is more realistic and private than related methods built upon the centralized storage. Besides, data scarcity generally arouses performance degeneration and magnifies the negative effect of leading bias."

**Excerpt**: "FedSum demonstrates its promising improvement over baselines on benchmark datasets, while exhibiting its generalization in tackling the intricacies of data heterogeneity. We further verify the scalability of FedSum with various data quantities and the efficacy in mitigating the negative effect of data bias."

**Excerpt**: "Future investigations can build from this foundation to examine other capabilities of the model under data scarcity FL, like stability and fairness. Further experiments are needed to verify the adaptability of our framework for other NLP tasks(e.g. machine translation and sentiment analysis). Besides, our evaluation methodology is based on averages across three experimental runs, which could be enhanced through more rigorous statistical analysis."

**Analysis**: Strong conclusion that restates contributions and addresses limitations transparently. Notice the explicit mention of statistical analysis limitations and future directions.

---

## Cross-Disciplinary Comparison

### Computer Science vs. Traditional Academic Writing

| Aspect | FedSum Paper | Traditional Academic |
|---|---|---|
| **Literature Review Location** | Separate section after introduction | Integrated into introduction |
| **Technical Detail Level** | Very High (algorithms, math, architectures) | Medium (methods overview) |
| **Evaluation Focus** | Quantitative metrics, ablation studies, multiple datasets | Theoretical validation, qualitative analysis |
| **Contribution Claims** | Technical novelty + algorithmic innovation | Theoretical advancement + empirical evidence |
| **Mathematical Formalism** | Extensive use of equations and algorithms | Moderate mathematical notation |

### Key Learning Points for Imitation

1. **Algorithmic Precision**: Use of formal algorithmic descriptions with pseudocode
2. **Multi-dimensional Evaluation**: Strong focus on multiple evaluation dimensions (heterogeneity, bias, scalability)
3. **Evaluation Rigor**: Multiple evaluation metrics, ablation studies, comprehensive baselines
4. **Modular Structure**: Clear separation of technical components (depth vs. breadth extensions)
5. **Privacy-First Design**: Emphasis on federated learning constraints and privacy preservation

---

## Imitation Opportunities for Future Papers

### Structural Elements to Adapt
- **Two-pronged Approach**: Depth and breadth extensions as a framework
- **Modular Architecture**: Breaking complex systems into understandable components (Data Partition, Multi-knowledge Training)
- **Algorithmic Presentation**: Detailed pseudocode with line-by-line explanations
- **Comprehensive Evaluation**: Multiple datasets, multiple metrics, multiple baselines

### Rhetorical Strategies
- **Problem Novelty**: Explicit question format ("Then a natural question is") + specific technical gaps
- **Technical Positioning**: Clear differentiation from related work with specific critiques
- **Practical Relevance**: Connecting technical contributions to real-world constraints (privacy, data scarcity)
- **Quantitative Precision**: Specific numerical improvements and bounds (0.15% to 29.9%, ≤ 2.6%)

### Quality Indicators
- **Mathematical Rigor**: Formal definitions and loss functions with precise notation
- **Empirical Validation**: Multiple evaluation metrics and baselines across datasets
- **Reproducibility**: Clear algorithmic descriptions and experimental setup details
- **Scalability Analysis**: Explicit evaluation of method's behavior under varying conditions
