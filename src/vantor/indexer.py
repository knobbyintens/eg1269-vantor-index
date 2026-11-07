"""Segment builder for the Vantor-Index layout."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass
class Segment:
    segment_id: int
    postings: Dict[str, List[int]] = field(default_factory=dict)
    shared_offsets: Dict[str, int] = field(default_factory=dict)

    def add(self, term: str, doc_id: int, offset: int) -> None:
        self.postings.setdefault(term, []).append(doc_id)
        self.shared_offsets.setdefault(term, offset)


def build_segments(path: str | Path, max_terms: int = 4096) -> List[Segment]:
    segments: List[Segment] = []
    current = Segment(segment_id=0)
    with open(path, encoding="utf-8") as handle:
        for doc_id, line in enumerate(handle):
            record = json.loads(line)
            for term in record.get("terms", []):
                if len(current.shared_offsets) >= max_terms and term not in current.shared_offsets:
                    segments.append(current)
                    current = Segment(segment_id=len(segments))
                current.add(term, doc_id, doc_id % 64)
    if current.shared_offsets:
        segments.append(current)
    return segments
