---
title: "Transferable Multi-Domain State Generator for Task-Oriented Dialogue Systems"
collection: publications
permalink: /publications/trade
excerpt: 
date: 2019-06-01
venue: 'The 57th Annual Meeting of the Association for Computational Linguistics (ACL)'
paperurl: 
citation: 
---

[[PDF]](https://arxiv.org/abs/1905.08743) [[Code]](https://github.com/jasonwu0731/trade-dst)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@InProceedings{WuTradeDST2019,
  author = 	"Wu, Chien-Sheng
		and Madotto, Andrea
    		and Hosseini-Asl, Ehsan 
    		and Xiong, Caiming 
    		and Socher, Richard
    		and Fung, Pascale",
  title = 	"Transferable Multi-Domain State Generator for Task-Oriented Dialogue Systems",
  booktitle = 	"Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  year = 	"2019",
  publisher = 	"Association for Computational Linguistics"
}
</font>
</pre>


## Abstract
Over-dependence on domain ontology and lack of knowledge sharing across domains are two practical and yet less studied problems of dialogue state tracking. Existing approaches generally fall short in tracking unknown slot values during inference and often have difficulties in adapting to new domains. In this paper, we propose a Transferable Dialogue State Generator (TRADE) that generates dialogue states from utterances using a copy mechanism, facilitating knowledge transfer when predicting (domain, slot, value) triplets not encountered during training. Our model is composed of an utterance encoder, a slot gate, and a state generator, which are shared across domains. Empirical results demonstrate that TRADE achieves state-of-the-art joint goal accuracy of 48.62% for the five domains of MultiWOZ, a human-human dialogue dataset. In addition, we show its transferring ability by simulating zero-shot and few-shot dialogue state tracking for unseen domains. TRADE achieves 60.58% joint goal accuracy in one of the zero-shot domains, and is able to adapt to few-shot cases without forgetting already trained domains.

