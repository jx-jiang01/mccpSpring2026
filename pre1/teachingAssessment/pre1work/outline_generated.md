# CHASE-SQL Presentation Outline
## 8-Minute Research Presentation - Non-specialist Audience

---

## PRESENTATION OUTLINE & SPEAKER NOTES

### **OPENING (~1 minute)**

#### Main Content
"Imagine you have access to a massive database of information, but you don't know SQL – the technical language needed to search it. What if you could just ask a question in plain English, and an AI system would automatically write the exact search command to find your answer? That's what researchers at Google Cloud and Stanford have solved with a new system called CHASE-SQL.

This work sits at the intersection of artificial intelligence and data science – two fields that are becoming essential across industries like healthcare, finance, and retail. Right now, extracting insights from massive databases requires SQL expertise. But CHASE-SQL aims to change that, making it possible for anyone to query databases without requiring specialized technical training."

#### Presenter Notes
- **Hook Strategy**: Lead with a relatable question that captures the "why this matters" without requiring technical background
- **Context Setting**: Briefly situate the research in a broader societal context
- **Tone**: Conversational but professional; make eye contact with different parts of the audience
- **Emphasis**: Stress "CHASE-SQL" clearly so the audience remembers the name
- **Pause**: Brief pause after the hook question to let it land with the audience
- **Transition**: "Let me explain what this research is really about"

#### Slide Notes
- Slide 1: Title + Hook image (perhaps a simple illustration of databases or data)
- Relevant academic phrases: "Let me begin by...", "The focus of this presentation is..."

---

### **SECTION 1: INTRODUCTION TO THE RESEARCH (~1.5 minutes)**

#### Main Content
"The problem is a classic one in computer science: Large language models – the AI systems behind tools like ChatGPT – are very good at understanding human language. But converting human questions into SQL commands – the specialized language that computers use to search databases – is surprisingly hard. Even the best AI systems only get the answer right about 63% of the time.

Think of it this way: You're standing in a massive library, and you ask a librarian to find books on a specific topic. But the librarian doesn't speak your language perfectly. Sometimes they misunderstand what you're asking for, or they search the wrong catalog section. The researchers wanted to improve the librarian's accuracy.

The key innovation is this: instead of just asking the AI once to translate your question into a search command, they have the AI generate multiple different versions, and then use a second AI system – trained as an expert selector – to pick the best one. This is similar to how good writers revise their work multiple times before settling on the final version."

#### Presenter Notes
- **Accessibility Strategy**: Use the library metaphor to make the database concept tangible
- **Jargon Handling**: Define "SQL" and "Large Language Models" in simple terms; avoid saying "natural language processing" or "transformer architecture"
- **Evidence**: Reference the 63% baseline performance to show why the problem matters
- **Signaling Language**: "Think of it this way..." – this transition helps non-specialists follow
- **Connection to Audience**: "Similar to how good writers revise their work" – this creates a bridge to their own experience
- **Pacing**: Slow down at the library metaphor; speak clearly about the multi-step process
- **Body Language**: Use hand gestures to show the multi-step process (one hand for question, two hands for multiple versions, then point to selector)

#### Slide Notes
- Slide 2: Problem Statement
  - AI accuracy for SQL: 63% baseline
  - Simple icon: Question mark → Database → Answer
- Slide 3: The Librarian Metaphor
  - Illustration of a librarian with multiple book stacks
  - Caption: "Challenge: Understanding questions correctly"

---

### **SECTION 2: KEY FINDINGS (~2 minutes)**

#### Main Content
"So what did the researchers discover? Three main findings:

**First, they found that generating SQL in multiple creative ways improves quality.** The team developed three different strategies: one that breaks complex questions into simpler parts (divide-and-conquer), one that thinks through the problem step-by-step like a database engine would work through it, and one that learns from examples from the specific database being queried. Each method is different enough that it creates diverse candidate answers.

**Second, they found that an AI-trained selector – a system specifically designed to compare SQL commands – outperforms simpler ranking methods.** Interestingly, just picking the most popular answer doesn't always work. The trained selector is like having an expert reviewer who understands the subtle differences between similar but incorrect SQL commands. It ranks all the candidates by comparing them in pairs and scores each one.

**Third – and this is the headline result – their system achieved a 73% success rate, topping the global leaderboard for this challenge.** That's a 10-percentage-point improvement over the previous best approach. To put it in perspective, they jumped from 63% to 73% accuracy. The system works so well that even when using open-source models instead of Google's most powerful proprietary ones, it still achieved 70.3% accuracy."

#### Presenter Notes
- **Enumeration**: Use clear signaling: "First," "Second," "Third" – helps non-specialists follow
- **Impact Framing**: Emphasize the 10-percentage-point improvement as a concrete achievement
- **Avoiding Dense Technical Details**: We're NOT explaining the neural network architecture; we're explaining *what* they did and *how much better* it works
- **Pacing**: Slow down for the three findings; give slight pauses after each one
- **Emphasis**: Stress "73% accuracy" and "10-percentage-point improvement" – these are the concrete results
- **Relatability**: "Like having an expert reviewer" – this is a metaphor all academics understand
- **Voice Modulation**: Vary intonation to keep the audience engaged; slightly raise volume on key numbers
- **Eye Contact**: Make eye contact during the three findings to pull audience in

#### Slide Notes
- Slide 4: Three Generation Strategies (Visual with icons)
  - Break it down / Think step-by-step / Learn from examples
  - Each with a small icon and label
- Slide 5: The Selector System
  - Visual showing multiple SQL options feeding into an "AI Selector" box
  - Result: Ranked candidates with scores
- Slide 6: The Results
  - Large comparison chart: 63% (baseline) vs 73% (CHASE-SQL)
  - Arrow showing +10 percentage point improvement
  - "State-of-the-art results" highlighted

---

### **SECTION 3: SIGNIFICANCE OF THE RESEARCH (~1.5 minutes)**

#### Main Content
"Why should we care about this? Let me highlight three reasons:

**First, this research has immediate practical applications.** Thousands of companies use databases to make decisions – from hospitals managing patient records to retail companies analyzing sales patterns. Right now, professionals need to know SQL to query these databases. But if you improve the accuracy from 63% to 73%, suddenly the system becomes trustworthy enough for non-technical users. This democratizes access to data – it means anyone in an organization can ask questions of the data without needing technical training.

**Second, this research contributes to how we think about using AI systems more broadly.** The key insight – that combining multiple approaches and using a trained selector outperforms single-pass methods – applies far beyond SQL generation. This strategy could improve AI performance in translating languages, generating code, or even writing scientific papers. It's a methodological contribution that other researchers can apply.

**Third, the openness of their approach matters.** The researchers published their work at ICLR, a top-tier conference, and achieved strong results even with open-source models. This means other organizations don't need to build expensive proprietary systems – they can adapt this approach with publicly available AI models. That democratizes innovation."

#### Presenter Notes
- **Broader Context**: Connect back to non-specialist concerns – hospitals, retail, companies
- **Signaling Language**: "First," "Second," "Third" – makes structure crystal clear
- **Accessibility**: Avoid speaking about "multi-agent architectures" or "ensemble methods"; instead say "combining multiple approaches"
- **Relevance Escalation**: Move from immediate (company use) to methodological (AI research) to societal (open innovation)
- **Emphasis**: Stress "democratizes" and "accessible to non-technical users" – these are the real-world impacts
- **Connection to Earlier Content**: Tie back to the librarian metaphor – this is about making the librarian better for everyone
- **Pacing**: Slightly slower pace for this section; allow time to sink in
- **Body Language**: Open hand gestures to convey "accessibility" and "openness"

#### Slide Notes
- Slide 7: Real-World Applications
  - Simple icons/images: Hospital, Retail, Finance
  - Caption: "From specialized to accessible"
- Slide 8: Broader Impact
  - Showing applicability to language translation, code generation
  - "Multi-agent approach works across domains"
- Slide 9: Open Innovation
  - Icon showing open-source, public availability
  - "Accessible to organizations of all sizes"

---

### **SECTION 4: IMPACT ON MY OWN RESEARCH (~1.5 minutes)**

#### Main Content
"Now let me bring this back to my own work and what I've learned from this paper.

**On research design:** This paper teaches me that for complex problems, especially those involving language and AI, a multi-strategy approach outperforms single attempts. In my own research, I'm working on [YOUR RESEARCH AREA]. This paper suggests that I should consider generating multiple candidates from different angles or using different prompting strategies, then applying a thoughtful selection mechanism. I don't have to get the perfect answer on the first try; I should design my system to explore multiple pathways.

**On writing and communication:** The authors of this paper are masterful storytellers. Notice how they frame their work: they start with a simple, relatable problem (AI struggles with SQL); they explain their solution without jargon; they show concrete results (73% vs. 63%); and they discuss implications for the real world. This is exactly the approach I want to adopt in my own research papers.

Additionally, they structure their abstract and introduction carefully. They don't dive into technical details immediately – they first establish why anyone should care. As I write my own research papers, I'm going to adopt this strategy: lead with impact, then explain the method.

And one more thing – see how they justify their approach with evidence? Table 1 in their paper compares different methods and shows why their selector is necessary. I'm learning to support every claim with data, not assumptions. That's the rigor I want to bring to my writing going forward."

#### Presenter Notes
- **Personalization**: Tailor the first paragraph to your actual research (replace [YOUR RESEARCH AREA])
- **Concrete Evidence**: Reference specific writing strategies from the CHASE-SQL paper – this shows deep reading
- **Depth of Reflection**: Move beyond surface-level observations ("the paper is well-written") to specific, actionable insights
- **Demonstrating Learning**: Show that you've analyzed the writing craft, not just the research content
- **Connection**: Tie the writing lessons back to the assessment itself – show you're applying what you've learned
- **Authenticity**: Speak genuinely about your own research; avoid generic statements
- **Emphasis**: Slightly increase energy here; this is where you show critical thinking
- **Eye Contact**: Look directly at the audience; make them feel you're having a conversation

#### Slide Notes
- Slide 10: Learning from This Paper
  - Three key takeaways (with icons or visual hierarchy):
    1. Multi-strategy approach for complex problems
    2. Clear storytelling in academic writing
    3. Evidence-based justification of claims
  - Include a quote from the paper if possible (visual appeal)

---

### **CLOSING (~0.5 minutes)**

#### Main Content
"To sum up: CHASE-SQL shows us that improving AI systems requires not just better algorithms, but smarter workflows – generating diverse candidates and selecting thoughtfully. This work will impact how thousands of non-technical users interact with data. And for me personally, it's a model for how to approach my own research more strategically and how to communicate that research with clarity and impact.

Thank you for your attention. I'm happy to answer any questions."

#### Presenter Notes
- **Recap Phrase**: "To sum up" – signaling language recommended in Session 4
- **Key Takeaway**: One sentence that captures the essence (_strategy matters; diverse approaches work_)
- **Personal Impact**: Remind audience of your own learning
- **Tone Shift**: Slightly slower, more deliberate speech for this closing
- **Pause**: Brief pause before "Thank you" to let conclusions settle
- **Non-verbal**: Stand still during thank you; maintain eye contact
- **Openness**: Smile and use open body language when inviting questions

#### Slide Notes
- Slide 11: Key Takeaway (Summary slide)
  - Visually simple; perhaps a circular icon showing the three components (generation, selection, impact)
  - Bold statement: "Diverse approaches, thoughtful selection, real-world impact"
- Slide 12: Thank You + Contact
  - Professional closing slide
  - Your name, email, research area

---

## SLIDE PLAN & HTML DESIGN SPECIFICATIONS

### Slide Count: 12 slides (approximate timeline for 8-minute presentation)

| Slide # | Section          | Title                                          | Content Type | Time |
|---------|------------------|------------------------------------------------|--------------|------|
| 1       | Opening          | Hook + Title                                   | Text + Image | 0:30 |
| 2       | Intro (Pt. 1)    | The Problem: 63% Accuracy                      | Text + Chart | 0:45 |
| 3       | Intro (Pt. 2)    | The Solution: Multi-Agent Approach             | Metaphor + Visual | 0:45 |
| 4       | Findings (Pt. 1) | Three Generation Strategies                     | Icons + Labels | 0:45 |
| 5       | Findings (Pt. 2) | The Selector: Expert Ranking System             | Process Diagram | 0:45 |
| 6       | Findings (Pt. 3) | Results: 73% Accuracy Achievement               | Chart + Data | 0:45 |
| 7       | Significance     | Real-World Applications                         | Icons + Examples | 0:45 |
| 8       | Significance     | Broader Impact: Multi-Domain Relevance          | Visual Grid | 0:45 |
| 9       | Significance     | Open Innovation & Accessibility                 | Icon + Text | 0:45 |
| 10      | My Research      | Key Takeaways for My Own Work                   | Structured List | 0:45 |
| 11      | Closing          | Summary + Key Insight                           | Visual Summary | 0:30 |
| 12      | Contact          | Thank You + Q&A Invitation                      | Simple Text | 0:15 |

### HTML Design Specifications

#### Framework
- **Technology**: Reveal.js (lightweight, responsive, easy to navigate)
- **Alternative**: Custom HTML5 + CSS3 with simple JavaScript for navigation
- **Navigation**: Arrow keys (left/right) to advance slides, spacebar for next slide
- **Responsive**: Scales appropriately for projector displays and laptops

#### Design Principles
- **Color Scheme**: 
  - Background: Clean white or very light gray (#f8f8f8)
  - Primary accent: Professional blue (#2563eb) or university brand color
  - Secondary accent: Subtle orange/coral (#f97316) for emphasis
  - Text: Dark gray (#1f2937) for readability
  
- **Typography**:
  - Headings: Sans-serif (e.g., Inter, Segoe UI) – 44-54pt, bold
  - Body text: Sans-serif – 28-32pt (large enough to read from back of room)
  - Absolute minimum font: 24pt (for citations/small notes)
  - Maximum text per slide: 5-6 bullet points; no paragraphs
  
- **Layout**:
  - Header area: 20% of slide
  - Content area: 70% of slide
  - Whitespace/footer: 10% of slide
  - Never center-align large text blocks; use left alignment for readability
  - One visual element per slide (image, chart, diagram, or icon set)

#### Visual Elements

**For each slide type:**

1. **Opening/Title Slides**: 
   - Minimalist design with large title and supporting image/illustration
   - Optional: Relevant photograph or abstract graphic
   
2. **Data/Chart Slides**: 
   - Large, clear charts (bar charts for comparison, line charts for progress)
   - Simple legends; use consistent colors
   - Avoid 3D charts or unnecessary complexity
   
3. **Metaphor/Concept Slides**: 
   - Simple illustration or diagram
   - Label each part clearly
   - Keep visual not too detailed (avoid overwhelming non-specialists)
   
4. **List/Structured Slides**: 
   - Bullet points with icons (one icon per bullet)
   - Consistent formatting
   - Animate bullet points to appear one at a time (animation on click)

#### Specific Visuals Needed

- **Slide 1**: Large, engaging title; optional background image (database, network, data streams)
- **Slide 2**: Simple comparison chart (63% vs. baseline methods)
- **Slide 3**: Librarian illustration + arrows showing process
- **Slide 4**: Three side-by-side boxes with icons:
  - Icon 1: Puzzle pieces (divide-and-conquer)
  - Icon 2: Chain links (chain-of-thought)
  - Icon 3: Example papers (synthetic examples)
- **Slide 5**: Flow diagram: Multiple SQL boxes → Selection box → Final answer
- **Slide 6**: Large bar chart: 63% → 73% (with +10 highlighted)
- **Slide 7**: Three icons (hospital, store, finance) with labels
- **Slide 8**: 2×2 grid showing domains (SQL, code, translation, writing)
- **Slide 9**: Open-source/community icon (e.g., GitHub octocat or similar); accessibility symbol
- **Slide 10**: Three numbered takeaways with visual hierarchy
- **Slide 11**: Circular or triangular diagram summarizing the approach
- **Slide 12**: Minimal text with "Thank You" and optional contact info

#### Interaction Features
- **Keyboard controls**: Arrow keys to navigate, Home/End to jump to first/last slide
- **Optional**: Click to advance as alternative to keyboard
- **No auto-progression**: Presenter controls timing
- **Optional speaker notes**: Hidden notes below slide content (only visible to presenter with speaker view)

#### Accessibility Considerations
- High contrast between text and background (WCAG AA compliant)
- No information conveyed by color alone (use patterns/labels as well)
- Alt text for all images (in the HTML)
- Large font sizes throughout

---

## TIMING BREAKDOWN

- **Opening**: 1 minute (Slide 1)
- **Introduction**: 1.5 minutes (Slides 2-3)
- **Key Findings**: 2 minutes (Slides 4-6)
- **Significance**: 1.5 minutes (Slides 7-9)
- **My Research**: 1.5 minutes (Slide 10)
- **Closing**: 0.5 minutes (Slides 11-12)
- **Buffer/Natural pauses**: ~0.5 minutes
- **Total**: 8 minutes (+ time for Q&A)

---

## PRESENTER DELIVERY TIPS ALIGNED WITH RUBRIC

### Content & Structure
✓ Avoid jargon: Replace "natural language processing," "transformer," "pairwise ranking," with accessible terms
✓ Use transition phrases: "Let me move on to...", "The next key finding is...", "This connects to..."
✓ Show deep reflection: Don't just summarize the paper; explain how it influences your thinking

### Delivery & Body Language
✓ Stand still during key statements; use gestures for emphasis on processes/comparisons
✓ Maintain eye contact throughout; don't lock onto one audience member
✓ Pause slightly after delivering each finding to let it land
✓ Vary intonation; avoid monotone delivery
✓ Speak at natural pace; don't rush through numbers/results

### Visual Aids
✓ Keep slides clean and uncluttered
✓ Use large, readable fonts
✓ Let slides support your speech, not replace it
✓ Point to specific elements on slides while speaking

### Language & Accuracy
✓ Use academic register (not too casual, not overly formal)
✓ Use full sentences in speaker's notes but bullet points on slides
✓ Check pronunciation of key terms before presenting (CHASE-SQL = "chase-SQL")
✓ Use signaling language: "First," "Additionally," "In conclusion"

---

## NOTES FOR CUSTOMIZATION

Before finalizing this outline:
1. **Add your own research area** in Section 4 (replace the placeholder)
2. **Personalize examples** if you have specific research interests related to data, AI, or language
3. **select one visual style** for the slides (minimalist, illustrated, data-focused, etc.)
4. **practice timing** with the outline to ensure you stay within 8 minutes
5. **prepare answers** to likely audience questions about SQL, databases, or AI

---

## CHECKLIST BEFORE PRESENTATION

- [ ] Outline finalized and memorized (key points, not word-for-word script)
- [ ] Slides created in Reveal.js or preferred format
- [ ] All visuals optimized for large-screen projection
- [ ] Fonts tested for readability at 10+ feet away
- [ ] Section transitions practiced (smooth, natural delivery)
- [ ] Metaphors and examples rehearsed (to avoid stumbling)
- [ ] Eye contact and body language practiced (record yourself once)
- [ ] Q&A answers prepared for likely questions
- [ ] Slides uploaded to shared folder at least 2 hours before presentation
- [ ] Slides tested on the presentation equipment (projector, laptop, internet connection if needed)

