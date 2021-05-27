---
title: "DISCERN: Discourse-Aware Entailment Reasoning Network for Conversational Machine Reading"
collection: publications
permalink: /publications/DISCERN
excerpt: 
date: 2020-11-31
venue: 'The Conference on Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 
citation: 
---

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@inproceedings{gao-etal-2020-discern,
    title = "Discern: Discourse-Aware Entailment Reasoning Network for Conversational Machine Reading",
    author = "Gao, Yifan  and
      Wu, Chien-Sheng  and
      Li, Jingjing  and
      Joty, Shafiq  and
      Hoi, Steven C.H.  and
      Xiong, Caiming  and
      King, Irwin  and
      Lyu, Michael",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.191",
    doi = "10.18653/v1/2020.emnlp-main.191",
    pages = "2439--2449",
}
</font>
</pre>

## Abstract
Document interpretation and dialog understanding are the two major challenges for conversational machine reading. In this work, we propose {``}Discern{''}, a discourse-aware entailment reasoning network to strengthen the connection and enhance the understanding of both document and dialog. Specifically, we split the document into clause-like elementary discourse units (EDU) using a pre-trained discourse segmentation model, and we train our model in a weakly-supervised manner to predict whether each EDU is entailed by the user feedback in a conversation. Based on the learned EDU and entailment representations, we either reply to the user our final decision {``}yes/no/irrelevant{''} of the initial question, or generate a follow-up question to inquiry more information. Our experiments on the ShARC benchmark (blind, held-out test set) show that Discern achieves state-of-the-art results of 78.3{\%} macro-averaged accuracy on decision making and 64.0 BLEU1 on follow-up question generation.
