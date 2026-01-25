# Top-K Representative Search Paper Macro-Level Structure Analysis

**Paper Title**: Top-K Representative Search for Comparative Tree Summarization
**Authors**: Yuqi Chen, Xin Huang, Bilian Chen (2025)
**Journal**: IEEE Transactions on Knowledge and Data Engineering, VOL. 37, NO. 8, AUGUST 2025
**Field**: Data Engineering / Graph Algorithms / Tree Summarization
**Structure Type**: IMRaD (Introduction, Related Work, Problem Statement, Methods, Experiments, Conclusion)

---

## Overall Macro-Level Assessment

### Structural Framework
**IMRaD Adaptation**: Introduction → Related Work → Problem Statement → SVDT Algorithm → Experiments → Conclusion
- **Total Length**: ~8 pages (journal paper format)
- **Citation Style**: IEEE numeric system
- **Disciplinary Conventions**: Heavy emphasis on algorithmic methodology, mathematical formalism, experimental evaluation
- **Rhetorical Style**: Problem-solution structure with strong technical justification

### Hourglass Flow Analysis
**General → Specific → General** progression is well-executed:
- **Introduction**: Broad applications (graph visualization, conferences, disease ontology) → Specific technical problem (comparative tree summarization) → Contribution claims
- **Related Work**: Broad field overview (graph summarization) → Specific gaps (single tree vs. comparative) → Positioning of current work
- **Problem Statement**: Technical specificity with mathematical definitions
- **Methods**: Detailed algorithmic specificity with formal notation
- **Experiments**: Specific evaluation → General implications
- **Conclusion**: Specific findings → Broad impact

---

## Section-by-Section Macro Analysis

### Section 1: Introduction (CARS Model Application)

#### Move 1: Establishing Territory (Paragraphs 1-2)
**Content**: Claims centrality of graph visualization and tree summarization

**Strengths**:
- Uses evaluative language: "useful," "important," "enhance understanding"
- Establishes broad significance: graph visualization, data summarization
- Present/present perfect tense: "Graphs composed of nodes and edges are often used," "Data summarization aims at utilizing"

**Excerpt**: "Graphs composed of nodes and edges are often used to depict complex datasets [2], [3]. Graph visualization gives a simplified presentation with an intuitive overview for users. However, graphs can only enhance understanding if the size of summary answers is small enough in a manageable scale for human comprehension [1]."

**Analysis**: Strong centrality claims supported by practical applications. Notice the emphasis on human comprehension and manageable scale - connects technical CS work to usability concerns.

**Excerpt**: "Data summarization aims at utilizing a small-scale summary to represent massive datasets as a whole, which is useful for visualization and information sipped generation."

**Analysis**: Clear statement of the broader field's goals, setting the stage for the specific problem addressed.

#### Move 2: Establishing Niche (Paragraphs 3-5)
**Content**: Identifies specific gaps in comparative tree summarization

**Strengths**:
- Clear gap identification: "most existing studies of hierarchical summarization only work on one single tree"
- Specific technical challenge: comparative summarization on two trees
- Concrete examples: SIGMOD conference papers example

**Excerpt**: "However, most existing studies of hierarchical summarization only work on one single tree by selecting k representative nodes, which neglects an important problem of comparative summarization on two trees."

**Analysis**: Gap is highly specific and researchable. Uses "however" and "neglects" to clearly establish the limitation of existing work.

**Excerpt**: "In this paper, given two trees with the same topology structure and different node weights, we aim at finding k representative nodes, where k1 nodes summarize the common relationship between them and k2 nodes highlight significantly different subtrees meanwhile satisfying k1 + k2 = k."

**Analysis**: Precise problem statement that defines both the input (two trees with same topology, different weights) and the output (k representative nodes split between similarity and difference).

**Excerpt**: "To optimize summarization results, we introduce a scaling coefficient for balancing the summary view between two subtrees in terms of similarity and difference. Additionally, we propose a novel definition based on the Hellinger distance to quantify the node distribution difference between two subtrees."

**Analysis**: Preview of technical contributions - scaling coefficient and Hellinger distance - shows the paper's methodological approach.

#### Move 3: Occupying Niche (Paragraphs 6-8)
**Content**: Presents SVDT algorithm as solution with specific contributions

**Strengths**:
- Clear objectives: finding k representative nodes for similarity and difference
- Specific outcomes: algorithm with approximation guarantee
- Roadmap: outlines paper organization

**Excerpt**: "We present a greedy algorithm SVDT to find high-quality results with approximation guaranteed in an efficient way. Furthermore, we explore an extension of our comparative summarization to handle two trees with different structures. Extensive experiments demonstrate the effectiveness and efficiency of our SVDT algorithm against existing summarization competitors."

**Analysis**: Strong positioning with clear contribution claims. Notice the mention of approximation guarantee (theoretical rigor) and efficiency (practical importance).

**Excerpt**: "To summarize, this paper makes the following contributions:
- The problem we study is to choose a small set of elements to summarize two large-scale and hierarchically structured trees. We define the kVDT problem for finding representative nodes for similarity and difference summarization by considering the diverse representation across subtrees' weight distribution (Section III).
- We propose an efficient Hellinger distance-based distribution calculation to quantify the node distribution distance between two subtrees. Furthermore, we introduce a summary visualization technique that converts the output of our method into a concise and visually comprehensible tree summary (Section IV).
- We conduct extensive experiments on real-world datasets, including a case study and a usability study, to validate the feasibility and effectiveness of our algorithm against competitors (Section V)."

**Analysis**: Enumerated contributions provide clear roadmap. Notice the combination of theoretical (problem definition), methodological (Hellinger distance), and practical (visualization, experiments) contributions.

#### Key Linguistic Features
- **Nominalization**: "summarization," "visualization," "representation" - creates technical formality
- **Technical Terminology**: kVDT, SVDT, Hellinger distance - assumes expert audience
- **Mathematical Precision**: "k1 + k2 = k" - quantitative specificity

---

### Section 2: Related Work (Literature Review Structure)

#### Move 1: Thematic Overview (Paragraph 1)
**Content**: Broad overview of graph summarization field

**Strengths**:
- Establishes scope: "Graph summarization has been studied widely in the literature"
- Thematic grouping: compression methods, efficiency improvements, attributed graphs
- Temporal progression: references multiple works

**Excerpt**: "Graph summarization has been studied widely in the literature [4], [6], [8], [10], [11]. Navlakha et al. [8] proposed a graph compression method to generate graph summary with edge corrections. To enhance efficiency, Chu et al. [6] improved Navlakha's approach by identifying and merging pairs with high saving values."

**Analysis**: Clear positioning relative to existing work. Notice how authors group works thematically (compression, efficiency, attributed graphs) rather than chronologically.

#### Move 2: Critical Analysis (Paragraphs 2-3)
**Content**: Detailed evaluation of related approaches

**Strengths**:
- Thematic organization: compression, efficiency, attributed graphs, hierarchical data
- Critical evaluation: mentions limitations ("led to a graph recovery error rate")
- Comparative analysis: strengths/weaknesses of different approaches

**Excerpt**: "Wu et al. [10] considered topology and feature similarity for summarizing attributed graphs, but led to a graph recovery error rate. Kumar et al. [11] and Lee et al. [9] addressed this problem from different perspectives, the former focused on utility-driven to ensure the graph summary meet a user-specified utility threshold, while the latter achieved lossless summarization by representing unweighted graphs using positive and negative edges between hierarchical supernodes."

**Analysis**: Systematic coverage of related work with clear differentiation. Notice how authors acknowledge different "perspectives" - shows nuanced understanding of the field.

#### Move 3: Research Gaps (Final paragraph)
**Content**: Gaps emerge through critique and positioning

**Strengths**:
- Clear differentiation: "Different from most existing studies above that focus on a single graph, our study aims at differential summarization"
- Specific gap: comparative summarization on two trees
- Positioning: clearly distinguishes their contribution

**Excerpt**: "Different from most existing studies above that focus on a single graph, our study aims at differential summarization by finding k similar and different representatives on two trees."

**Analysis**: Strong positioning statement that clearly distinguishes the paper's contribution. Uses "Different from" to explicitly contrast with prior work.

---

### Section 3: Problem Statement (Technical Foundation)

#### Macro-Level Organization
**Content**: Formal problem definition with mathematical notation

**Strengths**:
- Clear definitions: trees, nodes, edges, weights
- Mathematical formalism: distance functions, representative scores
- Concrete examples: illustrates definitions with examples

**Excerpt**: "Preliminaries: Given a tree T = (V, E, freq), which contains V nodes and E edges, and freq is a non-negative integer function of the node weight. We introduce the node set S1 ⊆V representing similarity, and the node set S2 ⊆V representing difference. S1 ∩S2 = ∅, and their union S = S1 ∪S2 serves as the set of selected nodes for summarization."

**Analysis**: Strong mathematical foundation with clear set notation. Notice the explicit separation of similarity and difference sets.

**Excerpt**: "To balance the similarity and difference in summary views, we introduce the scaling coefficient γ."

**Excerpt**: "Deﬁnition 1 (Scaling Coefﬁcient): Given two weighted trees T1, T2, the scaling coefﬁcient represented by γ is obtained by calculating the average ratio of similarity and difference of all nodes satisfying x ∈V.
γ = (1/|V|) Σ[x∈V] min(freqT1(x), freqT2(x)) / |freqT1(x) − freqT2(x)|"

**Analysis**: Formal definition with mathematical notation. The scaling coefficient is a key innovation that balances similarity and difference.

**Excerpt**: "Representative score: For two nodes x, y satisfying y ∈ des(x), we deﬁne simRepx(y) and difRepx(y) to measure representative similarity and difference score of x on y in T1 and T2, respectively. Note that scaling coefﬁcient γ is only used in the difference measure formula to adjust the imbalance of the similarity and difference between nodes.
simRepx(y) = min (freqT1(y), freqT2(y)) · disx(y)
difRepx(y) = |freqT1(y) − freqT2(y)| · γ · disx(y)"

**Analysis**: Precise mathematical definitions for similarity and difference scores. Notice the use of the scaling coefficient only in the difference measure - shows careful design.

**Excerpt**: "The kVDT-problem statement: Given two trees T1, T2 with different weights and a positive integer k, the problem is to ﬁnd a k-sized representative set S ⊆V such that S = S1 ∪S2, where S1 consists of k1 similarity representatives and S2 consists of k2 difference representatives, ensuring that S reaches the maximum summary score with |S| = k."

**Analysis**: Clear problem statement with input (two trees, k) and output (representative set S). The constraint k1 + k2 = k is implicit in the definition.

---

### Section 4: SVDT Algorithm (Core Technical Contribution)

#### Macro-Level Organization
**Content**: Detailed algorithmic methodology presentation

**Strengths**:
- Clear subsections: Distribution Normalization, Property Analysis, Algorithm Description, Extension
- Technical detail with mathematical formalism
- Algorithm description with pseudo-code

**Excerpt**: "In this section, we first introduce a novel concept of normalized distribution score comparing similarity and difference. Based on it, we define our summary score function and prove its submodularity. Leveraging the submodular property, we develop a greedy algorithm SVDT and introduce the summary visual representation based on SVDT results. Finally, we discuss an extension of our techniques to handle differential summarization on two trees with different structures."

**Analysis**: Clear roadmap of the section. Notice the progression: definition → property analysis (submodularity) → algorithm → visualization → extension.

**Excerpt**: "In our problem formulation, we consider the distribution of nodes with their descendants. The key of comparing a representative node x in two trees T1, T2 is to measure the similarity and difference of their representative normalized distribution in x's subtree. Here, we use a parameter β ∈Z+ to be the number of representative similar and different weights, i.e., SimD(x) = [SimT1₁(x), SimT2₁(x), ..., SimT2β(x)], DifD(x) = [Dif T1₁(x), Dif T1₁(x), ..., Dif T2β(x)], respectively."

**Analysis**: Introduces the key concept of distribution normalization. The parameter β controls the granularity of representation.

**Excerpt**: "Computing distribution score Distri(·): After obtaining SimD(·) and DifD(·) for all non-leaf nodes, we proceed with the normalization to obtain SimD(·) and DifD(·) for all non-leaf nodes. After converting them to probability distributions, we apply the Hellinger distance [12] to calculate the distance between similarity distribution and difference distribution, i.e., Distri(·) as the distribution values of the non-leaf nodes."

**Analysis**: Describes the key innovation - using Hellinger distance to quantify distribution differences. This connects to the theoretical foundation mentioned in the introduction.

**Excerpt**: "Summary score: For two summary sets S1, S2 ⊆V , the similarity summary score of S1 and difference summary score of S2 on y ∈V are denoted as simSmyS1(y) and difSmyS2(y) as follows, representing the maximum similarity and difference impact on y among all representative elements in S1 and S2.
simSmyS1(y) = max[x∈S1∩anc(y)] simRepx(y) · (1 − Distri(x))
difSmyS2(y) = max[x∈S2∩anc(y)] difRepx(y) · Distri(x)"

**Analysis**: Defines the summary score function that combines similarity and difference scores. Notice how Distri(x) is used to weight the contributions.

**Excerpt**: "Submodularity: Given a similarity summary node x ∈S1, let the set of nodes that take x as their similarity summary node, denoted by θS1(x) = {y ∈dec(x) : simSmyS1(y) = simRepx(y) · (1 − Distri(x))}. Similarly, for a difference summary node x ∈S2, the set of nodes that take x as their difference summary node is defined as: θS2(x) = {y ∈dec(x) : difSmyS2(y) = difRepx(y) · Distri(x)}."

**Analysis**: Establishes the theoretical foundation - submodularity - which enables the greedy algorithm with approximation guarantees.

---

### Section 5: Experiments (Evaluation)

#### Macro-Level Organization
**Content**: Comprehensive experimental evaluation

**Strengths**:
- Clear subsections: Datasets, Methods Comparison, Evaluation Metrics, Quality Evaluation, Scalability, Case Study, Usability Study
- Multiple evaluation metrics: diversity, query closeness, average level difference
- Real-world case study and usability evaluation

**Excerpt**: "In this section, we conducted extensive experiments to evaluate the performance. The source code of our algorithm is available at https://github.com/csyqchen/TKDE_SVDT."

**Analysis**: Opens with transparency about code availability - good practice for reproducibility.

**Excerpt**: "Datasets: We used three pairs of real-world datasets containing hierarchical terminologies. Latt&Lnur are extracted from the Medical Entity Dictionary [1] with 4226 entities in a tree height of 22, which consists of information on patient and nurse access to online knowledge resources. The Anime hierarchical structure, extracted from the 'Anime' directory in Wikipedia, includes 15,135 animes and their frequency represented by the number of page views in Jan 2018 and Jan 2024 [15]. The Yago hierarchical structure is an extracted tree of ontology structure yagoTaxonomy with 493,839 taxonomies in multilingual Wikipedias, which are by randomly assigning two different weights denoted as Yago1 and Yago2."

**Analysis**: Describes datasets with specific details (sizes, sources). Notice the diversity: medical data, Wikipedia, ontology - shows broad applicability.

**Excerpt**: "Methods Comparison: To evaluate the quality of our method SVDT, we compare it with three baseline algorithms, including GVDO [5], FEQ [1], and CAGG [1]. GVDO is a summarization approach applied to ontology-based structure. FEQ is a method of selecting k nodes with the highest frequency as the summarized answer. CAGG selects k nodes with the highest frequency as the summarization answer by controlling descendant contribution."

**Analysis**: Clear description of baselines. Notice that these methods work on single trees, so variants are created for comparison - shows careful experimental design.

**Excerpt**: "Evaluation Metrics: To evaluate the quality of summarization answers, we use three metrics: the diversity Div(S), the query closeness CQ(S) [4], and average level difference Ald(S) [5]."

**Analysis**: Multiple metrics provide comprehensive evaluation. Each metric captures a different aspect: diversity (coverage), query closeness (proximity), level difference (hierarchical preservation).

**Excerpt**: "Exp-I: Quality Evaluation: Fig. 5 demonstrates that SVDT markedly surpasses three baseline methods in capturing diversity Div(S), thereby indicating its superiority in summarizing intrinsic tree relationships. Figs. 6 and 7 both illustrate that our algorithm, SVDT, maintains the closest distance and the smallest average level difference in almost all datasets compared to other baseline methods. This demonstrates that our summary is the most effective in closely mirroring the original tree structure of the dataset."

**Analysis**: Strong empirical validation with multiple metrics. Uses "markedly surpasses" and "most effective" to emphasize superiority.

**Excerpt**: "Exp-II: Scalability Test: We generated four synthetic datasets with tree node sizes from 10³ to 10⁶. In all experiments, we fixed k = 10 and β = 3 to compare the scalability of SVDT. The baseline in Fig. 8 is a summary approach that finds the optimal combination of S1 and S2. As the tree node size increases, SVDT exhibits remarkable scalability and efficiency, reflecting the effectiveness of Algorithm 2."

**Analysis**: Demonstrates scalability - important for practical applicability. Tests up to 1 million nodes shows the algorithm can handle large-scale data.

**Excerpt**: "Exp-III: Case Study on ACM CCS Topic Summarization: Fig. 10(a) illustrates publication counts of research papers in different five-year periods on a poly-hierarchical ontology (ACM Computing Classification System [14]). For k = 7, in Fig. 10(b), we show the summarization given by GVDO with the best experimental results among all baselines in quality evaluation. GVDO summarizes attractive topics but lacks priority or changes, providing limited information to users. In contrast, our SVDT summarization in Fig. 10(c) has red and blue themes, representing similarities and differences, respectively."

**Analysis**: Real-world case study demonstrates practical value. The comparison shows how SVDT captures both similarities and differences, while baselines only capture one aspect.

**Excerpt**: "Exp-IV: Usability Study on ACM CCS Topic Summarization: We conduct usability evaluation for top-k topic summarization, selecting k topics from Fig. 10(a) to capture commonalities and trends over different five-year periods. We set k = 7 and invite 10 users with the background in computer science and academic research to choose their top-7 topics for summarization. Then, we compare their selections with different methods (FEQ, GVDO, CAGG, and SVDT). As shown in Fig. 9, our method achieves an average matching accuracy of 85.7%, significantly outperforming the 60% accuracy by other methods. This result highlights the effectiveness of our algorithm in homogeneous and differential summarization."

**Analysis**: User study provides strong validation - 85.7% matching accuracy significantly outperforms baselines. This demonstrates real-world usefulness, not just algorithmic correctness.

---

### Section 6: Conclusion

#### Macro-Level Organization
**Content**: Synthesis and summary of contributions

**Strengths**:
- Clear contribution summary
- Restates key innovations
- Acknowledges future directions (extension to different structures)

**Excerpt**: "In this paper, we introduce the kVDT problem aimed at visually summarizing two weighted hierarchical trees of identical structure. The SVDT algorithm selects k representative nodes, summarizing the commonalities and diversities between two weighted trees. We propose a distribution normalization technique extending Hellinger distance for efficient non-leaf node computation. Our method includes a summary visual representation for the compact visualization. Extensive experiments demonstrate the superiority of our proposed algorithm."

**Analysis**: Concise summary that restates the problem, solution, key technical contributions, and validation. Notice the mention of visualization - connects back to the practical application.

---

## Cross-Disciplinary Comparison

### Computer Science (Data Engineering) vs. Traditional Academic Writing

| Aspect | Top-K Representative Search Paper | Traditional Academic |
|---|---|---|
| **Literature Review Location** | Separate section (Section II) after introduction | Integrated into introduction |
| **Technical Detail Level** | Very high (algorithms, mathematical definitions, pseudo-code) | Medium (methods overview) |
| **Evaluation Focus** | Quantitative metrics, scalability tests, usability studies | Theoretical validation, qualitative analysis |
| **Contribution Claims** | Algorithmic novelty + efficiency + visualization | Theoretical advancement + empirical evidence |
| **Mathematical Formalism** | Extensive (definitions, proofs of properties like submodularity) | Moderate (key formulas) |
| **Experimental Design** | Multiple metrics, case studies, user studies | Controlled experiments or theoretical proofs |

### Key Learning Points for Imitation

1. **Mathematical Precision**: Use of formal definitions, set notation, and mathematical properties (submodularity)
2. **Algorithmic Clarity**: Clear algorithm description with theoretical guarantees (approximation)
3. **Comprehensive Evaluation**: Multiple metrics, scalability tests, real-world case studies, and user studies
4. **Practical Applications**: Concrete examples (SIGMOD conference, disease ontology, university admissions)
5. **Theoretical-Practical Balance**: Strong theoretical foundation (submodularity) with practical efficiency (greedy algorithm)

---

## Imitation Opportunities for Future Papers

### Structural Elements to Adapt

- **Problem Formulation**: Clear separation of input (two trees), output (representative set), and constraints (k = k1 + k2)
- **Scaling Coefficient**: Novel concept (γ) for balancing competing objectives (similarity vs. difference)
- **Distribution Normalization**: Using probability distributions and distance metrics (Hellinger distance) for comparison
- **Submodularity Analysis**: Proving properties that enable efficient approximation algorithms
- **Multi-metric Evaluation**: Diversity, query closeness, and structural preservation metrics
- **User Studies**: Validating algorithmic results with human evaluation

### Rhetorical Strategies

- **Problem Novelty**: "Different from most existing studies above that focus on a single graph, our study aims at..."
- **Technical Positioning**: Clear differentiation from related work with specific limitations
- **Practical Relevance**: Multiple real-world applications (conferences, medical data, Wikipedia)
- **Contributions Enumeration**: Numbered list of contributions in introduction
- **Case Study Integration**: Detailed real-world example (ACM CCS) showing practical value

### Quality Indicators

- **Theoretical Rigor**: Formal definitions, property proofs (submodularity), approximation guarantees
- **Empirical Validation**: Multiple datasets, metrics, scalability tests, user studies
- **Code Availability**: Public GitHub repository for reproducibility
- **Visualization**: Summary visual representation for practical use
- **Extensibility**: Discussion of extension to different structures (trees with different topologies)

---

## Additional Excerpts for Reference

### Introduction Excerpts

**Excerpt on Applications**: "Beside the application of differential summarization on SIGMOD research topic, we illustrate two more typical applications as follows. First, consider a disease ontology [5], the hierarchical tree consists of disease categories (e.g. cancer, mental health disease, syndrome disease, cellular proliferation disease). In turn, the category of 'cancer' may have specific instances of 'lung cancer' and 'leukemia'. Given one hospital with different disease distributions on this disease ontology over a few years, the differential summarization reveals the common disease patterns and the change trends of disease occurrence."

**Excerpt on Challenges**: "In light of the above, the differential summary in Fig. 1(e) is a concise answer to well preserve the homogeneity and difference in T1 and T2. However, the problem of differential summarization has two challenges. First, it is hard to determine the number of homogeneous and differential nodes although the total number k is given. Second, it is not easy to design a unified summary score function to similarity and difference simultaneously by incorporating the weight distributions in subtrees."

### Problem Statement Excerpts

**Excerpt on Distance Function**: "To capture the representative effect of nodes and their descendants at different levels, we consider the distance denoted as disx(y) between them. disx(y) only exists when y ∈des(x). Otherwise, it is set to 0. The distance disx(y) can be calculated using the following formula.
disx(y) = 1/(level(y) − level(x) + 1), if y ∈des(x)
0, otherwise"

**Excerpt on Example**: "Example 1: Consider the tree T(V, E) in Fig. 1(a). For nodes p1 and r, the function level(·) is defined as level(x) = distT (x, r0), representing the level distance from the root r0 to the node x in tree T. Thus, level(p1) = 2 and level(r) = 0, and the distance disr(p1) = 1/3."

### Methods Excerpts

**Excerpt on Algorithm Overview**: "Based on the deﬁnition of simSmyS1(x) and difSmyS2(x), the summary score of the set S is defined as:
sum(S) = Σ[y∈V] simSmyS1(y) + Σ[y∈V] difSmyS2(y)"

**Excerpt on Distribution Computation**: "These two distributions can be efficiently computed from the non-leaf nodes at the bottom level, i.e., progressively passing up top-β similar and differential distributions from the bottom upwards until reaching the root."

### Experimental Excerpts

**Excerpt on Metrics Details**: "First, Div(S) computes the diversity of the original data set represented by the summary node in two trees T1, T2. The higher the diversity, the better the summary.
Div(S) = Σ[x∈S∩anc(y), y∈V] |freqT1(y) − freqT2(y)| · disx(y)"

**Excerpt on Case Study Details**: "For the four second-level topics (I1, I2, I3, I4) in the original graph, SVDT uses varying shades of red to indicate the popularity levels of these topics. Additionally, we show the diversity by highlighting the changes in some topics between the two five-year periods. Nodes (I5, I13, I14) are colored with different shades of blue, and their direct ancestor computing methodology is marked with the deepest shade of red. These show that the popularity of artificial intelligence, learning paradigms, and machine learning approaches has changed significantly in five years and is showing a trend of increasing popularity."
