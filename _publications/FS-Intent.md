---
title: "Discriminative Nearest Neighbor Few-Shot Intent Detection by Transferring Natural Language Inference"
collection: publications
permalink: /publications/FS-Intent
excerpt: 
date: 2020-11-31
venue: 'The Conference on Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 
citation: 
---

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@inproceedings{zhang-etal-2020-discriminative,
    title = "Discriminative Nearest Neighbor Few-Shot Intent Detection by Transferring Natural Language Inference",
    author = "Zhang, Jianguo  and
      Hashimoto, Kazuma  and
      Liu, Wenhao  and
      Wu, Chien-Sheng  and
      Wan, Yao  and
      Yu, Philip  and
      Socher, Richard  and
      Xiong, Caiming",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.411",
    doi = "10.18653/v1/2020.emnlp-main.411",
    pages = "5064--5082",
}
</font>
</pre>

## Abstract
Intent detection is one of the core components of goal-oriented dialog systems, and detecting out-of-scope (OOS) intents is also a practically important skill. Few-shot learning is attracting much attention to mitigate data scarcity, but OOS detection becomes even more challenging. In this paper, we present a simple yet effective approach, discriminative nearest neighbor classification with deep self-attention. Unlike softmax classifiers, we leverage BERT-style pairwise encoding to train a binary classifier that estimates the best matched training example for a user input. We propose to boost the discriminative ability by transferring a natural language inference (NLI) model. Our extensive experiments on a large-scale multi-domain intent detection task show that our method achieves more stable and accurate in-domain and OOS detection accuracy than RoBERTa-based classifiers and embedding-based nearest neighbor approaches. More notably, the NLI transfer enables our 10-shot model to perform competitively with 50-shot or even full-shot classifiers, while we can keep the inference time constant by leveraging a faster embedding retrieval model.