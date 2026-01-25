# Foundation-Expert Paper Macro-Level Structure Analysis

**Paper Title**: Realizing Scaling Laws in Recommender Systems: A Foundation–Expert Paradigm for Hyperscale Model Deployment
**Authors**: Li et al. (2025)
**Venue**: arXiv preprint (under review, likely KDD '26)
**Field**: Recommender Systems / Machine Learning
**Structure Type**: IMRaD (Introduction, Related Work, Methods, Experiments, Conclusion)

---

## Overall Macro-Level Assessment

### Structural Framework
**IMRaD Adaptation**: Introduction → Related Work → Methods (FM Design, Expert Design, System Deployment) → Experiments → Conclusion
- **Total Length**: Conference paper format (~10-12 pages estimated)
- **Citation Style**: Numeric (ACM style)
- **Disciplinary Conventions**: Heavy emphasis on production deployment, infrastructure, and real-world metrics
- **Rhetorical Style**: Problem-solution structure with strong production validation

### Hourglass Flow Analysis
**General → Specific → General** progression:
- **Introduction**: Broad scaling laws context → Specific deployment challenges in recommenders → Foundation-Expert paradigm solution
- **Related Work**: Broad field overview (long user history, representation learning) → Specific gaps → Positioning
- **Methods**: Technical specificity with formal definitions and architecture descriptions
- **Experiments**: Specific evaluation metrics and A/B testing → General production implications
- **Conclusion**: Specific findings → Broad impact on recommender systems

---

## Section-by-Section Macro Analysis

### Section 1: Introduction (CARS Model Application)

#### Move 1: Establishing Territory (Paragraphs 1-3)
**Content**: Claims centrality of scaling laws in deep learning
**Strengths**:
- Uses evaluative language: "fundamentally transformed industrial practice," "well-suited"
- Establishes broad significance across ML domains
- Temporal markers: "past years," "over the past two years"

**Excerpt**: "The identification and systematic characterization of scaling laws in deep learning models has fundamentally transformed industrial practice. While these principles originated in the study of large language models, they have since been validated and applied to the study recommender systems."

**Analysis**: Strong centrality claims with broad domain appeal. Notice how authors quickly pivot from general scaling laws to recommender-specific context.

#### Move 2: Establishing Niche (Paragraphs 4-8)
**Content**: Identifies specific deployment challenges in recommender systems
**Strengths**:
- Clear gap identification: "major unsolved challenge"
- Specific technical challenges: streaming data, shifting distributions, latency constraints
- Critique of existing approaches: SFT and teacher-student paradigms

**Excerpt**: "Despite the potential offered by scaling recommender models, their deployment in large-scale production environments presents a significant challenge. First, training large recommendation models often requires hundreds or even thousands of high-performance GPUs, making efficient iteration challenging for researchers and developers. Second, recommendation systems typically consist of multiple applications and surfaces, each requiring dedicated development and tuning, making scaling and maintaining of dedicated large models for each impractical."

**Analysis**: Gap is highly specific and production-oriented. Notice the enumeration of concrete challenges (GPU requirements, multiple surfaces).

#### Move 3: Occupying Niche (Paragraphs 9-12)
**Content**: Presents Foundation-Expert paradigm as solution with specific contributions
**Strengths**:
- Clear positioning: "In this work, we propose the Foundation-Expert paradigm"
- Specific technical innovation: target-aware embeddings
- Production validation: "deployed at Meta serving tens of billions of user requests daily"

**Excerpt**: "In this work, we propose the Foundation-Expert paradigm, an alternative to methods like SFT or knowledge distillation. Our approach integrates a large, general-purpose foundation model (FM) with smaller, specialized expert models, decoupling general knowledge learning from task-specific adaptation. This separation addresses production bottlenecks and ensures computational feasibility in demanding online streaming environments."

**Analysis**: Strong positioning with clear technical differentiation. The use of bold terms emphasizes key innovations. Production scale evidence is prominently featured.

#### Key Linguistic Features
- **Nominalization**: "deployment," "optimization," "iteration" - creates technical formality
- **Technical Terminology**: HSTU, FM, embeddings, transfer ratio - assumes expert audience
- **Acronyms**: FM (Foundation Model), SFT (Supervised Fine-Tuning), TAE (Target-Aware Embeddings)

---

### Section 2: Related Works (Literature Review Structure)

#### Move 1: Thematic Organization
**Content**: Broad categorization of related work
**Strengths**:
- Clear thematic grouping: Long User History Modeling, Learning Rich Representations
- Temporal progression: "over the past two years," "recent works"
- Connection to Introduction: references challenges mentioned earlier

**Excerpt**: "In the previous section we discussed connections to SFT and teacher-student paradigms. In this section we focus on connections to long user history modeling and methods for learning rich user representations for recommendation systems."

**Analysis**: Clear structural cue that connects to previous section. Thematic organization is logical and comprehensive.

#### Move 2: Critical Analysis
**Content**: Evaluation of related approaches
**Strengths**:
- Specific citations: Meta, LinkedIn, ByteDance, Xiaohongshu, Alibaba
- Comparative positioning: "orthogonal to these previous work"
- Identification of limitations: "inherently limited in the expressiveness"

**Excerpt**: "Our work is orthogonal to these previous work, as we focus on how to efficiently productionalize the scaled model via a Foundation-Expert framework. Most of those innovations can be applied to our FM design."

**Analysis**: Strong positioning with "orthogonal" distinction. Notice the practical focus on productionalization vs. algorithmic innovation.

#### Move 3: Research Gaps (Implicit throughout)
**Content**: Gaps emerge through critique
**Strengths**:
- Gap identification: "struggles to achieve a high transfer ratio"
- Specific limitation: "without focusing on representation of user and item pair"
- Production-oriented gap: offline training vs. online streaming

**Excerpt**: "These methods largely focus on learning general user or item summarization independently, without focusing on representation of user and item pair—user's target-aware representation is about the user's interest in a specific item based on his/her behavior sequence and the item information. While this approach is beneficial in terms of computational efficiency, it is inherently limited in the expressiveness of the representations it can learn."

**Analysis**: Gap is established through direct technical critique. The dash construction emphasizes the definition of "target-aware."

---

### Section 3: Methods (Technical Core)

#### Macro-Level Organization
**Content**: Foundation Model design, Expert design, System deployment
**Strengths**:
- Clear subsections with hierarchical structure
- Formal mathematical definitions and notation
- Production infrastructure details
- Figure references for architectural visualization

**Analysis**: Highly technical section with strong mathematical foundation. The inclusion of infrastructure (HyperCast) is notable for a methods section.

#### Subsection: Foundation Model Design

**Input Features Organization**
**Excerpt**: "Main Features are used for target-aware sequential modeling to generate the FM embeddings. These include the user's interaction history and information about the target items. Each item (historical or target) is represented by its categorical features such as item ID p, contextual features c (which includes but not limited to surface type, timestamp, LLM-powered multi-modal representations), and the associated user action a."

**Analysis**: Clear categorization of features with specific examples. Technical notation (p, c, a) is introduced systematically.

**Target-aware Sequential Modeling**
**Excerpt**: "Building upon the original HSTU architecture, we introduce an architectural simplification: instead of interleaving item and action embeddings, we combine them via direct summation. Furthermore, to prevent label leakage from user history, we remove the auto-regressive auxiliary losses. This optimization effectively halves the input sequence length, yielding a 50% reduction in complexity for the linear projection layers and a 25% reduction for the attention operations."

**Analysis**: Strong technical justification with quantitative efficiency claims. "Label leakage" is an important production concern highlighted.

**Foundation Model Alignment (MTML)**
**Excerpt**: "Similar to many recommendation models, our FM is optimized using a multi-task multi-label (MTML) learning objective. The overall loss function L consists of two components, L = Σₛ₌ₛωₛₛL_mainₛₛ + Σₛ₌ₛωₛₛL_auxₛₛ where L_mainₛₛ and L_auxₛₛ denote the loss of each shared main task and surface-specific auxiliary task respectively"

**Analysis**: Formal mathematical definition with clear notation. The distinction between main and auxiliary losses is crucial for surface alignment.

#### Subsection: Expert Design

**Excerpt**: "By offloading the compute-heavy task of general knowledge acquisition to the Foundation Model (FM), experts can be substantially smaller than their one-stage counterparts. This enables rapid iteration cycles focused exclusively on surface-specific optimizations. The primary architectural difference from their one-stage counterparts is the inclusion of three components: a FM Embedding Module, a FM Fusion Module, and a lightweight HSTU module dedicated to capturing short-term, real-time user interests."

**Analysis**: Clear architectural comparison with "compute-heavy" vs "lightweight" distinction. Three-module organization is systematic.

#### Subsection: System Deployment (HyperCast)

**High Freshness**
**Excerpt**: "HyperCast enables exceptional model and data freshness, which is critical in a real-time recommendation environment. For model freshness, both the FM and experts are trained in online streaming fashion. HyperCast facilitates independent and high-frequency model updates, employing a component-wise streaming synchronization mechanism. Specifically, instead of publishing and updating a full model snapshot which can be time-consuming, only part of (e.g. 30%) the most recently updated model weights are published and synchronized with the inference server, allowing for model refreshes on the order of several minutes without service disruption."

**Analysis**: Production-focused with specific technical details (component-wise sync, 30% partial updates, minutes-level freshness).

**Decoupled Training Architecture**
**Excerpt**: "A core design principle of our paradigm is the complete decoupling of the FM and expert model iterations. This is achieved by materializing the FM's target-aware embeddings and logging them as candidate-level features available in the training data. Consequently, the FM and expert training jobs can operate independently, each consuming its own data and updating its weights without direct dependencies on the other's training state."

**Analysis**: Strong emphasis on decoupling as a "core design principle." "Materializing embeddings" is a key technical term.

---

### Section 4: Experiments (Evaluation)

#### Macro-Level Organization
**Content**: Effectiveness, transfer efficiency, generalization, online performance
**Strengths**:
- Clear evaluation metrics: Normalized Entropy (NE)
- Ablation studies: target-aware embeddings vs. user embeddings
- Transfer ratio quantification
- Production A/B test results

**Analysis**: Strong empirical evaluation with both offline and online metrics. The transfer ratio concept is a novel metric.

#### Experiment Setup: Evaluation Metrics

**Excerpt**: "In the present work, we estimate the offline performance of our approach using the Normalized Entropy (NE). NE is the usual cross-entropy loss normalized by the the entropy of the data distribution. For example, given N training examples and letting yᵢ ∈ {0, 1} be the label of the iᵗʰ training example, the NE is estimated as, NE = (1/N Σᵢyᵢlog pᵢ + (1-yᵢ)log(1-pᵢ)) / (p log p + (1-p)log(1-p)) where p=1/N Σᵢyᵢ and pᵢ is predicted probability for example i."

**Analysis**: Formal metric definition with mathematical notation. Practical utility is explained: "less sensitive to datasets where the number of negative examples greatly outnumbers the number of positive examples."

#### Effectiveness of Target-Aware Embeddings

**Excerpt**: "The results are summarized in Table 1. The "Baseline" model is a production model that excludes both user embeddings and our proposed target-aware embeddings. It clearly shows that adding our target-aware embeddings to the baseline yields substantial NE improvements across all tasks, significantly outperforming the gains achieved by adding the user embeddings. Furthermore, an ablation study adding the user embeddings on top of our system shows only minor additional improvements. This indicates that our approach efficiently captures the necessary signals for modeling a user's interest in a specific candidate, validating the efficacy of our strategy."

**Analysis**: Clear ablation design with controlled comparison. "Substantial NE improvements" is specific quantitative claim.

#### Foundation-to-Expert Transfer Efficiency

**Excerpt**: "We define the Transfer Ratio (TR) between a pair of FMs for a given expert as, TR = (NE(Expert_FM₁) - NE(Expert_FM₂)) / (NE(FM₁) - NE(FM₂)) Here, NE represents the Normalized Entropy, our primary offline performance metric. The TR measures the proportional improvement in the expert model relative to the underlying improvement in the foundation model. A higher TR value signifies a more efficient paradigm, ensuring that investments in scaling the FM yield corresponding performance gains in downstream expert models."

**Analysis**: Novel metric with clear formal definition. Higher TR = more efficient paradigm. This is a key contribution metric.

**Results**
**Excerpt**: "These results demonstrate that scaling gains from the FM are efficiently propagated to expert models across various surfaces, which can save considerable training resources and engineering effort that would otherwise be dedicated to scaling each model independently."

**Analysis**: Strong practical impact claim. Results show TR in range [0.64, 1.0], which is quantitatively stated.

#### Online Performance

**Excerpt**: "We validated our proposed paradigm through extensive online A/B tests on several core recommendation surfaces. The results demonstrated statistically significant improvements on all surfaces across both engagement and consumption metrics, including a notable shift in engagement towards fresher content. Moreover, these user-facing improvements were achieved without compromising system performance. The infrastructure metrics such as end-to-end serving latency and CPU performance remained neutral."

**Analysis**: Production validation is emphasized. "Statistically significant" and "remained neutral" are important qualifiers.

---

### Section 5: Conclusion

#### Macro-Level Organization
**Content**: Summary of contributions, production deployment, future implications
**Strengths**:
- Clear restatement of paradigm
- Production scale evidence
- Limitation acknowledgment (implicit)
- Future directions

**Excerpt**: "In this paper, we introduced the Foundation-Expert paradigm, a novel approach for deploying hyperscale recommender systems. By decoupling a central, compute-heavy FM from lightweight, surface-specific Experts, our framework facilitates highly efficient and generalizable knowledge transfer at a massive scale via target-aware embeddings. We demonstrated that this paradigm, powered by our HyperCast infrastructure, overcomes the limitations of traditional knowledge distillation and provides statistically significant improvements in online metrics in A/B testing."

**Analysis**: Strong conclusion that restates core contributions. Production evidence is prominently mentioned.

**Production Scale Evidence**
**Excerpt**: "Currently, the proposed paradigm is fully deployed across multiple core recommendation surfaces at Meta, serving tens of billions of daily user requests. This work provides a proven blueprint for realizing the benefits of scaling laws in complex, real-time recommendation environments."

**Analysis**: Concrete scale evidence ("tens of billions of daily user requests"). "Proven blueprint" positioning is strong claim.

---

## Cross-Disciplinary Comparison

### Recommender Systems vs. Traditional Academic Writing

| Aspect | Foundation-Expert Paper | Traditional Academic |
|---|---|---|
| **Literature Review Location** | Separate section after introduction | Integrated into introduction |
| **Technical Detail Level** | Very high (infrastructure, production metrics) | Medium (methods overview) |
| **Evaluation Focus** | Production A/B tests, transfer ratio, latency | Theoretical validation, standard metrics |
| **Contribution Claims** | Technical + Infrastructure + Production deployment | Theoretical + Empirical |
| **Scale Emphasis** | Tens of billions of daily requests | Usually academic scale |
| **Industry Context** | Strong (Meta production system) | Varies, often minimal |

### Key Learning Points for Imitation

1. **Production Validation**: Extensive use of production-scale evidence
2. **Infrastructure Integration**: Methods section includes detailed infrastructure (HyperCast)
3. **Novel Metrics**: Introduction of domain-specific metrics (Transfer Ratio)
4. **Quantitative Efficiency Claims**: Specific percentages (20-40%, 50% reduction)
5. **Scale Emphasis**: Concrete production scale throughout

---

## Imitation Opportunities for Future Papers

### Structural Elements to Adapt
- **Two-Stage Paradigm Description**: Clear separation of Foundation Model and Expert design
- **Infrastructure as Methods**: Including production infrastructure in technical sections
- **Production Metrics**: Using A/B test results and real-world metrics
- **Efficiency Quantification**: Concrete computational savings with percentages

### Rhetorical Strategies
- **Production Credibility**: "deployed at Meta serving tens of billions of user requests daily"
- **Novel Metric Introduction**: Formal definition and application of Transfer Ratio
- **Technical Differentiation**: "orthogonal to these previous work" positioning
- **Infrastructure Claims**: "High Freshness," "Decoupled Training Architecture" as named concepts

### Quality Indicators
- **Mathematical Rigor**: Formal definitions for loss functions and metrics
- **Empirical Validation**: Offline NE metrics + Online A/B tests
- **Production Evidence**: Concrete deployment scale and performance metrics
- **Infrastructure Detail**: Specific implementation details (component-wise sync, 30% partial updates)
