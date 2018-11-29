---
title: "Mem2Seq: Effectively Incorporating Knowledge Bases into End-to-End Task-Oriented Dialog Systems"
collection: publications
permalink: /publications/Mem2Seq
excerpt: 
date: 2018-04-20
venue: 'The Association for Computational Linguistics (ACL)'
paperurl: 
citation: 
---

[[PDF]](https://arxiv.org/pdf/1804.08217.pdf) [[Poster]](/files/mem2seq-poster) [[Code]](https://github.com/HLTCHKUST/Mem2Seq)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@InProceedings{P18-1136,
  author = 	"Madotto, Andrea
		and Wu, Chien-Sheng
		and Fung, Pascale",
  title = 	"Mem2Seq: Effectively Incorporating Knowledge Bases into End-to-End Task-Oriented Dialog Systems",
  booktitle = 	"Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  year = 	"2018",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"1468--1478",
  location = 	"Melbourne, Australia",
  url = 	"http://aclweb.org/anthology/P18-1136"
}
</font>
</pre>

## Abstract
End-to-end task-oriented dialog systems usually suffer from the challenge of incorporating knowledge bases. In this paper, we propose a novel yet simple end-toend differentiable model called memoryto-sequence (Mem2Seq) to address this issue. Mem2Seq is the first neural generative model that combines the multihop attention over memories with the idea of pointer network. We empirically show how Mem2Seq controls each generation step, and how its multi-hop attention mechanism helps in learning correlations between memories. In addition, our model is quite general without complicated taskspecific designs. As a result, we show that Mem2Seq can be trained faster and attain the state-of-the-art performance on three different task-oriented dialog datasets
