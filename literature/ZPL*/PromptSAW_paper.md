# Prompt-SAW: Leveraging Relation-Aware Graphs for Textual Prompt Compression

**Authors**: Muhammad Asif Ali, Zhengping Li, Shu Yang, Keyuan Cheng, Lijie Hu, Lu Yu, Di Wang  
**Venue**: IJCAI 2025  
**Field**: Natural Language Processing / Large Language Models

## Abstract

Large Language Models (LLMs) have shown exceptional abilities for multiple different natural language processing tasks. While prompting is a crucial tool for LLM inference, we observe that there is a significant cost associated with exceedingly lengthy prompts. Existing attempts to compress lengthy prompts lead to sub-standard results in terms of readability/interpretability of the compressed prompt, with a detrimental impact on prompt utility. 

To address this, we propose Prompt-SAW: Prompt compression via Relation-Aware graphs, an effective strategy for prompt compression over task-agnostic and task-aware prompts. Prompt-SAW uses the prompt's textual information to build a graph, later extracts key information elements in the graph to come up with the compressed prompt. We also propose GSM8K-aug, i.e., an extended version of the existing GSM8K benchmark for task-agnostic prompts in order to provide a comprehensive evaluation platform. 

Experimental evaluation using benchmark datasets shows that prompts compressed by Prompt-SAW are not only better in terms of readability, but they also outperform the best-performing baseline models by up to 10.1% and 77.1% respectively for task-agnostic and task-aware settings while compressing the original prompt text by 34.9% and 56.7%.

## 1. Introduction

LLMs have attracted considerable attention for their superior performance across a wide range of applications. For this, instructions (aka. prompts) play a crucial role in extending the capabilities of LLMs for multiple different tasks. The prompts provide the provision to guide the model to elucidate desired model behavior without perturbing the model parameters. Different LLMs-related techniques directly benefiting from prompts include but are not limited to: In-Context Learning, Chain-of-Thought, Retrieval Augmented Generation, and Agents.

At the same time, the abilities of LLMs are significantly compromised/constrained by increasingly lengthy prompts, even comprising thousands of tokens. Lengthy prompts not only obscure requisite information but also increase computational costs and incur inference latency. To tackle this challenge, prompt compression techniques, e.g., Selective-Context, have garnered significant interest. These approaches are based on the fact that natural language is inherently redundant. Thus, it is possible to substantially compress the length of original textual prompts by preserving requisite information in small segments.

Existing prompt compression approaches focus on compressing text at the token level, i.e., they verify whether compression is applicable to each individual token. For instance, Selective-Context proposed that uses a compact language model to evaluate context's lexical units, enabling compression by eliminating units with minimal information. Also, LLMLingua and LongLLMLingua developed budget control mechanisms to compresses prompts based on their perplexity.

While existing approaches could enhance the ability to deal with lengthy prompts for LLMs, they lack grammatical coherence, i.e., existing approaches neglect the syntactic and semantic structure of the compressed prompt. This is because contemporary prompt compression methods primarily focus on quantifying token-level information, neglecting the overall grammatical structure of the compressed prompt. Such ignorance not only increases the risk of semantic loss within the compressed prompt but also hampers its readability for human readers. An example in this regard shows the original prompt text: "Two women have won the prize: Curie and Maria Goeppert-Mayer" is compressed to: "won twoes forg01 theate women prize:ertMayer" by LongLLMlingua.

To fill in the gap, in this paper, we propose Prompt-SAW, i.e., Prompt compresSion via Relation-Aware graphs, a novel method designed to cut down unnecessary information in the prompt text by using Knowledge Graph (KG) structures to exploit the small-scale information elements in the prompts, i.e., information units comprising entities and their underlying relations.

Prompt-SAW first extracts all entities and their relations in the prompt to formulate the graph. Later, (i) for task-aware prompts, Prompt-SAW looks for small-scale information elements in the graph to only retain task-specific information as a sub-graph, (ii) for task-agnostic prompts, Prompt-SAW measures similarity scores between successive information elements in the graph to remove the redundant elements to obtain required sub-graph. To retain the syntactic and semantics of the prompt structure, Prompt-SAW finally reinstates the information contained in the sub-graph resulting in an optimized and compressed prompt.

We conducted extensive experimental analysis of Prompt-SAW under both task-agnostic and task-aware settings against existing best-performing models as baselines. For evaluation, we used: (i) GSM8K-aug, i.e., an extended experimental setting proposed by us for GSM8K, (ii) NaturalQuestions, and (iii) ShareGPT. Experimental results show that Prompt-SAW significantly outperforms other baseline models.

## 2. Related Work

### Prompt Compression

Prompt compression techniques are used to reduce the inference cost of LLMs across a wide range of applications. Existing work can be categorized into soft prompt compression and discrete prompt compression.

Soft prompts were introduced to integrate additional trainable parameters at the model's input stage. Soft prompt compression effectively retains crucial abstract information with a reduced parameter count. Carefully crafted prompts are helpful in augmenting the end-performance of compressed LLMs.

Compared to soft prompt compression, discrete prompt compression seeks to optimize the effectiveness of prompts via token-level search strategies. Policy networks have been employed to eliminate unnecessary tokens for prompt compression. Self-information metrics have been utilized to identify and remove superfluous information in prompts. Algorithms have been formulated for dynamically adjusting compression rates across different prompt sections, giving precedence to tokens with higher perplexity.

Despite the significant advancements achieved by these studies, their primary focus lies on token-level compression, neglecting the comprehensive graph structure information inherent in the prompt.

### Knowledge Graphs (KGs) for LLM

KGs organize information as structured units, i.e., relational triplets, that encapsulate a wide variety of entities/concepts along with underlying relations. Multiple different scenarios for integration of KGs with LLM for knowledge and data-driven bi-directional reasoning have been illustrated. LLMs have been combined with KGs for interpretable reasoning over KG Question Answering tasks. Innovative frameworks have been introduced that leverage LLM's reasoning capabilities for executing KG-based tasks. To the best of our knowledge, Prompt-SAW is the first to make an attempt to leverage knowledge graph structure for prompt compression.

## 3. Problem Definition

[Formal problem definition and notation would be included here]

## 4. Method

In contrast to the existing token-level compression methods, in Prompt-SAW we use a graph structure to effectively represent the textual information in the prompt, which is helpful to analyze the key aspects of the prompt. Later, we can refine the information in the graph structure to come up with a compressed prompt in a way that: (i) The semantic consistency of the compressed prompt is preserved; (ii) The end performance and/or utility of the prompt is not distorted.

### Motivation of Prompt-SAW

Prompt-SAW is motivated by the observation that the key information within the prompt text could be inferred as a set of entities and relations, which can also be organized into a graph structure, commonly known as a knowledge graph in literature.

Formally, given a prompt text P, we claim it encompasses a set of entities, i.e., names of persons, locations, organizations, miscellaneous elements, etc. These entities serve as the key elements of the prompt structure. In addition to the entities, we can also infer some relations R in P that may be used to describe the connections between the entities. Prompt-SAW re-organizes these key elements of the prompt (i.e., entities and their relations) in a graph structure, represented by G={(eᵢ, rᵢ, e'ᵢ)⊆E×R×E}. We use gᵢ=(eᵢ, rᵢ, e'ᵢ) to represent the i-th information element of G, i.e., a fact stating that eᵢ has rᵢ-th relation with e'ᵢ.

We argue this transformation of text information to graph is a more reasonable and natural approach as: (i) It helps in highlighting the key information elements in the prompt. (ii) Later, analyzing these key entities in combination with underlying relations helps in filtering/digging out the salient content within the prompt to come up with a compressed prompt.

### Workflow of Prompt-SAW

The workflow of Prompt-SAW consists of two parts. First, it uses the information in prompt P to construct a graph G. Then, based on the specific scenario, we proceed as follows:

**(a) Task-aware scenario.** For this scenario, we traverse the graph (G) in a way to preserve only the information elements that are relevant to the task as task-specific subgraphs, indicative of information useful for the compressed prompt.

**(b) Task-agnostic scenario.** For this scenario, we no longer have access to task-specific information. Thus, we use similarity scores between the information elements in G to identify and remove the redundant elements to obtain subgraphs that are helpful for compression.

#### Graph Construction

For graph construction from the text data, we primarily rely traditional knowledge extraction approaches, i.e., OpenIE, to construct a graph G. For the cases not addressed by the above equation, we use an in-context learning prompt as our auxiliary method that prompts the language model to construct the graph from the original prompt text.

#### Task-aware Prompts

Task-aware scenarios refer to the settings when the information within the prompt is helpful and/or is related to the end-task, e.g., question answering. For such cases, Prompt-SAW aims to retain only the task-specific information in G, while filtering out the redundant/useless information.

For this, it first uses an encoder function to get the embeddings for the prompt question. Then, it computes the pair-wise similarity between the question embeddings and information elements in G. Later, it ranks the scores in order to retain only the elements in G showing a higher degree of similarity with the question. We then use the information in the ranked list to iterate over G to extract the sub-graph G_subset not surpassing the targeted compression ratio η*. Finally, we restore/reconstruct the information elements in G_subset to come up with our compressed prompt C.

#### Task-agnostic Prompts

A task-agnostic scenario implies that it is almost impossible to filter useful and/or task-specific information within the original prompt text P. In such cases, Prompt-SAW looks for recurring information elements in P for probable prompt compression. We assume two main sources of recurring elements in P, i.e., (i) the verbose expression of the prompt itself and (ii) the repeated element generated by auxiliary models.

For compression over task-agnostic scenarios, we sequentially traverse the information elements in G and select only the elements exhibiting a lower similarity with priorly selected information elements. Our underlying intuition is that highly similar information elements will carry repeated information. Thus, we could avoid redundant information in P by selecting only dissimilar elements.

For this, we use a threshold δ as a selection criteria for Prompt-SAW. The value of the δ is determined using a binary search algorithm that computes an appropriate value of threshold δ required to meet the targeted compression rate η*.

## 5. Experiments

### Experimental Setup

To comprehensively evaluate the effectiveness of compressed prompts, we evaluate their performance under both task-agnostic and task-aware data settings. For task-agnostic data sets, we consider GSM8K-aug, i.e., an extended variant of the original GSM8K devised by us to report the model performance under i-shot settings with i∈{1,2,4,8}. For the task-aware dataset, we use NaturalQuestions, and ShareGPT.

We compare the performance of Prompt-SAW against following models as baselines: (i) Selective-Context, (ii) LLMLingua, (iii) LongLLMlingua, and (iv) GPT4.

Similar to prior work, we use Exact Match (EM) as the evaluation metric for GSM8K-aug. For NaturalQuestions, we used Span Accuracy (Span-Acc) as a metric. For ShareGPT, we used Rouge as the evaluation metric. Apart from these, we also use fluency (FL) to measure the readability and grammatical coherence of the compressed prompt.

To demonstrate the generalization of our algorithm on different LLMs, we use GPT3.5-turbo and LLaMA2-7B-chat as our target LLMs.

### Experimental Results

#### Results for Task-agnostic Settings

For task-agnostic settings, we report the results of Prompt-SAW for GSM8K-aug. Unlike existing research that reports their performance for one fixed setting, we report these results for i-shot settings, where i indicates the number of prompts have been employed by Prompt-SAW, i.e., {1, 2, 4 and 8}-shots.

Comparing these results against the baseline models, we can observe that Prompt-SAW outperforms the previous state-of-the-art by a significant margin. For instance, compared to the best performing baselines, Prompt-SAW improves the EM score by up to 7.3%, 10.1%, 5.5% and 4.2% under 1-shot, 2-shot, 4-shot and 8-shot settings, respectively. Correspondingly reduction in the prompt size is 32.3%, 34.9%, 33.0% and 32.9%.

We attribute such drastic performance improvement to the following factors: (1) Prompt-SAW retains the logical integrity of the prompts by sub-dividing the original prompts into smaller comprehensive information elements; (2) Prompt-SAW benefits from the workflow that allows selecting and omitting individual information elements for prompt compression without destroying the overall information structure of the compressed prompt. These help Prompt-SAW to ensure the utility of the compressed prompt for the end task.

#### Results for Task-aware Settings

The performance of Prompt-SAW under task-aware settings on NaturalQuestions using GPT3.5-turbo and LLaMA2-7B-chat as target LLMs shows that Prompt-SAW improves the Span Accuracy by 39.0%, 40.8% and 14.7% for GPT3.5-turbo, and 77.1%, 71.2%, 72.7% for LLaMA2-7B-chat, respectively, for different values of the target compression rates η*={0.5, 0.3, 0.1}, against the best-performing baseline (LongLLMLingua). Correspondingly, the reduction in the prompt size is 56.7%, 74.0%, and 93.7% respectively.

The results of Prompt-SAW on ShareGPT show for GPT3.5-turbo as target LLM, Prompt-SAW improves the Rouge-1 score by up to 29.3%, 34.9% and 38.6%. The performance for Rouge-2 and Rouge-L exhibit a similar behavior.

#### Readability of Compressed Prompts

As explained in the introduction, a key limitation of existing prompt compression approaches is the limited readability of the compressed prompt. In order to validate the results of Prompt-SAW in terms of human readability and/or interpretability, we report some example prompts along with prompt compressed using Prompt-SAW and LLMLingua for a quick comparison. These examples clearly indicate that the prompt compressed by Prompt-SAW exhibit better readability and/or interpretability compared to compressed using LLMLingua.

For instance, the prompt compressed by LLMLingua encompasses grammatical incoherent text, such as: "List of Nobelates in The first Prize1 Wilhelmrad, of who received82 in en prize". Lack of grammatical coherence significantly undermines the readability and/or interpretability of the compressed prompt, thus impacting its end-utility. Whereas, the prompt compressed by Prompt-SAW, relying on knowledge graph triples exhibits a consistent grammatical sentence structure.

To further support our claims, we also conducted a quantitative comparison. Specifically, we assess the fluency of the compressed prompts through the computation of a weighted mean of bi-gram and tri-gram entropies. These results show that Prompt-SAW yields relatively higher fluency scores than the baseline models. A lower score for baseline models, e.g., LLMLingua, is attributable to loss of intrinsic semantic relationship between the tokens for the compressed prompt.

## 6. Conclusion

[Conclusion section would summarize key contributions and future directions]
