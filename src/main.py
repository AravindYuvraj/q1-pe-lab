import json
import subprocess
from pathlib import Path

# === Paths (relative to project root) ===
PROMPTS_DIR = Path("../prompts")
EVAL_DIR = Path("../evaluation")

PROMPT_FILES = {
    "zero_shot": PROMPTS_DIR / "zero_shot.txt",
    "few_shot": PROMPTS_DIR / "few_shot.txt",
    "cot": PROMPTS_DIR / "cot_prompt.txt",
    "meta_prompt": PROMPTS_DIR / "meta_prompt.txt"
}

INPUT_FILE = EVAL_DIR / "input_queries.json"
OUTPUT_FILE = EVAL_DIR / "output_logs.json"

# === Detect if model is confused or uncertain ===
def is_ambiguous(response: str) -> bool:
    ambiguous_phrases = [
        "I'm not sure", "unclear", "need more information",
        "don't understand", "cannot determine", "ambiguous",
        "please rephrase"
    ]
    return any(phrase.lower() in response.lower() for phrase in ambiguous_phrases)

# === Load a specific prompt style ===
def load_prompt(style: str) -> str:
    return PROMPT_FILES[style].read_text(encoding="utf-8")

# === Run prompt through LLaMA 3 via Ollama ===
def run_ollama(query: str, full_prompt: str) -> str:
    cmd = ["ollama", "run", "llama3:8b"]
    input_text = full_prompt + "\n\nQuestion: " + query
    result = subprocess.run(
        cmd,
        input=input_text.encode("utf-8"),  # fixed encoding
        capture_output=True
    )
    return result.stdout.decode("utf-8", errors="ignore").strip()

# === Fallback if LLM returns unclear/confused response ===
def fallback_clarification(query: str) -> str:
    clarification_prompt = f"""You received a possibly ambiguous math question. Ask the student to clarify or rephrase.

Question: {query}
Response:"""
    return run_ollama(query, clarification_prompt)

# === Main driver ===
def main():
    queries = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    output_logs = []

    for q in queries:
        entry = {"id": q["id"], "query": q["query"], "results": {}}

        for style in PROMPT_FILES:
            print(f"🧠 Running LLaMA 3 [{style}] on Q{q['id']}...")
            base_prompt = load_prompt(style)
            response = run_ollama(q["query"], base_prompt)

            if is_ambiguous(response):
                print(f"⚠️ Ambiguity detected for Q{q['id']} with {style} prompt.")
                clarification = fallback_clarification(q["query"])
                entry["results"][style] = {
                    "response": response,
                    "fallback": clarification
                }
            else:
                entry["results"][style] = {"response": response}

        # 🆕 Write partial result after each query
        output_logs.append(entry)
        OUTPUT_FILE.write_text(json.dumps(output_logs, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n✅ All outputs saved to {OUTPUT_FILE.resolve()}")

if __name__ == "__main__":
    main()
