---
title: "Improving Large-Scale Fact-Checking using Decomposable Attention Models and Lexical Tagging"
collection: publications
permalink: /publications/emnlp18
excerpt: 
date: 2018-08-20
venue: 'The Conference on Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 
citation: 
---

[[PDF]](http://aclweb.org/anthology/D18-1143) [[Poster]](/files/EMNLP2018_Poster.pdf)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@InProceedings{D18-1143,
  author = 	"Lee, Nayeon
		and Wu, Chien-Sheng
		and Fung, Pascale",
  title = 	"Improving Large-Scale Fact-Checking using Decomposable Attention Models and Lexical Tagging",
  booktitle = 	"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
  year = 	"2018",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"1133--1138",
  location = 	"Brussels, Belgium",
}
</font>
</pre>

## Abstract
Fact-checking of textual sources needs to effectively extract relevant information from large knowledge bases. In this paper, we extend an existing pipeline approach to better tackle this problem. We propose a neural ranker using a decomposable attention model that dynamically selects sentences to achieve promising improvement in evidence retrieval F1 by 38.80%, with ($\times$65) speedup compared to a TF-IDF method. Moreover, we incorporate lexical tagging methods into our pipeline framework to simplify the tasks and render the model more generalizable. As a result, our framework achieves promising performance on a large-scale fact extraction and verification dataset with speedup.
