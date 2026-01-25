# JJGou Literature Analysis - Completed

## Overview

This folder contains analysis of two related papers on Graph Edit Distance (GED) computation by Lijun Chang and colleagues. Both papers represent important contributions to database systems and graph algorithms research.

---

## Papers Analyzed

### 1. App-BMao Paper
**Full Title**: Graph Edit Distance Estimation: A New Heuristic and A Holistic Evaluation of Learning-based Methods  
**Authors**: Mouyi Xu, Lijun Chang (The University of Sydney)  
**Venue**: SIGMOD 2025 (Proc. ACM Manag. Data, Vol. 3, No. 3, Article 167)  
**Length**: 24 pages  
**Type**: Full research article with survey component  

**Key Contributions**:
- Comprehensive survey of learning-based GED prediction methods
- Novel taxonomy: Interpretable vs. non-interpretable approaches
- Framework identification: Three-module pattern across models
- New heuristic algorithm App-BMao that outperforms all learning-based methods

**Significance**: Challenges the assumption that deep learning always outperforms traditional methods in GED prediction.

### 2. AStar-BMao Paper
**Full Title**: Accelerating Graph Similarity Search via Efficient GED Computation  
**Authors**: Lijun Chang, Xing Feng, Kai Yao, Lu Qin, Wenjie Zhang  
**Venue**: IEEE Transactions (appears to be TKDE or similar)  
**Length**: ~15 pages  
**Type**: Journal article on algorithmic improvement  

**Key Contributions**:
- New lower bound lbBMa for GED computation (tighter than state-of-the-art)
- Optimized version lbBMao that balances tightness and efficiency
- Addresses memory consumption limitations of previous algorithms
- Formal proofs of correctness and tightness

**Significance**: Enables GED computation to scale to larger graphs and thresholds through improved memory efficiency.

---

## Files in This Folder

### Original Papers
- `App-Bmao.pdf` - Original PDF of SIGMOD 2025 paper
- `AStar-Bmao.pdf` - Original PDF of IEEE paper

### Converted Markdown
- `App-Bmao.md` - Full text converted from PDF (2,429 lines)
- `AStar-Bmao.md` - Full text converted from PDF (3,261 lines)

### Analysis Reports
- `AppBMaoInsights.md` - Comprehensive macro-level structure analysis
  - Section-by-section CARS model analysis
  - Rhetorical strategies identification
  - Cross-disciplinary comparison
  - Imitation opportunities for future writing
  
- `AStarBMaoInsights.md` - Comprehensive macro-level structure analysis
  - Two-stage refinement strategy analysis
  - Incremental innovation model
  - Trade-off articulation techniques
  - Comparison with companion paper

### Visualizations
- `AppBMaoVisualization.html` - Interactive HTML visualization of paper structure
  - Color-coded sections (Introduction, Survey, Contribution, Experiments)
  - CARS moves visualization
  - Key excerpts and analysis
  - Comparison tables
  
- `AStarBMaoVisualization.html` - Interactive HTML visualization of paper structure
  - Two-stage refinement flow
  - Trade-off boxes highlighting key decisions
  - Incremental innovation model
  - Comparison tables

### Documentation
- `process.log` - Detailed log of analysis process
- `retrieveAnalyze.md` - Original task instructions
- `README.md` - This file

---

## Key Insights for Academic Writing

### From App-BMao Paper

#### 1. Survey-as-Contribution Model
- Comprehensive literature review can be a primary contribution, not just background
- Dedicate substantial space (~8 pages) to systematic survey
- Create original taxonomy to organize existing work

#### 2. Framework Identification
- Abstract common design patterns across different approaches
- Shows deep understanding beyond surface-level description
- Example: Three-module framework (Siamese GNN → Fusion → Prediction)

#### 3. Cross-Community Synthesis
- Bridge multiple research communities (DB, ML, IR, CV)
- Identify gaps in cross-field evaluation
- Provide comprehensive comparison across communities

#### 4. Challenging Conventional Wisdom
- Counter-narrative: Simple heuristic can outperform complex deep learning
- Requires strong empirical evidence (tests against ALL surveyed methods)
- Honest about when each approach works best

### From AStar-BMao Paper

#### 1. Incremental Innovation Model
- Significant improvement over state-of-the-art is valuable research
- Don't need revolutionary change - targeted improvement is sufficient
- Focus on specific, practical limitations (memory consumption)

#### 2. Two-Stage Refinement Strategy
- Present ideal solution first (lbBMa - tightest bounds)
- Then present practical optimization (lbBMao - efficient computation)
- Shows sophisticated algorithm design through iteration

#### 3. Explicit Trade-off Discussion
- Openly discuss trade-offs (tightness vs. efficiency)
- Acknowledge when ideal solution is impractical
- "To strike a balance between..." demonstrates maturity

#### 4. Formal Guarantees
- Provide correctness proofs
- Prove relative tightness (lbBMao ≥ lbLSa)
- State complexity bounds explicitly

---

## Relationship Between Papers

These two papers are closely related but distinct:

| Aspect | AStar-BMao | App-BMao |
|--------|------------|----------|
| **Problem** | Exact GED computation | GED estimation (approximate) |
| **Foundation** | Proposes new algorithm | Adapts AStar-BMao for estimation |
| **Scope** | Focused algorithmic improvement | Broad survey + new heuristic |
| **Contribution Type** | Incremental innovation | Survey + challenging ML methods |
| **Narrative** | Improving state-of-the-art | Questioning conventional wisdom |

**Connection**: App-BMao adapts the AStar-BMao algorithm (exact computation) for GED estimation, then compares it against all learning-based methods.

---

## Imitation Opportunities

### Structural Elements
1. **Dual Contribution**: Survey + new method (App-BMao model)
2. **Two-Stage Solution**: Ideal → Practical (AStar-BMao model)
3. **Taxonomy Development**: Create original categorization schemes
4. **Framework Abstraction**: Identify common patterns across approaches
5. **Late Related Work**: Place after experiments if comprehensive survey earlier

### Rhetorical Strategies
1. **Enumerated Gaps**: "(1)... (2)..." for clear limitation identification
2. **Visual Argumentation**: Use figures to support claims (not just illustrate)
3. **Critical Survey**: Analyze and critique, don't just describe
4. **Trade-off Framing**: "To strike a balance between..." shows sophistication
5. **Comparative Language**: Constant positioning against baselines

### Quality Indicators
1. **Comprehensive Coverage**: Survey all relevant work, not just selected papers
2. **Formal Guarantees**: Proofs of correctness, tightness, complexity bounds
3. **Multi-Dimensional Evaluation**: Time, space, accuracy metrics
4. **Honest Limitations**: Acknowledge when approaches don't work well
5. **Cross-Community Synthesis**: Bridge multiple research areas

---

## How to Use These Materials

### For Understanding Paper Structure
1. Read the Insights.md files for detailed analysis
2. Open the Visualization.html files in a browser for interactive exploration
3. Compare the two papers to see different rhetorical strategies

### For Learning Academic Writing
1. Study the CARS model application in Introduction sections
2. Examine how gaps are identified and occupied
3. Note the use of enumeration, visual evidence, and comparative language
4. Observe how trade-offs are articulated

### For Writing Your Own Papers
1. Identify which model fits your contribution (survey vs. incremental innovation)
2. Adapt structural elements appropriate to your work
3. Use rhetorical strategies for clear positioning
4. Follow quality indicators for rigorous research

---

## Analysis Methodology

The analysis follows the framework from `writing/activity 1.2 analyze macro-level structure`:

1. **CARS Model** (Creating a Research Space):
   - Move 1: Establishing Territory
   - Move 2: Establishing Niche
   - Move 3: Occupying Niche

2. **Hourglass Flow**: General → Specific → General

3. **Section-by-Section Analysis**: 
   - Purpose and content
   - Key excerpts with line references
   - Rhetorical strategies
   - Linguistic features

4. **Cross-Disciplinary Comparison**: Database/Algorithms vs. Machine Learning

5. **Imitation Framework**: Actionable insights for future writing

---

## References

### App-BMao Paper Citation
```
Mouyi Xu and Lijun Chang. 2025. Graph Edit Distance Estimation: A New Heuristic 
and A Holistic Evaluation of Learning-based Methods. Proc. ACM Manag. Data 3, 3 
(SIGMOD), Article 167 (June 2025), 24 pages. https://doi.org/10.1145/3725304
```

### AStar-BMao Paper Citation
```
Lijun Chang, Xing Feng, Kai Yao, Lu Qin, Wenjie Zhang. Accelerating Graph 
Similarity Search via Efficient GED Computation. IEEE Transactions.
```

---

## Completion Status

✅ All tasks completed as specified in `retrieveAnalyze.md`:
- ✅ Searched for HTML versions (none available)
- ✅ Converted PDFs to markdown
- ✅ Analyzed macro-level structure
- ✅ Generated insights reports with extensive excerpts
- ✅ Created visualization HTML files
- ✅ Documented process in log file

**Date Completed**: January 11, 2026

---

## Contact

For questions about this analysis, refer to:
- `process.log` for detailed process documentation
- `AppBMaoInsights.md` and `AStarBMaoInsights.md` for comprehensive analysis
- Original task specification in `retrieveAnalyze.md`
