# Generate Presentation Outline — Instructions for AI Agent

## What this file does

This file provides instructions for an AI agent to generate a presentation outline and a plan for creating HTML slides for **Oral Presentation Assessment 1: Research Story-telling by Experienced Writers**.

## Instructions for AI Agent

Please complete the following steps:

### Step 1: Read the assessment requirements

Review these files to understand the presentation requirements and rubric:
- `pre1/materials/Presentation_1_Brief.md` — the assessment brief
- `pre1/materials/pre1AssessmentRubrics.md` — the detailed rubric
- `pre1/materials/Session 4_Handout_STUDENT Version_LLM_Formatted.md` — presentation skills guidance

### Step 2: Read the student's paper

Read the journal article placed in the `papers/` subfolder. Identify:
- The research topic and context
- The methodology used
- The key findings and results
- The significance and implications of the research
- Writing strategies used by the authors that are noteworthy

### Step 3: Generate a presentation outline

Create a markdown outline for an **8-minute presentation** with the following structure:

#### Opening (~1 minute)
- Hook to engage the non-specialist audience (story, question, interesting fact, or visual)
- Brief context: what field is this paper from and why does it matter?
- Transition statement to the main body

#### Section 1: Introduction to the Article (~1.5 minutes)
- What is the research about? (explain in accessible language)
- What gap or problem does it address?
- What is the research question or objective?
- **Presenter note:** Use metaphors or everyday examples to explain technical concepts. Avoid jargon. (Rubric: Content appropriate to non-specialist audience)

#### Section 2: Key Findings (~2 minutes)
- What did the researchers find?
- Present 2–3 main findings in clear, non-technical language
- Use specific evidence or data from the paper
- **Presenter note:** Use signaling language ("The findings reveal…", "Our data indicates…"). Reference visuals on slides. (Rubric: In-depth reflection integrated into analysis)

#### Section 3: Significance of the Research (~1.5 minutes)
- Why do these findings matter?
- How do they contribute to the field?
- What are the broader implications?
- **Presenter note:** Connect to broader concerns the audience can relate to. (Rubric: Content entirely appropriate to non-specialist audience)

#### Section 4: Impact on My Own Research (~1.5 minutes)
- How might this paper influence my research design?
- What good writing skills have I learned from this article?
- Provide convincing evidence from the article
- **Presenter note:** Be specific and personal. Show genuine reflection. (Rubric: In-depth reflection well-integrated)

#### Closing (~0.5 minutes)
- Summarize the key takeaway
- Thank the audience and invite questions
- **Presenter note:** Use concluding phrases ("To sum up…", "In conclusion…"). Maintain eye contact. (Rubric: Well-structured with clear logical flow)

### Step 4: Add presenter notes for rubric alignment

For each section, include notes on:
- **Content/Structure:** How to make content accessible; which transition phrases to use
- **Delivery:** Where to pause, emphasize, make eye contact
- **Visual Aids:** What should appear on slides for this section
- **Language:** Suggested academic phrases from Session 4 materials

### Step 5: Create a plan for generating HTML slides

Outline a plan for creating HTML presentation slides that includes:

1. **Slide count estimate** — approximately 8–12 slides for an 8-minute presentation
2. **Slide-by-slide plan** — for each slide:
   - Title
   - Key content (bullet points, not full sentences)
   - Visual elements (diagrams, charts, images, or highlighted quotes)
   - Design notes (minimal text, large font, high contrast)
3. **HTML format specifications:**
   - Use a clean, modern design (e.g., Reveal.js or simple custom CSS)
   - Include navigation (arrow keys or click to advance)
   - Responsive layout for different screen sizes
   - Minimal text on slides — focus on key points and visuals
4. **Sample slide reference** — check `sample_slides/` for format examples

### Step 6: Save the output

Save the generated outline as a markdown file in this folder (e.g., `outline_generated.md`).
Save the slide plan as part of the same file or as `slide_plan.md`.

---

## For the Student

After the AI generates the outline:
1. **Read it carefully** — does it accurately represent your paper?
2. **Check accessibility** — would a non-specialist understand it?
3. **Write your feedback** in `feedback.md`
4. The AI will then revise and generate your HTML slides
