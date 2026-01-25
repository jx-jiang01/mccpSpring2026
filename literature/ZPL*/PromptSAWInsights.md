# Prompt-SAW Paper Macro-Level Structure Analysis

**Paper Title**: Prompt-SAW: Leveraging Relation-Aware Graphs for Textual Prompt Compression  
**Authors**: Ali, Li, Yang, Cheng, Hu, Yu, Wang (2025)  
**Journal**: IJCAI 2025  
**Field**: Natural Language Processing / Large Language Models  
**Structure Type**: IMRaD (Introduction, Related Work, Preliminaries, Methods, Experiments, Conclusion)

---

## Overall Macro-Level Assessment

### Structural Framework
**IMRaD Adaptation**: Introduction → Related Work → Preliminaries (Problem Definition) → Method → Experiments → Conclusion
- **Total Length**: ~8-10 pages (conference paper format)
- **Citation Style**: IJCAI format
- **Disciplinary Conventions**: Heavy emphasis on graph-based methodologies, knowledge extraction, and LLM evaluation metrics
- **Rhetorical Style**: Problem-solution structure with strong emphasis on readability and grammatical coherence

### Hourglass Flow Analysis
**General → Specific → General** progression is well-executed:
- **Introduction**: Broad applications (LLMs, prompting techniques) → Specific technical problem (lengthy prompts, lack of grammatical coherence) → Contribution claims
- **Related Work**: Broad field overview → Specific gaps → Positioning of current work
- **Methods**: Technical specificity with graph-based formalism
- **Experiments**: Specific evaluation → General implications
- **Conclusion**: Specific findings → Broad impact

---

## Section-by-Section Macro Analysis

### Section 1: Introduction (CARS Model Application)

#### Move 1: Establishing Territory (Paragraphs 1-2)
**Content**: Claims centrality of LLMs and prompting techniques
**Strengths**:
- Uses evaluative language: "exceptional abilities," "crucial tool," "attracted considerable attention"
- Establishes broad significance across multiple applications
- Present tense: "have shown," "play a crucial role," "provide the provision"

**Excerpt**: "LLMs have attracted considerable attention for their superior performance across a wide range of applications. For this, instructions (aka. prompts) play a crucial role in extending the capabilities of LLMs for multiple different tasks."

**Excerpt**: "The prompts provide the provision to guide the model to elucidate desired model behavior without perturbing the model parameters. This is also highlighted in recent studies that show well-designed prompts and the integration of external knowledge are significant to enhance the effectiveness of LLMs'~\citep{PromptEngineeringSurvey}. Different LLMs-related techniques directly benefiting from prompts include but are not limited to: In-Context Learning~\citep{ICL}, Chain-of-Thought~\citep{CoT}, Retrieval Augmented Generation~\citep{RAG}, and Agents~\citep{Agent} \emph{etc.}"

**Analysis**: Strong centrality claims supported by practical applications. Notice the comprehensive list of techniques (ICL, CoT, RAG, Agents) that establishes the importance of prompting. The present tense usage creates a sense of ongoing relevance.

#### Move 2: Establishing Niche (Paragraphs 3-5)
**Content**: Identifies specific gaps in current prompt compression approaches
**Strengths**:
- Clear gap identification: "exceedingly lengthy prompts," "lack grammatical coherence," "neglect the syntactic and semantic structure"
- Specific technical challenge: "thousands of tokens," "compressed to: {\em ''won twoes forg01 theate women prize:ertMayer''}"
- Opposing viewpoint: contrasts existing token-level approaches with graph-based needs

**Excerpt**: "At the same time, the abilities of LLMs are significantly compromised/constrained by increasingly lengthy prompts, even comprising thousands of tokens. Lengthy prompts not only obscure requisite information but also increase computational costs and incur inference latency."

**Excerpt**: "Existing prompt compression approaches focus on compressing text at the token level, \emph{i.e.,} they verify whether compression is applicable to each individual token. For instance,~\cite{selectiveContext} proposed Selective-Context that uses a compact language model to evaluate context's lexical units, enabling compression by eliminating units with minimal information. Also, LLMLingua~\citep{llmlingua} and LongLLMLingua~\citep{longllmlingua} developed budget control mechanisms to compresses prompts based on their perplexity."

**Excerpt**: "While existing approaches could enhance the ability to deal with lengthy prompts for LLMs, they lack grammatical coherence, \emph{i.e.,} existing approaches neglect the syntactic and semantic structure of the compressed prompt. This is because contemporary prompt compression methods primarily focus on quantifying token-level information, neglecting the overall grammatical structure of the compressed prompt."

**Excerpt**: "Such ignorance not only increases the risk of semantic loss within the compressed prompt but also hampers its readability for human readers. An example in this regard is shown in Figure~\ref{fig:example1}, where the original prompt text: {''\em Two women have won the prize: Curie and Maria Goeppert-Mayer''} is compressed to: {\em ''won twoes forg01 theate women prize:ertMayer''} by LongLLMlingua~\citep{longllmlingua}."

**Analysis**: Gap is highly specific and researchable. Uses concrete example (compressed text) to illustrate the problem vividly. Notice the explicit critique: "lack grammatical coherence" and "neglect the syntactic and semantic structure" - these become key contributions of their work.

#### Move 3: Occupying Niche (Paragraphs 6-8)
**Content**: Presents Prompt-SAW as solution with specific contributions
**Strengths**:
- Clear objectives: "cut down unnecessary information," "retain the syntactic and semantics"
- Specific outcomes: "task-aware" and "task-agnostic" scenarios
- Novel approach: graph-based compression with knowledge extraction

**Excerpt**: "To fill in the gap, in this paper, we propose~\OurMODEL{}, \emph{i.e.,} \textsc{\underline{\textbf{Prompt}}} compres\underline{\textbf{S}}ion via Relation \underline{\textbf{AW}}are graphs, a novel method designed to cut down unnecessary information in the prompt text by using Knowledge Graph (KG) structures to exploit the small-scale information elements (Section \ref{sec:notation}) in the prompts, \emph{i.e.,} information units comprising entities and their underlying relations."

**Excerpt**: "\OurMODEL{} first extracts all entities and their relations in the prompt to formulate the graph. Later, (i) for task-aware prompts,~\OurMODEL{} looks for small-scale information elements in the graph to only retain task-specific information as a sub-graph, (ii) for task-agnostic prompts,~\OurMODEL{} measures similarity scores between successive information elements in the graph to remove the redundant elements to obtain required sub-graph."

**Excerpt**: "To retain the syntactic and semantics of the prompt structure, \OurMODEL{} finally reinstates the information contained in the sub-graph resulting in an optimized and compressed prompt."

**Excerpt**: "We conducted extensive experimental analysis of~\OurMODEL{} under both task-agnostic and task-aware settings against existing best-performing models as baselines. For evaluation, we used: (i) ~\OurDATA{}, \emph{i.e.,} an extended experimental setting proposed by us for~\textsc{GSM8K}~\citep{GSM8K}, (ii) \textsc{NaturalQuestions}~\citep{LostInMiddle}, and (iii) ShareGPT\footnote{\url{https://sharegpt.com/}}."

**Analysis**: Strong positioning with two-scenario approach (task-aware vs. task-agnostic) and clear technical differentiation. Notice the emphasis on "syntactic and semantics" which directly addresses the gap identified. The contribution is clear: graph-based compression with knowledge extraction.

#### Key Linguistic Features
- **Nominalization**: "compression," "readability," "coherence" - creates technical formality
- **Passive Voice**: "are significantly compromised," "is compressed to" - emphasizes processes over agents
- **Technical Terminology**: LLMs, KGs, embeddings, perplexity - assumes expert audience
- **Visual Examples**: Concrete before/after examples for clarity

---

### Section 2: Related Work (Literature Review Structure)

#### Move 1: Thematic Overview (Paragraphs 1-3)
**Content**: Broad overview of prompt compression field
**Strengths**:
- Establishes scope: "reduce the inference cost of LLMs"
- Categorical organization: "soft prompt compression" vs. "discrete prompt compression"
- Temporal progression: establishes evolution of the field

**Excerpt**: "Prompt compression techniques are used to reduce the inference cost of LLMs across a wide range of applications. Existing work can be categorized into soft prompt compression and discrete prompt compression."

**Excerpt**: "Soft prompts were introduced by~\citet{softPrompt}. A soft prompt integrates additional trainable parameters at the model's input stage. \citet{softpromptcompression} emphasized that soft prompt compression effectively retains crucial abstract information with a reduced parameter count."

**Analysis**: Clear categorical organization. Notice how they establish two main categories before diving into specific methods. This creates a structured framework for understanding the field.

#### Move 2: Critical Analysis (Paragraphs 4-5)
**Content**: Detailed evaluation of related approaches
**Strengths**:
- Thematic organization: soft vs. discrete compression
- Critical evaluation: "seeks to optimize," "neglecting the comprehensive graph structure"
- Gap identification: token-level focus vs. graph structure need

**Excerpt**: "Compared to soft prompt compression, discrete prompt compression seeks to optimize the effectiveness of prompts via token-level search strategies. \citet{Jung2023DiscretePC} employed policy networks to eliminate unnecessary tokens for prompt compression. \citet{selectiveContext} utilized self-information metrics to identify and remove superfluous information in prompts."

**Excerpt**: "Capitalizing on these advancements, \citet{llmlingua} and \citet{longllmlingua} \eat{have} formulated algorithms for dynamically adjusting compression rates across different prompt sections, giving precedence to tokens with higher perplexity\eat{due to their substantial influence}."

**Excerpt**: "Despite the significant advancements achieved by these studies, their primary focus lies on token-level compression, neglecting the comprehensive graph structure information inherent in the prompt. \eat{To the best of our knowledge, our study represents the first exploration of prompt compression using graph structure.}"

**Analysis**: Strong critical analysis with clear limitations identified. Uses "despite" to acknowledge contributions while emphasizing gaps. Notice the implicit gap statement: "neglecting the comprehensive graph structure" - this sets up their contribution.

#### Move 3: Knowledge Graphs for LLM (Subsection)
**Content**: Positions graph-based approaches in LLM context
**Strengths**:
- Establishes KG as valid approach: "organize information as structured units"
- Shows existing KG-LLM integration: "multiple different scenarios"
- Novelty claim: "first to make an attempt to leverage knowledge graph structure for prompt compression"

**Excerpt**: "\noindent{\bf Knowledge Graphs (KGs) for LLM.} KGs organize information as structured units, \emph{i.e.,} relational triplets (explained in Appendix~\ref{sec:BCKGD_KG}), that encapsulate a wide variety of entities/concepts along with underlying relations~\citep{KGSurvey}."

**Excerpt**: "\citet{KGLLMSurvey} illustrated multiple different scenarios for integration of KGs with LLM for knowledge and data-driven bi-directional reasoning."

**Excerpt**: "To the best of our knowledge, \OurMODEL{} is the first to make an attempt to leverage knowledge graph structure for prompt compression."

**Analysis**: Excellent positioning strategy. Establishes KGs as valid and useful in LLM context, then claims novelty for applying to prompt compression. The "to the best of our knowledge" phrase provides academic hedging while making strong claim.

---

### Section 3: Preliminaries (Problem Definition and Notations)

#### Macro-Level Organization
**Content**: Formal mathematical definitions and notation system
**Strengths**:
- Clear mathematical formalism
- Systematic notation: consistent use of symbols throughout
- Problem formulation: formal statement of compression objective

**Excerpt**: "We use $P$ and $C$ to represent the original and compressed prompt respectively. Likewise, we use $N$ and $\widetilde{N}$ to represent the length of the original and compressed prompt. We use $\eta=\widetilde{N}/N$ to represent the compression rate and $1/\eta$ as the compression ratio. $\eta^{*}$ is used to represent the target compression rate."

**Excerpt**: "The graph is represented by $\mathcal{G}=\{(e_i,r_i,e_i^{'})\subseteq\mathcal{E}\times\mathcal{R}\times\mathcal{E}\}$, where $e_i$, $r_i$ and $e_i^{'}$ represent the subject entity, relation and object entity in the graph respectively; $\mathcal{E} = \{e_1, e_2, \cdots, e_m\}$ and $\mathcal{R}=\{r_1,r_2, \cdots, r_n\}$ denote the set of entities and relations in $\mathcal{G}$."

**Excerpt**: "$g_i = (e_i,r_i,e_i^{'})$ is used to represent small-scale information elements in $\mathcal{G}$, equivalent to graph triplet."

**Excerpt**: "In this work, we aim to design and develop an effective prompt compression strategy that can cut down the prompt text by only preserving the requisite information content while at the same time maintaining the semantics and end performance of the prompt to the best possible extent."

**Excerpt**: "Formally, we aim to generate a compressed prompt $C = \{c_i\}_{i=1}^{\widetilde{N}}$ given the original prompt $P=(p^\mathrm{ins},p^\mathrm{info},p^\mathrm{que})$, where $p^\mathrm{ins} = \{p_{i}^\mathrm{ins}\}_{i=1}^{N^\mathrm{ins}}$, $p^\mathrm{info} = \{p_{i}^\mathrm{info}\}_{i=1}^{N^\mathrm{info}}$, and $p^\mathrm{que} = \{p_{i}^\mathrm{que}\}_{i=1}^{N^\mathrm{que}}$, denote the prompt instruction, information and question, respectively"

**Analysis**: Strong methodological section with clear mathematical foundation. Notice the decomposition of prompts into three components (instruction, information, question) which becomes important for their graph-based approach. The "small-scale information elements" terminology is key to their contribution.

---

### Section 4: Method (Core Technical Contribution)

#### Macro-Level Organization
**Content**: Technical methodology presentation with graph-based approach
**Strengths**:
- Clear problem statement: "graph structure to effectively represent the textual information"
- Modular architecture explanation: Graph Construction, Task-aware, Task-agnostic
- Mathematical formalism: similarity functions, ranking algorithms
- Algorithm presentation: Detailed pseudocode

**Excerpt**: "In contrast to the existing token-level compression methods, in \OurMODEL{} we use a graph structure to effectively represent the textual information in the prompt, which is helpful to analyze the key aspects of the prompt. Later, we can refine the information in the graph structure to come up with a compressed prompt in a way that: (i) The semantic consistency of the compressed prompt is preserved; (ii) The end performance and/or utility of the prompt is not distorted."

**Excerpt**: "\OurMODEL{} is motivated by the observation that the key information within the prompt text could be inferred as a set of entities and relations, which can also be organized into a graph structure, commonly known as a knowledge graph in literature."

**Excerpt**: "Formally, given a prompt text $P$, we claim it encompasses a set of entities $\mathcal{E}\eat{=\{e_1,e_2,\cdots\}}$, \emph{i.e.,} names of persons, locations, organizations, miscellaneous elements, etc.,~\citep{ali2020fine}. These entities serve as the key elements of the prompt structure."

**Excerpt**: "\OurMODEL{} re-organizes these key elements of the prompt (\emph{i.e.,} entities and their relations) in a graph structure, {represented by $\mathcal{G}= \{(e_i, r_i,e_i^{'})\subseteq\mathcal{E}\times\mathcal{R}\times\mathcal{E}\}$. We use $g_i=(e_i,r_i,e_i^{'})$ to represent the $i$-th information element of $\mathcal{G}$, \emph{i.e.,} a fact stating that $e_i$ has $r_i$-$th$ relation with $e_i^{'}$.}"

**Analysis**: Highly technical section with strong mathematical foundation. Notice the transformation from text to graph structure, which is the key innovation. The emphasis on preserving "semantic consistency" directly addresses their identified gap.

#### Subsection 4.1: Graph Construction
**Content**: Methodology for extracting graph from text
**Strengths**:
- Primary method: OpenIE toolkit
- Auxiliary method: LLM-based extraction
- Computational consideration: preference for small-scale LLMs

**Excerpt**: "For graph construction from the text data, we primarily rely traditional knowledge extraction approaches, \emph{i.e.,} OpenIE~\citep{OpenIE}, to construct a graph $G$, as follows $\mathcal{G} = {IE}({P})$"

**Excerpt**: "For the cases not addressed by the above equation, we use an in-context learning prompt as our auxiliary method that prompts the language model to construct the graph from the original prompt text as follows: $\mathcal{G} = {M}(P_{\text{template}}(\text{P}))$"

**Excerpt**: "Note, for Equation~\ref{eq:graphConstruct}, we typically prefer a small-scale open-source LLM in order to avoid higher computational costs incurred by large models."

**Analysis**: Practical implementation details with computational considerations. Shows awareness of cost-benefit tradeoffs.

#### Subsection 4.2: Task-aware Prompts
**Content**: Similarity-based subgraph extraction for task-aware scenarios
**Strengths**:
- Question-answer alignment: embeds questions and computes similarity
- Ranking mechanism: selects high-similarity information elements
- Compression ratio control: meets target compression rate

**Excerpt**: "Task-aware scenarios refer to the settings when the information within the prompt is helpful and/or is related to the end-task, \emph{e.g.,} question answering. For such cases,~\OurMODEL{} aims to retain only the task-specific information in $\mathcal{G}$, while filtering out the redundant/useless information."

**Excerpt**: "For this, it first uses an encoder function to get the embeddings for the prompt question, as follows. $Emb_{p^{\mathrm{que}}} = E(p^{\mathrm{que}})$ where $Emb_{p^{\mathrm{que}}}$ is the embedding for prompt question $(p^{\mathrm{que}})$, and $E$ is the encoder network."

**Excerpt**: "Then, it computes the pair-wise similarity between the $Emb_{p^{\mathrm{que}}}$ and information elements in $\mathcal{G}$, as shown below. $Sim_{\mathcal{G}} = \{E(g_i)\cdot Emb_{p^{\mathrm{que}}} \; | \forall \; g_i \in \mathcal{G} \}$"

**Excerpt**: "Later, it ranks the scores in $Sim_{\mathcal{G}}$ in order to retain only the elements in $\mathcal{G}$ showing a higher degree of similarity with $p^{\mathrm{que}}$, as shown below. $Index_{\text{ranked}} = \text{Rank}(Sim_{\mathcal{G}})$"

**Excerpt**: "Finally, we restore/reconstruct the information elements in $\mathcal{G}_{\text{subset}}$ to come up with our compressed prompt $C$, as shown below. $C=e_1\oplus r_1 \oplus e_1^\prime ; \cdots ; e_n\oplus r_n \oplus e_n^\prime$ where $\oplus$ is the concatenation operator used to combine the entities and relations within the information elements $(g_i)$ {in the extracted subgraph $\mathcal{G}_{\text{subset}}$}, and $({;})$ is the delimiter used to separate different information elements in $\mathcal{G}_{\text{subset}}$."

**Analysis**: Clear algorithmic approach with mathematical precision. Notice the restoration step which ensures grammatical coherence - this directly addresses their main contribution claim.

#### Subsection 4.3: Task-agnostic Prompts
**Content**: Similarity-based redundancy removal for task-agnostic scenarios
**Strengths**:
- Redundancy detection: identifies similar information elements
- Threshold-based selection: binary search for optimal threshold
- Sequential processing: maintains order while removing redundancy

**Excerpt**: "A task-agnostic scenario implies that it is almost impossible to filter useful and/or task-specific information within the original prompt text $(P)$. {In such cases,~\OurMODEL{} looks for recurring information elements in $P$ for probable prompt compression.}"

**Excerpt**: "We assume two main sources of recurring elements in $P$, \emph{i.e.,} (i) the verbose expression of the prompt itself and (ii) the repeated element generated by auxiliary models. Note that these assumptions are based on empirical observation illustrating that large models' re-reading phenomenon leads to the repeated generation of the extracted knowledge \citep{Yan2023UnderstandingIL}."

**Excerpt**: "For compression over task-agnostic scenarios, we sequentially traverse the information elements in $\mathcal{G}$ and select only the elements exhibiting a lower similarity with priorly selected information elements. Our underlying intuition is that highly similar information elements will carry repeated information. Thus, we could avoid redundant information in $P$ by selecting only dissimilar elements."

**Excerpt**: "For this, we use a threshold $\delta$ as a selection criteria for~\OurMODEL{}. The value of the $\delta$ is determined using a binary search algorithm (shown in Algorithm~\ref{alg:alg2}) that computes an appropriate value of threshold $\delta$ required to meet the targeted compression rate $\eta^{*}$."

**Analysis**: Sophisticated approach with theoretical justification. Notice the binary search mechanism for threshold selection - this shows algorithmic sophistication. The assumption about "re-reading phenomenon" provides theoretical grounding.

---

### Section 5: Experiments (Evaluation)

#### Macro-Level Organization
**Content**: Comprehensive quantitative and qualitative evaluation
**Strengths**:
- Clear evaluation metrics: EM, Span Accuracy, Rouge, Fluency
- Multiple baselines: Selective-Context, LLMLingua, LongLLMLingua, GPT4
- Multiple datasets: GSM8K-aug, NaturalQuestions, ShareGPT
- Multiple target LLMs: GPT3.5-turbo, LLaMA2-7B-chat

**Excerpt**: "To comprehensively evaluate the effectiveness of compressed prompts, we evaluate their performance under both task-agnostic and task-aware data settings. For task-agnostic data sets, we consider~\OurDATA{}, \emph{i.e.,} an extended variant of the original \textsc{GSM8K}~\citep{GSM8K} devised by us to report the model performance under $i$-shot settings with $i\in \{1,2,4,8\}$."

**Excerpt**: "We compare the performance of~\OurMODEL{} against following models as baselines: (i) Selective-Context~\citep{selectiveContext}, (ii) LLMLingua~\citep{llmlingua}, (iii) LongLLMlingua~\citep{longllmlingua}, and (iv) GPT4~\citep{GPT4}."

**Excerpt**: "Similar to \citet{GSM8K} and \citet{llmlingua}, we use Exact Match (EM) as the evaluation metric for~\OurDATA{}. For NaturalQuestions, we used Span Accuracy (Span-Acc) as a metric, similar to~\citet{LostInMiddle} and \citet{longllmlingua}. For ShareGPT, we used Rouge as the evaluation metric~\citep{rouge_2004}. Apart from these, we also use fluency (FL)~\citep{Fluency} to measure the readability and grammatical coherence of the compressed prompt."

**Excerpt**: "To demonstrate the generalization of our algorithm on different LLMs, we use {GPT3.5-turbo} and LLaMA2-7B-chat as our target LLMs."

**Analysis**: Strong experimental design with multiple dimensions of evaluation. Notice the addition of "fluency" metric which directly measures their key contribution (readability/grammatical coherence).

#### Results for Task-agnostic Settings
**Content**: Performance on GSM8K-aug across different shot settings
**Strengths**:
- Comprehensive evaluation: 1-shot, 2-shot, 4-shot, 8-shot
- Significant improvements: up to 10.1% improvement
- Compression rates: 32.3% to 34.9% reduction

**Excerpt**: "For task-agnostic settings, we report the results of~\OurMODEL{} for~\OurDATA{} in Table~\ref{tab:exp1}. Note, unlike existing research that reports their performance for one fixed setting, we report these results for $i$-shot settings, where $i$ indicates the number of prompts have been employed by \OurMODEL{}, \emph{i.e.,} \{1, 2, 4 and 8\}-shots."

**Excerpt**: "Comparing these results against the baseline models, we can observe that~\OurMODEL{} outperforms the previous state-of-the-art by a significant margin. For instance, compared to the best performing baselines, \OurMODEL{} improves the {EM} score by up to 7.3\%, 10.1\%, 5.5\% and 4.2\% under 1-shot, 2-shot, 4-shot and 8-shot settings, respectively. {Correspondingly reduction in the prompt size is 32.3\%, 34.9\%, 33.0\% and 32.9\%}."

**Excerpt**: "We attribute such drastic performance improvement to the following factors: (1)~\OurMODEL{} retains the logical integrity of the prompts by sub-dividing the original prompts into smaller comprehensive information elements; (2)\OurMODEL{} benefits from the workflow that allows selecting and omitting individual information elements for prompt compression without destroying the overall information structure of the compressed prompt. These help~\OurMODEL{} to ensure the utility of the compressed prompt for the end task."

**Analysis**: Strong empirical results with clear attribution of success factors. Notice the explanation directly connects to their methodology (information elements, logical integrity).

#### Results for Task-aware Settings
**Content**: Performance on NaturalQuestions and ShareGPT
**Strengths**:
- Dramatic improvements: up to 77.1% improvement
- Multiple compression rates: 0.5, 0.3, 0.1
- Different target LLMs: shows generalization

**Excerpt**: "Table~\ref{tab:exp2} reports the performance of~\OurMODEL{} under task-aware settings on NaturalQuestions using GPT3.5-turbo and LLaMA2-7B-chat as target LLMs. These results show that, \OurMODEL{} improves the Span Accuracy by 39.0\%, 40.8\% and 14.7\% for GPT3.5-turbo, and 77.1\%, 71.2\%, 72.7\% for LLaMA2-7B-chat, respectively, for different values of the target compression rates $\eta^{*} = \{0.5, 0.3, 0.1\}$, against the best-performing baseline (LongLLMLingua)."

**Excerpt**: "Correspondingly, the reduction in the prompt size is 56.7\%, 74.0\%, and 93.7\%\ respectively."

**Excerpt**: "The results of~\OurMODEL{} on ShareGPT (in Table~\ref{tab:exp_sharegpt}) show for GPT3.5-turbo as target LLM, \OurMODEL{} improves the Rouge-1 score by up to 29.3\%, 34.9\% and 38.6\%. The performance for Rouge-2 and Rouge-L exhibit a similar behavior."

**Analysis**: Impressive results, especially for task-aware settings. Notice the very high compression rates (up to 93.7%) while maintaining performance - this is a strong selling point.

#### Readability of Compressed Prompts
**Content**: Qualitative and quantitative evaluation of readability
**Strengths**:
- Concrete examples: before/after comparison
- Quantitative metric: fluency scores
- Human-centered evaluation: readability focus

**Excerpt**: "As explained in the introduction (also highlighted in Figure~\ref{fig:example1}), a key limitation of existing prompt compression approaches is the limited readability of the compressed prompt. In order to validate the results of~\OurMODEL{} in terms of human readability and/or interpretability, we report some example prompts along with prompt compressed using~\OurMODEL{} and LLMLingua~\citep{llmlingua} in Appendix~\ref{Appendix:exp-readability}, for a quick comparison."

**Excerpt**: "For instance, as shown in Example~\ref{Appendix:ex1} (Appendix~\ref{Appendix:exp-readability}), the prompt compressed by LLMLingua encompasses grammatical incoherent text, such as: \{\emph{``List of Nobelates in The first Prize1 Wilhelmrad, of who received82 in en prize''}\}. Lack of grammatical coherence significantly undermines the readability and/or interpretability of the compressed prompt, thus impacting its end-utility."

**Excerpt**: "Whereas, the prompt compressed by~\OurMODEL{}, relying on knowledge graph triples exhibits a consistent grammatical sentence structure, as shown in the lower half of Example~\ref{Appendix:ex1}."

**Excerpt**: "To further support our claims, we also conducted a quantitative comparison. Specifically, we assess the fluency of the compressed prompts through the computation of a weighted mean of bi-gram and tri-gram entropies~\citep{Fluency}. Its computational details are given in Appendix~\ref{Appendix:Eval}, and result is reported in Table~\ref{tab:exp4}. These results show that~\OurMODEL{} yields relatively higher fluency scores than the baseline models. A lower score for baseline models, \emph{e.g.,} LLMLingua, is attributable to loss of intrinsic semantic relationship between the tokens for the compressed prompt."

**Analysis**: Excellent evaluation that directly addresses their main contribution claim (readability/grammatical coherence). The combination of qualitative examples and quantitative metrics provides strong evidence.

---

### Section 6: Conclusion

#### Macro-Level Organization
**Content**: Synthesis and contribution summary
**Strengths**:
- Clear contribution summary
- Key benefits highlighted
- Concise presentation

**Excerpt**: "In this work, we proposed~\OurMODEL{} that leverages graph structures to infer key information in the prompt in order to come up with a compressed prompt. Experimental evaluation showed that~\OurMODEL{} outperforms the existing research on by a significant margin."

**Excerpt**: "Moreover,~\OurMODEL{} addressed a key limitation of existing prompt compression approaches, \emph{i.e.,} the compressed prompts are easy to read and understand for end-readers."

**Analysis**: Concise conclusion that reinforces main contributions. Notice the emphasis on readability which is their unique contribution.

---

## Cross-Disciplinary Comparison

### Computer Science vs. Traditional Academic Writing

| Aspect | Prompt-SAW Paper | Traditional Academic |
|---|---|---|
| **Literature Review Location** | Separate section after introduction | Integrated into introduction |
| **Technical Detail Level** | Very High (graph algorithms, embeddings, similarity functions) | Medium (methods overview) |
| **Evaluation Focus** | Quantitative metrics, readability assessment, fluency scores | Theoretical validation, qualitative analysis |
| **Contribution Claims** | Technical novelty + benchmark contribution (GSM8K-aug) | Theoretical advancement + empirical evidence |
| **Mathematical Formalism** | Extensive use of equations and graph notation | Moderate mathematical notation |

### Key Learning Points for Imitation

1. **Graph-Based Representation**: Use of knowledge graphs for structured information extraction
2. **Readability Focus**: Emphasis on human-centered evaluation metrics
3. **Benchmark Contribution**: Creation of extended dataset (GSM8K-aug) for evaluation
4. **Two-Scenario Approach**: Task-aware vs. task-agnostic as organizational framework
5. **Qualitative + Quantitative**: Combination of examples and metrics for comprehensive evaluation

---

## Imitation Opportunities for Future Papers

### Structural Elements to Adapt
- **Graph-Based Methodology**: Transformation from text to graph structure
- **Scenario-Based Organization**: Different approaches for different scenarios (task-aware vs. task-agnostic)
- **Benchmark Creation**: Extended datasets for comprehensive evaluation
- **Readability Evaluation**: Human-centered metrics alongside performance metrics

### Rhetorical Strategies
- **Concrete Examples**: Before/after comparisons to illustrate problems and solutions
- **Gap Emphasis**: Explicit identification of specific limitations (grammatical coherence)
- **Novelty Claims**: "First to leverage knowledge graph structure" type statements
- **Practical Impact**: Emphasis on real-world benefits (readability, computational cost)

### Quality Indicators
- **Mathematical Rigor**: Formal definitions with graph notation
- **Empirical Validation**: Multiple evaluation dimensions (performance, compression, readability)
- **Benchmark Contributions**: New datasets or extended versions for evaluation
- **Algorithmic Sophistication**: Binary search, similarity-based ranking, threshold optimization
