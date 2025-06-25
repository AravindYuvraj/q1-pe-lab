# 📓 Hallucinations Log

This document records hallucinations (i.e. factual inaccuracies or misleading information) found in the responses across different prompting strategies.

---

## ID: 1 — Solve for x: 5x - 7 = 18

**Hallucinations**:
None
**Notes**:
All methods (Zero-shot, Few-shot, CoT, Meta-prompt) correctly solve the equation with appropriate steps and explanations. No inaccuracies detected.

---

## ID: 2 — What is the area of a circle with radius 7 cm?

**Hallucinations**:

* ✅ *Zero-shot*: Area = **153.86 cm²**
* ✅ *Few-shot*, *CoT*, *Meta-prompt*: Area = **152.86 cm²**

**Issue**:
There's an inconsistency in π approximation:

* 3.14 × 49 = **153.86**, which is what *Zero-shot* uses.
* But 3.14 × 49 actually equals **153.86**, not **152.86**.

**Verdict**:
*Zero-shot* is correct.
*Few-shot*, *CoT*, and *Meta-prompt* responses contain a **minor calculation error** likely due to mistyping or incorrect recall of multiplication.

**Suggested Fix**:
Correct 3.14 × 49 to 153.86 in those responses.

---

## ID: 3 — Explain the difference between mean, median, and mode

**Hallucinations**:

* *Zero-shot*: Mean = **97.5** for \[80, 70, 90, 85, 75, 95]

**Issue**:
Incorrect calculation of the mean:

* Sum: 80 + 70 + 90 + 85 + 75 + 95 = **495**
* Count: 6
* Mean = 495 / 6 = **82.5**, not **97.5**

**Verdict**:
*Zero-shot* hallucinated the mean value.
*Few-shot*, *CoT*, and *Meta-prompt* use different and valid examples.

**Suggested Fix**:
Update mean example calculation to correct sum and result.

---

## ID: 4 — A train travels 120 km in 3 hours. What is its speed?

**Hallucinations**:
None
**Notes**:
All strategies compute speed correctly using `Speed = Distance / Time`. Final answer: **40 km/h** is consistent across responses.