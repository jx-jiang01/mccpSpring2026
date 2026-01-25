# FedSum: Data-Efficient Federated Learning Under Data Scarcity Scenario For Text Summarization

**Authors**: Zhiyong Ma, Zhengping Li, Yuanjie Shi, Jian Chen  
**Venue**: AAAI 2025  
**Field**: Federated Learning / Natural Language Processing

## Abstract

Text summarization task extracts salient information from a large amount of text for productivity enhancement. However, most existing methods heavily rely on training models from ample and centrally stored data which is infeasible to collect in practice, due to privacy concerns and data scarcity nature under several settings (e.g., edge computing or cold starting).

The main challenge lies in constructing the privacy-preserving and well-behaved summarization model under the data scarcity scenario, where the data scarcity nature will lead to the knowledge shortage of the model while magnifying the impact of data bias, causing performance degeneration.

In this work, we propose FedSum which extends the standard FL framework from depth and breadth to further extract prime and diversified knowledge from limited resources for text summarization. For depth extension, we introduce a Data Partition method to cooperatively recognize the prime samples that are more significant and unbiased, and the Data skip mechanism is introduced to help the model further focus on those prime samples during the local training process. For breadth extension, FedSum extends the source of knowledge and develops the summarization model by extracting knowledge from the data samples, hidden spaces, and globally received parameters.

## 1. Introduction

The amount of text data has grown explosively in various domains, such as journalism, medicine, and entertainment. For productivity enhancement, the summarization model, namely summarizer, compresses textual content into shorter versions while retaining key concepts from input content.

To construct a summarizer, most existing literature focused on the centralized manner with ample data. However, the data from individuals or institutions are generally private and sensitive, prohibiting access from the public. This makes the collection of text data in a central location infeasible.

Federated Learning (FL) provides a paradigm to utilize information and construct a shared model securely. Nevertheless, when the FL system is plagued by data scarcity (e.g., under edge computing or cold starting settings, where each FL client trains a common and basic summarization model with over 10M parameters with less than 500 samples), it is intractable for the summarizer to get adequate knowledge and vulnerable to data bias, such as Leading Bias, resulting in performance degradation. Then a natural question is: *How to derive a well-behaved summarizer in data scarcity FL?*

Generally, data scarcity leads to the knowledge shortage of the summarizer, which is the main reason for degeneration. To tackle this challenge, complementing samples or improving the efficiency of data are two common-used strategies. The former creates samples by applying various transformations to the original data, which generally is computation-costed and heavily relies on the hyperparameters setting. The latter focuses on exploiting limited resources, such as utilizing the distance between measured prototypes and exploring parameters. Although these methods further explore the limited data, the improvement is not remarkable in the practice, due to the neglect of data bias.

To find an effective solution for the degeneration, we propose to maximize the data efficiency in model training. We study the strategy of sample weighting, and mining hidden knowledge from different aspects. We propose FedSum which extends the standard FL framework from depth and breadth to further extract prime and diversified knowledge for constructing the summarizer.

For depth extension, inspired by hard sample mining and bias elimination, we introduce the Data Partition method to recognize the prime samples, and adjust the weight of data by the proposed Data skip mechanism, to further mining prime knowledge. Specifically, we refer to the samples with more unbiased and higher loss samples as prime samples, while pronounced data bias and low supervised loss as normal samples. Since normal samples account for a large proportion in the dataset, the summarizer will easily ignore the prime sample, degrading the generalization, especially under data scarcity. To address it, FedSum dynamically discards part of normal samples based on the training progress, but not all normal samples like the common solutions, preventing further degradation.

For breadth extension, inspired by Multi-Task learning, we extend the source of knowledge in training. FedSum not only learns from data but also from hidden spaces and parameters. Since the prototype is generally regarded as the carrier of semantic information in hidden space, we leverage different prototypes to build prototype loss, improving the generalization and discrimination of features. Then, FedSum constructs the semantic portraits for FL clients by their specific prototypes, and measures the semantic distances between them to maintain the Portrait Distance Table (PDT) on the server. Take the PDT as a guideline, each client can supplement the insufficient semantic knowledge of their representation model by training with the globally received classification heads.

Finally, we evaluate our method on benchmark datasets, showing that FedSum provides a promising total improvement over baselines in ROUGE metrics (0.15% at least and 29.9% at most) and exhibits generalization under various heterogeneity (fluctuation in ROUGE metrics ≤ 2.6% on CNNDM and ≤ 0.3% on PubMed), scalability about data quantity over FL system, and robustness to leading bias.

## 2. Background

### Extractive Text Summarization

Since extracting the key idea from abounding information is valuable in various scenes, many works have been proposed in this track. Inspired by the success of BERT, a summarizer with an enlightening pattern has been proposed, namely BERTSUM. It leverages BERT to represent the input content and then recognizes the most salient sentences by classification modules. Following this pattern, a series of works modify the model architecture to further explore the semantic and structural information. Another branch of work builds contrastive frameworks to reinforce BERTSUM by re-ranking the model result or modifying the learning object.

### Federated Learning

Federated Learning is a rising paradigm in privacy-preserving. A surge of works explore diverse FL applications in NLP. Although FL has strength in protecting privacy, it suffers from degradation problems, caused by heterogeneity and data scarcity.

To alleviate the degradation due to heterogeneity, FedProx introduces a proximal term to restrain the local drift. SCAFFOLD learns personalized control variates referring directions of global updates to guide the local training. FedNova introduces a normalizing weight to eliminate the objective inconsistency and stabilize convergence.

In the data scarcity scenario, like the cold start scenario, models trained by these methods might have difficulty acquiring sufficient knowledge. One intuitive idea is extracting knowledge from hidden space. FedProto extends the concept of prototype learning to FL, reaching feature-wise local alignment with the global prototype. Another branch of methods tries to leverage the extensive knowledge from parameters. FedDC interleaving model aggregation and permutation steps. During a permutation step, it redistributes local models across clients through the server. These above methods mitigate the negative effects of data heterogeneity and scarcity, but not always behave outstanding in the summarization task, due to the neglect of data bias.

## 3. Task Definition and Notations

Given a document (data sample) d={u₁,...,uₛ} with S sentences from dataset D={d₁,...,dₙ}, each sentence is assigned a result φ̂ ∈ [0, 1] through the model (summarizer), representing the probability that the sentence should be extracted. General extractive summarizer f(Ω, ·) parametered by Ω={θ, ω} can be divided into the representation model r(θ, ·) and the classification head h(ω, ·), where f(Ω, ·) = h(ω, r(θ, ·)).

## 4. Method

The data scarcity leads to the knowledge shortage problem, affecting the performance of the summarizer. To address this problem by maximizing the data efficiency, we propose FedSum with two innovative modules: Data Partition and Multi-knowledge Local Training, for depth and breadth extensions.

### 4.1 Data Partition

Similar to recognizing noisy samples, data can be allocated to normal and prime subsets according to their significance for better exploration. In ML, the sample with large training loss is generally considered as a prime sample, which can reflect more guidance about the task. Considering the characteristics of ExtSum, that the extractive summarization can be decomposed to the classification of multiple sentences, we propose that the criterion for the prime sample should be detailed down to the sentence level.

Since the amount of key sentences is much less than the ordinary, the loss of sentences labeled with "1" is more valuable, which can precisely reflect the dilemma in classification. Meanwhile, the label distribution can intuitively reflect the degree of leading bias in the data batch. Thus we refer to the samples with pronounced leading bias and low supervised loss as normal samples, while more unbiased and higher loss samples as prime samples.

### 4.2 Multi-knowledge Local Training

For the lack of knowledge problem caused by data scarcity, FedSum maximizes data efficiency by mining diversified knowledge from three aspects: data, hidden space, and received parameters. For better-exploring data, FedSum extends the standard local training with the Data skip mechanism to discard partial normal samples, promoting the model further focus on the prime samples. To extract knowledge from hidden space, FedSum takes the divergence between local and global prototypes as regularization constraints to promote the generalization and discrimination of feature representation. Mining the missing semantic knowledge from globally received parameters, FedSum takes the semantic portrait distances as a guideline to train the representation model with perturbed classification heads.

#### Data Knowledge and Data Skip Mechanism

Since the proportion of normal samples is more than the proportion of prime, it's common for the model to ignore those prime data, threatening the generalization. To improve performance, a common solution in ML studies is to discard normal data. Due to data scarcity, FedSum does not discard all normal samples to avoid exacerbating degradation. Instead, we propose the Data skip mechanism to skip normal samples according to the skipping probability ρ₍ᵢ,ⱼ₎ which increases with training progress.

As the training progresses, the summarizer will tend to learn more normal patterns than the prime. To enhance the generalization, we skip partial normal samples at the later stage, so that the summarizer can more focus on the samples with greater guidance value. Given j-th batch Bⱼ from i-th client belongs to normal subset D₍ᵢ,N₎, the skipping probability ρ₍ᵢ,ⱼ₎ = (t/T) · (e/E) · (j/τᵢ) is determined by the progress in communication, epoch, and local update.

#### Prototype Knowledge

To extract knowledge from hidden space, we take the prototype as the carrier. Following the definition of the class prototype presented in literature, we denote the class ξ prototype of D₍ᵢ,F₎ in t-th communication round as P₍ᵢ,c₎⁽ξ,t⁾, which take the average over hidden representation of sentences belong to class ξ ∈ {0,1}.

Leveraging these prototypes, we build the prototype loss Lₚₒ with two terms. One term aims to mitigate representation differences between the local and global prototypes, improving the generalization of features. Another aims to discriminate features, promoting the model to fit better decision boundaries.

#### Parameter Knowledge

The semantic knowledge contained in the local model is closely related to the client's data distribution. Different models might have different semantic knowledge deficiencies in practice. To fix the semantic deficiencies in the local model, FedSum extract knowledge from received parameters. FedSum uses PDT to guide the mining process about received parameters and build the parameter lost Lₚₘ, due to nature of PDT in intuitively reflecting the degree of semantic gap between different clients.

## 5. Experiments

### 5.1 Experimental Setup

We investigate the milestone model, BERTSUM, in FL experiments. Several representative algorithms are adopted as baselines: FedAvg, FedProx, SCAFFOLD, FedNova, FedProto, and FedDC. To observe the effect of global aggregation, we also adopt the Separate method, where each client only trains their model locally.

We built different test beds on common benchmark datasets, such as CNN/DailyMail, WikiHow, Reddit, and PubMed. To simulate the data scarcity scenarios, only 2K training samples can be accessed by the FL system. To simulate the non-IID setting, we construct the quantity skew and control the heterogeneity levels through Dir. Smaller Dir indicates a more imbalanced scenario about clients' data quantity, and Dir=+∞ represents the uniform case.

### 5.2 Experimental Results

Overall, FedSum obtains significant improvement in performance over baselines. The most obvious improvements compared to FedAvg are 1.6%/1.31%/1.52% in R-F and 2.18%/1.82%/2.05% in R-R on CNNM. Under data heterogeneity, comparing FedSum with the optimal baseline, there exists 0.15% total improvement at least, and 29.9% total improvement at most over ROUGE metrics on two datasets. These results demonstrate the effectiveness of FedSum.

The performance of FedSum fluctuates slightly (≤ 2.6% on CNNDM) as Dir increases. When Dir is 8, the FedSum ranks second with small gaps from the highest (≤ 1.5%), verifying the generalization of FedSum under different heterogeneous.

To verify the efficacy of tackling the degeneration caused by leading bias, we compare the position of the exacted sentences in the summaries generated between FedSum, FedAvg, and Oracle. The distribution of the extracted proportion about FedSum is more similar to the same of Oracle than FedAvg. The extracted result of FedAvg contains more leading bias than FedSum, shown by a more right-skewed histogram for FedSum.

To explore the scalability of FedSum under varying degrees of data scarcity over the FL system, the performance trends of FedSum and FedAvg with different data quantities are illustrated. Generally, the performance of FedSum becomes better as the data quantity enlarges, demonstrating the scalability in data quantity.

## 6. Conclusion and Limitation

In this paper, we explore the text summarization task in FL, which is more realistic and private than related methods built upon the centralized storage. Besides, data scarcity generally arouses performance degeneration and magnifies the negative effect of leading bias. To address these challenges, we propose FedSum to maximize the data efficiency and construct the summarizer. FedSum demonstrates its promising improvement over baselines on benchmark datasets, while exhibiting its generalization in tackling the intricacies of data heterogeneity. We further verify the scalability of FedSum with various data quantities and the efficacy in mitigating the negative effect of data bias.

Future investigations can build from this foundation to examine other capabilities of the model under data scarcity FL, like stability and fairness. Further experiments are needed to verify the adaptability of our framework for other NLP tasks (e.g. machine translation and sentiment analysis). Besides, our evaluation methodology is based on averages across three experimental runs, which could be enhanced through more rigorous statistical analysis.
