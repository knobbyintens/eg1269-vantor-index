"""Query evaluation over Vantor-Index segments."""

from __future__ import annotations


def intersect(postings_a, postings_b):
    """Galloping intersection of two document posting lists."""
    i = j = 0
    result = []
    while i < len(postings_a) and j < len(postings_b):
        if postings_a[i] == postings_b[j]:
            result.append(postings_a[i])
            i += 1
            j += 1
        elif postings_a[i] < postings_b[j]:
            i += 1
        else:
            j += 1
    return result


def evaluate(segments, query_terms):
    candidates = None
    for term in query_terms:
        postings = None
        for segment in segments:
            if term in segment.postings:
                postings = segment.postings[term]
                break
        if postings is None:
            return []
        candidates = postings if candidates is None else intersect(candidates, postings)
    return candidates or []
