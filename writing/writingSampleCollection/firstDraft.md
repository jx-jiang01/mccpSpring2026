# My First Draft

## Source Information

**Date written:** Feb 23rd, 2026

**Context:** For the course assignment and my research

**Status:** Partial draft

---

## Introduction

The objective of Text-to-SQL is to translate Natural Language (NL) queries to SQL queries. This technique holds significant importance for business intelligence, as it represents one of the field’s fundamental challenges. On the one hand, it enables non-technical users to explore insights from data, just as professional database engineers do. On the other hand, it boosts work efficiency for specialists like data analysts. According to the 2023 Stack Overflow survey, SQL ranks among the most widely used programming languages: over half (51.52%) of professional developers utilize it in their work, yet only around one-third (35.29%) have received systematic training in it. 

Recently, Large Language Models (LLMs) have brought about transformative changes to the research and application of Text-to-SQL. A user first inputs his questions or requirements into the Text-to-SQL system. Then, the Text-to-SQL system loads database schema and feeds it with the question to LLMs. Thirdly, the system obtains the generated SQL query from LLMs. Finally, return the generated SQL query to the user. In some cases, the system further executes the generated SQL query to retrieve data from the database and returns a corresponding data analysis report to the user. LLM-based Text-to-SQL methods achieve significant improvement. Benefit from the development of LLM, the performance of Text-to-SQL has remarkable improvement. On a well-known benchmark BIRD test set, the execution accuracy has improved from 7.06 to 81.67 within just two to three years. However, only relying on LLMs to solve Text-to-SQL task is expensive and inefficient. For example, some research reveal that feeding all database schema into LLMs could help Text-to-SQL approaches perform better, but it is unacceptable for both users and companies that a few casual words maybe cost more than 100 thousand tokens, because it is cost too much. Furthermore, LLM cannot directly utilize additional information (e.g., knowledge graphs) and instant information.

To alleviate aforementioned weaknesses, Retrieval-Augmented Generation (RAG) is adopted to Text-to-SQL. RAG is a technique that enhances the quality and relevance of generated content by integrating a retrieval component within the generation process. Therefore, the core of RAG is the retrieval model which is used to search useful information and integrate with information with the prompt. In general, the usage of RAG in three aspects within Text-to-SQL system. The first one is to explicitly choose the related database schema from full database schema. In contrast to inputting full schema to LLMs, this method saves a lot of token consumption. The second one is to choose correlated information for the question from additional information, which enhances the performance of Text-to-SQL. The last one is to retrieve examples to teach LLMs to accurately generate SQL. An example usually contains a question, a SQL query and other related information. By doing so, RAG based Text-to-SQL not only deepens the contextual richness of the responses but also guarantees a greater level of factual accuracy and specificity.

---

## Literature Review

We divide research work of Text-to-SQL into three types according to the prompt strategy. These types are vanilla prompting, decomposition prompting and chain-of-thought prompting. Vanilla prompting means prompt only uses zero-shot and few-shot strategies. Zero-shot learning in Text-to-SQL focuses on investigating the impact of prompt representation styles and benchmarking the baseline performance of various LLMs. Few-shot strategy is to integrate several examples with the prompt. Obviously, RAG methods in SQL generation belong to this type. Decomposition prompting refers to a strategy that addresses complex tasks or questions by breaking them down into manageable components, thereby transforming a challenging task or query into a set of simpler sub-tasks or sub-questions. DIN-SQL decomposes the task of natural language text to SQL into multiple sub-tasks and finally achieves competitive performance. Chain-of-Thought (COT) prompting is used to handle the task by making LLMs generate intermediate reasoning steps before predicting SQLs, ensuring that the generated SQL queries are more aligned with human expectations. CHASE-SQL designs three strategies (divide-and-conquer COT, query plan COT and online synthetic example generation) to generate several SQL queries and designing a pair-wise comparison to select the final SQL. CHESS  and OpenSearch-SQL uses chain-of-thought to transform natural language questions into SQL queries and finally achieve good performance.

Although the in-context learning paradigm achieves promising accuracy, from the perspective of computational efficiency, well-designed methods that adopt a multi-stage framework or expand context to increase the number of API calls for performance enhancement have simultaneously led to a substantial rise in costs. The techniques of in-context learning could be incorporated with RAG techniques for Text-to-SQL. For example, the chain-of-thought prompting technique for SQL generation is widely used in RAG based Text-to-SQL, for example, OpenSearch-SQL.


---

## Notes

[Any additional notes about your draft, challenges you faced, questions you have, etc.]
