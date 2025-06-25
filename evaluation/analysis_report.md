Comparing the styles across four prompting methods: **zero\_shot**, **few\_shot**, **cot (Chain-of-Thought)**, and **meta\_prompt**.

---

### **1. Solve for x: 5x - 7 = 18**

| Prompt Type     | Summary of Style & Content                                                                                                                    |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zero-Shot**   | Friendly tone, walks step-by-step through solving the equation with explanations, includes follow-up encouragement (“Does that make sense?”). |
| **Few-Shot**    | Concise, to the point: shows only the essential steps to get the answer.                                                                      |
| **CoT**         | Structured breakdown with labeled steps and rationale, educational tone.                                                                      |
| **Meta-Prompt** | Contextualizes topic (“Linear Equations”), gives clear steps, concise but with educational framing.                                           |

---

### 📏 **2. Area of Circle with Radius 7 cm**

| Prompt Type     | Summary of Style & Content                                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Zero-Shot**   | Friendly intro, formula given, detailed step-by-step including approximation of π. Result: \~153.86 cm².                      |
| **Few-Shot**    | Balanced explanation: formula, substitution, and approximation. Result: \~152.86 cm² (slight π variation).                    |
| **CoT**         | Stepwise explanation emphasizing each step: recall formula, identify input, substitute, calculate. Very instructive.          |
| **Meta-Prompt** | Framed as “Topic: Circles!”, gives a quick walkthrough with formulas and final result. Slightly rounded result: \~152.86 cm². |

---

### **3. Explain Mean, Median, Mode**

| Prompt Type     | Summary of Style & Content                                                                                                                                                                                                                         |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zero-Shot**   | Very verbose. Breaks down each concept thoroughly with examples, but has a **mistake in the mean** example (incorrect average: says 97.5 when it should be 97.5 only if sum was 585 — but 585 ÷ 6 is 97.5, which doesn't match the listed scores). |
| **Few-Shot**    | Clean, friendly, concise explanation with short examples.                                                                                                                                                                                          |
| **CoT**         | Very stepwise. Breaks each term down with bullet-pointed examples. Strong teaching tone.                                                                                                                                                           |
| **Meta-Prompt** | Labelled “Topic: Statistics”, walks through each concept with examples. However, includes a **math error in median example** (says (5 + 6)/2 = 5.5 when those weren’t the middle values).                                                          |

---

### **4. Speed = Distance ÷ Time (120 km in 3 hr)**

| Prompt Type     | Summary of Style & Content                                                                                                             |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Zero-Shot**   | Friendly, straightforward calculation and gentle closure.                                                                              |
| **Few-Shot**    | Efficient and formula-focused explanation, ends with clean answer.                                                                     |
| **CoT**         | Starts well with clear stepwise explanation, but the response is **cut off at the end**, suggesting a truncation or incomplete output. |

---

### Observations Across Prompt Types

* **Zero-Shot** is often friendlier and more verbose but risks inconsistency or redundancy.
* **Few-Shot** offers efficient, compact reasoning — great for quick answers.
* **CoT** excels in pedagogical clarity; often best for teaching/learning contexts.
* **Meta-Prompt** adds meta-context (“Topic: …”), useful in learning environments or generating content like tutorials.
