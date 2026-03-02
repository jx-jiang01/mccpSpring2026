# Writing Feedback — JIANG Junxiang (蔣俊翔)

JIANG Junxiang (蔣俊翔) Student ID: 25482440 Email: 25482440@life.hkbu.edu.hk Programme: PHD COMP | Group: week6 GitHub: https://github.com/jx-jiang01/mccpSpring2026/tree/main/writing/writingSampleCollection

--- firstDraft.md ---
My First Draft
Source Information
Date written: Feb 23rd, 2026

Context: For the course assignment and my research

Status: Partial draft


Introduction
The objective of Text-to-SQL is to translate Natural Language (NL) queries to SQL queries. This technique holds significant importance for business intelligence, as it represents one of the field’s fundamental challenges. On the one hand, it enables non-technical users to explore insights from data, just as professional database engineers do. On the other hand, it boosts work efficiency for specialists like data analysts. According to the 2023 Stack Overflow survey, SQL ranks among the most widely used programming languages: over half (51.52%) of professional developers utilize it in their work, yet only around one-third (35.29%) have received systematic training in it.

Recently, Large Language Models (LLMs) have brought about transformative changes to the research and application of Text-to-SQL. A user first inputs his questions or requirements into the Text-to-SQL system. Then, the Text-to-SQL system loads database schema and feeds it with the question to LLMs. Thirdly, the system obtains the generated SQL query from LLMs. Finally, return the generated SQL query to the user. In some cases, the system further executes the generated SQL query to retrieve data from the database and returns a corresponding data analysis report to the user. LLM-based Text-to-SQL methods achieve significant improvement. Benefit from the development of LLM, the performance of Text-to-SQL has remarkable improvement. On a well-known benchmark BIRD test set, the execution accuracy has improved from 7.06 to 81.67 within just two to three years. However, only relying on LLMs to solve Text-to-SQL task is expensive and inefficient. For example, some research reveal that feeding all database schema into LLMs could help Text-to-SQL approaches perform better, but it is unacceptable for both users and companies that a few casual words maybe cost more than 100 thousand tokens, because it is cost too much. Furthermore, LLM cannot directly utilize additional information (e.g., knowledge graphs) and instant information.

To alleviate aforementioned weaknesses, Retrieval-Augmented Generation (RAG) is adopted to Text-to-SQL. RAG is a technique that enhances the quality and relevance of generated content by integrating a retrieval component within the generation process. Therefore, the core of RAG is the retrieval model which is used to search useful information and integrate with information with the prompt. In general, the usage of RAG in three aspects within Text-to-SQL system. The first one is to explicitly choose the related database schema from full database schema. In contrast to inputting full schema to LLMs, this method saves a lot of token consumption. The second one is to choose correlated information for the question from additional information, which enhances the performance of Text-to-SQL. The last one is to retrieve examples to teach LLMs to accurately generate SQL. An example usually contains a question, a SQL query and other related information. By doing so, RAG based Text-to-SQL not only deepens the contextual richness of the responses but also guarantees a greater level of factual accuracy and specificity.


Literature Review
We divide research work of Text-to-SQL into three types according to the prompt strategy. These types are vanilla prompting, decomposition prompting and chain-of-thought prompting. Vanilla prompting means prompt only uses zero-shot and few-shot strategies. Zero-shot learning in Text-to-SQL focuses on investigating the impact of prompt representation styles and benchmarking the baseline performance of various LLMs. Few-shot strategy is to integrate several examples with the prompt. Obviously, RAG methods in SQL generation belong to this type. Decomposition prompting refers to a strategy that addresses complex tasks or questions by breaking them down into manageable components, thereby transforming a challenging task or query into a set of simpler sub-tasks or sub-questions. DIN-SQL decomposes the task of natural language text to SQL into multiple sub-tasks and finally achieves competitive performance. Chain-of-Thought (COT) prompting is used to handle the task by making LLMs generate intermediate reasoning steps before predicting SQLs, ensuring that the generated SQL queries are more aligned with human expectations. CHASE-SQL designs three strategies (divide-and-conquer COT, query plan COT and online synthetic example generation) to generate several SQL queries and designing a pair-wise comparison to select the final SQL. CHESS  and OpenSearch-SQL uses chain-of-thought to transform natural language questions into SQL queries and finally achieve good performance.

Although the in-context learning paradigm achieves promising accuracy, from the perspective of computational efficiency, well-designed methods that adopt a multi-stage framework or expand context to increase the number of API calls for performance enhancement have simultaneously led to a substantial rise in costs. The techniques of in-context learning could be incorporated with RAG techniques for Text-to-SQL. For example, the chain-of-thought prompting technique for SQL generation is widely used in RAG based Text-to-SQL, for example, OpenSearch-SQL.


Notes
[Any additional notes about your draft, challenges you faced, questions you have, etc.]

--- pre1_papers.md ---
JIANG Junxiang — Model Papers for Pre1
Literature Folder
JXJ* | GitHub: (not yet linked)
Paper 1
Title: CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL Authors: Pourreza et al. (2025) Venue: ICLR 2025 Field: Natural Language Processing / Database Systems / Text-to-SQL Repo files: Insights | Visualization | Paper MD
Paper 2
Title: OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment Authors: Xie et al. (2025) Venue: (Submitted) Field: NLP / Database Systems / Text-to-SQL Repo files: Insights | Visualization | Paper MD
Notes
Both papers focus on Text-to-SQL — a unified research area
CHASE-SQL is a strong choice for pre1: ICLR 2025, clear methodology, impressive results (73% execution accuracy)
Novelty type: novel combination (multi-path reasoning + preference optimization)

--- reflection.md ---
My Reflection on Writing
Writing Challenges and Difficulties
What aspects of academic writing do you find most challenging?

One of the most challenging aspects of academic writing for me is expressing my ideas in a clear and logical manner. I often struggle to organize my thoughts coherently, which sometimes makes my arguments difficult to follow. Additionally, I find it hard to use precise vocabulary and appropriate transitions to connect my points smoothly, resulting in my writing lacking clarity and flow.

What specific difficulties do you face when writing Introduction/Literature Review?

Sometimes, I find it difficult to summarize the background from a broad, high-level perspective. I tend to focus too much on specific details instead of providing an overall context, which makes it challenging to present a clear and comprehensive introduction or literature review.

What do you struggle with most?

When I write a long paper, I find it difficult to manage all the content effectively. For example, I sometimes forget what I have written in earlier sections while working on the current part, which can make my paper less logical and coherent as a whole.


My Writing Process
How do you approach writing Introduction and Literature Review?

My approach to writing the Introduction and Literature Review consists of several steps. First, I think carefully about the main content I want to include. Next, I create a detailed outline to organize my ideas and structure the section. Then, I fill in the outline by writing the actual content, making sure to cover all the key points. Finally, I revise the draft several times to improve clarity, coherence, and academic quality.

What steps do you take?

Develop an outline to organize my main ideas.
Write and expand on each section according to the outline.
Revise and edit the manuscript multiple times to improve clarity and coherence.

Do you have a particular method or strategy?

I do not use any specific methods.


How I Use AI for Help
Do you use AI tools (ChatGPT, Claude, etc.) to help with writing?

yes, gpt.

How do you use them?

editing, checking grammar, improving sentences

What prompts do you typically use?

please help me refine / polish the content "...".

what do you think about the content "..."

What do you find helpful or not helpful about AI assistance?

I find AI assistance very helpful for editing, grammar checking, and improving sentence structure. However, it is less effective when it comes to providing suggestions or feedback on the main ideas or content of my paper.


My Goals
What do you hope to improve in your writing?

I hope to make my writing more professional. Specifically, I want to learn how to use concise language to clearly express my key ideas.

What specific skills do you want to develop?

I want to develop the skill of using concise language to clearly express my key ideas.


Additional Notes
[Any other thoughts about your writing, concerns, questions, etc.]



