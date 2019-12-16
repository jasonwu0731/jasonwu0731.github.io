---
title: "Code-switched language models using neural based synthetic data from parallel sentences"
collection: publications
permalink: /publications/conll19
excerpt: 
date: 2019-11-01
venue: 'Conference on Computational Natural Language Learning (CoNLL)'
paperurl: 
citation: 
---
[[PDF]](https://arxiv.org/abs/1909.08582)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@inproceedings{winata-etal-2019-code,
    title = "Code-Switched Language Models Using Neural Based Synthetic Data from Parallel Sentences",
    author = "Winata, Genta Indra  and
      Madotto, Andrea  and
      Wu, Chien-Sheng  and
      Fung, Pascale",
    booktitle = "Proceedings of the 23rd Conference on Computational Natural Language Learning (CoNLL)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/K19-1026",
    doi = "10.18653/v1/K19-1026",
    pages = "271--280",
}
</font>
</pre>

## Abstract
Training code-switched language models is difficult due to lack of data and complexity in the grammatical structure. Linguistic constraint theories have been used for decades to generate artificial code-switching sentences to cope with this issue. However, this require external word alignments or constituency parsers that create erroneous results on distant languages. We propose a sequence-to-sequence model using a copy mechanism to generate code-switching data by leveraging parallel monolingual translations from a limited source of code-switching data. The model learns how to combine words from parallel sentences and identifies when to switch one language to the other. Moreover, it captures code-switching constraints by attending and aligning the words in inputs, without requiring any external knowledge. Based on experimental results, the language model trained with the generated sentences achieves state-of-the-art performance and improves end-to-end automatic speech recognition.
