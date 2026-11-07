# Vantor-Index

Reference implementation for the Vantor-Index paper on compressed inverted
indexes.

## Layout

- `src/vantor/indexer.py` - segment builder and postings layout
- `src/vantor/query.py` - query evaluation over the shared metadata layout
- `data/corpus_sample.jsonl` - sample of the retrieval corpus
- `experiments/eval_report.md` - latency / recall measurements

## Usage

```
python -m vantor.indexer --input data/corpus_sample.jsonl --out /tmp/vantor.idx
python -m vantor.query --index /tmp/vantor.idx --queries data/queries.txt
```

Released under the Apache-2.0 license.
