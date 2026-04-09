# learning

Snippets and notes for practice and learning, powered by an **LLM-maintained knowledge base** based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) via [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent).

## How it works

1. Drop source materials (code, notes, articles) into `raw/`
2. Run `/wiki-ingest raw/your-file.md` — the LLM reads it, writes wiki pages, updates cross-references
3. Run `/wiki-query` to ask questions against your compiled knowledge
4. Run `/wiki-lint` to health-check for contradictions, orphan pages, data gaps
5. Run `/wiki-graph` to build an interactive knowledge graph

## Structure

```
raw/          # Immutable source documents
wiki/         # LLM-maintained wiki (index, sources, entities, concepts, syntheses)
graph/        # Auto-generated knowledge graph (vis.js)
tools/        # Optional Python scripts for graph building
```
