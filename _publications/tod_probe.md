---
title: "Probing Task-Oriented Dialogue Representation from Language Models"
collection: publications
permalink: /publications/tod_probe
excerpt: 
date: 2020-11-31
venue: 'The Conference on Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 
citation: 
---

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@inproceedings{wu-xiong-2020-probing,
    title = "Probing Task-Oriented Dialogue Representation from Language Models",
    author = "Wu, Chien-Sheng  and
      Xiong, Caiming",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.409",
    doi = "10.18653/v1/2020.emnlp-main.409",
    pages = "5036--5051",
}
</font>
</pre>

## Abstract
This paper investigates pre-trained language models to find out which model intrinsically carries the most informative representation for task-oriented dialogue tasks. We approach the problem from two aspects: supervised classifier probe and unsupervised mutual information probe. We fine-tune a feed-forward layer as the classifier probe on top of a fixed pre-trained language model with annotated labels in a supervised way. Meanwhile, we propose an unsupervised mutual information probe to evaluate the mutual dependence between a real clustering and a representation clustering. The goals of this empirical paper are to 1) investigate probing techniques, especially from the unsupervised mutual information aspect, 2) provide guidelines of pre-trained language model selection for the dialogue research community, 3) find insights of pre-training factors for dialogue application that may be the key to success.
