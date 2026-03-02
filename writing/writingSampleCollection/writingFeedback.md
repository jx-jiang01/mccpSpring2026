# Writing Feedback — JIANG Junxiang (蔣俊翔)

## Feedback on JIANG Junxiang's First Draft: Introduction and Literature Review

**Student:** JIANG Junxiang (蔣俊翔)
**Topic:** RAG-Enhanced Text-to-SQL with Large Language Models
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your draft:** writing/writingSampleCollection/firstDraft.md
**Your reflection:** writing/writingSampleCollection/firstDraft.md (reflection section)
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

Your draft shows clear technical understanding of the Text-to-SQL domain and a genuine enthusiasm for the topic. You have the core ingredients: a well-defined research area (RAG-enhanced Text-to-SQL), concrete evidence of progress (execution accuracy from 7.06 to 81.67 on the BIRD benchmark), and a clear motivation for why RAG is needed (cost reduction, performance enhancement). However, the draft needs substantial work in three areas: (1) the Introduction lacks clear move boundaries — it reads as a continuous technical explanation rather than a structured argument; (2) the Literature Review is purely descriptive, listing three prompting strategies without comparing or critiquing them; and (3) there are several grammar and expression issues that weaken the academic tone.

**Estimated current level:** Developing (5–6 range) — The technical content is relevant, but the draft needs significant structural, analytical, and language improvements to reach Satisfactory or above.

---

## Part 1: Introduction Feedback

### What Works Well

- The opening effectively establishes the practical importance of Text-to-SQL with a concrete statistic (Stack Overflow survey: 51.52% use SQL, only 35.29% trained)
- The performance improvement data (7.06 to 81.67 on BIRD) gives readers a tangible sense of progress
- The three uses of RAG in Text-to-SQL (schema selection, additional information retrieval, example retrieval) are clearly enumerated
- The overall argument flow — from problem (NL to SQL) to solution (LLMs) to limitation (cost, no external info) to enhancement (RAG) — is logical

### Issue 1: No Clear Move Structure

Your Introduction reads as a single continuous explanation. The three required moves (Establishing Territory → Identifying the Niche → Occupying the Niche) are present in content but not separated structurally.

**Current structure:** One block covering everything from "what is Text-to-SQL" to "why RAG helps."

**Suggested restructure:**

- **Move 1 (paragraph 1–2):** Establish Text-to-SQL as an important problem. Include the Stack Overflow statistic, the LLM revolution, and the performance gains. Add citations.
- **Move 2 (paragraph 3):** Identify limitations — cost of full schema input (>100K tokens), inability to use external knowledge, lack of real-time information. Frame this as a gap: "Despite these advances, LLM-based Text-to-SQL remains impractical for production deployment because..."
- **Move 3 (paragraph 4):** State your research purpose — how you will use RAG to address these gaps, what specific aspect you focus on, and what contribution your work makes.

Currently, Move 2 and Move 3 are blurred together in the RAG description.

### Issue 2: No Citations in the Introduction

Your Introduction references the "2023 Stack Overflow survey" and "BIRD test set" but provides no formal citations. These are crucial — readers need to verify your claims.

**Action:** Add proper citations for:
- The Stack Overflow survey data
- The BIRD benchmark and the execution accuracy numbers
- The specific research showing that full schema input costs >100K tokens
- The foundational RAG paper or concept

### Issue 3: Grammar and Expression Issues

Several sentences have grammar problems that weaken the academic tone:

- "Benefit from the development of LLM, the performance of Text-to-SQL has remarkable improvement" → "Benefiting from the development of LLMs, Text-to-SQL performance has improved remarkably"
- "it is cost too much" → "it is too costly"
- "some research reveal" → "some studies reveal"
- "In general, the usage of RAG in three aspects" → "In general, RAG is used in three aspects"
- "Furthermore, LLM cannot directly utilize" → "Furthermore, LLMs cannot directly utilize"

**Action:** Do a careful grammar review. Read each sentence aloud — if it sounds awkward, rewrite it. Pay attention to subject-verb agreement and article usage.

### Issue 4: Move 3 Is Missing

Your Introduction describes what RAG does in Text-to-SQL but does not state your specific research question or contribution. The reader finishes the Introduction thinking "this is a nice overview of RAG for Text-to-SQL" but not "this is what this paper specifically contributes."

**Action:** Add a clear Move 3 paragraph: "In this paper, we [investigate/propose/analyze] [specific contribution]. Specifically, we focus on [specific aspect of RAG for Text-to-SQL]. Our work makes the following contributions: (1)... (2)... (3)..."

---

## Part 2: Literature Review Feedback

### What Works Well

- The three-category organization (vanilla prompting, decomposition prompting, chain-of-thought prompting) provides a useful framework
- You name specific systems (DIN-SQL, CHASE-SQL, CHESS, OpenSearch-SQL) which shows engagement with the literature

### Issue 5: Description Without Critical Analysis

This is your most significant Literature Review weakness. You describe what each prompting strategy does but do not evaluate how well they work, what their limitations are, or how they compare to each other.

**Your sentence (description only):** "DIN-SQL decomposes the task of natural language text to SQL into multiple sub-tasks and finally achieves competitive performance."

**With critical analysis:** "DIN-SQL decomposes the Text-to-SQL task into sub-tasks including schema linking, query classification, and SQL generation, achieving competitive performance on the Spider benchmark [citation]. However, this decomposition introduces additional LLM calls at each stage, increasing both latency and token cost. Compared to vanilla prompting approaches, decomposition methods trade computational efficiency for accuracy — a tradeoff that may not be acceptable in production environments with strict latency requirements."

### Issue 6: Literature Review Is Too Brief

Your Literature Review is only one paragraph covering three categories of prompting strategies. For a 1000–1500 word assignment, the Literature Review should be substantially longer and more developed than the Introduction.

**Action:**
- Expand each prompting category into its own paragraph with 3–4 papers analyzed
- Add a RAG-specific section — since your topic is RAG for Text-to-SQL, the Literature Review should have a dedicated section reviewing RAG approaches
- Include a comparison across categories: which approach works best under what conditions?

### Issue 7: Missing Moves 3 and 4

Your Literature Review only covers Move 2 (Critical Analysis). You need:
- **Move 1 (Thematic Overview):** Set up the categories and explain why you organized the literature this way
- **Move 3 (Research Gaps):** What remains unaddressed? Which RAG approaches need improvement?
- **Move 4 (Conclusion):** Summarize key insights and connect to your research

---

## Part 3: Reflection and Goals

Your reflection is honest and shows good self-awareness — you want to write more concisely and professionally. Your note that AI is "less effective when it comes to providing suggestions or feedback on the main ideas" is an important insight.

**Suggestion for your revision process:**
1. Write the structural outline first (moves for Introduction and Literature Review)
2. Fill in each move with content, focusing on one move at a time
3. Add citations as you write, not after
4. Use AI only for grammar checking at the end, not for content generation

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 High | Restructure Introduction into clear Move 1, 2, 3 paragraphs | Makes argument visible |
| 🔴 High | Add a clear Move 3 stating your specific research contribution | Tells readers what your paper does |
| 🔴 High | Add citations throughout | Makes claims verifiable |
| 🔴 High | Fix grammar issues (subject-verb agreement, articles, expression) | Improves academic tone |
| 🟡 Medium | Expand Literature Review to multiple paragraphs with critical analysis | Demonstrates engagement with the field |
| 🟡 Medium | Add Moves 1, 3, 4 to the Literature Review | Completes the required structure |
| 🟡 Medium | Add a RAG-specific review section | Aligns literature with your topic |
| 🟢 Lower | Improve conciseness (your stated goal) | Sharpens writing quality |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. Restructure your Introduction into clearly separated moves
3. Expand the Literature Review with critical analysis and all four moves
4. Fix grammar issues throughout
5. Submit by **15 March 2026** via Moodle forum and Turnitin
