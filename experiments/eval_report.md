# Vantor-Index evaluation

Latency / recall comparison on the 10M document collection.

| system            | p50 latency | p95 latency | recall@10 |
|-------------------|------------:|------------:|----------:|
| baseline BM25     |      12.4ms |      31.7ms |     0.71  |
| system A          |       9.8ms |      25.2ms |     0.69  |
| system B          |      11.1ms |      29.4ms |     0.74  |
| Vantor-Index      |       7.6ms |      19.8ms |     0.73  |

The shared metadata layout accounts for most of the latency reduction; the
recall difference against system B is within the confidence interval.
