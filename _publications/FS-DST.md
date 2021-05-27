---
title: "Improving Limited Labeled Dialogue State Tracking with Self-Supervision"
collection: publications
permalink: /publications/FS-DST
excerpt: 
date: 2020-11-31
venue: 'The Conference on Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 
citation: 
---

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@@inproceedings{wu-etal-2020-improving-limited,
    title = "Improving Limited Labeled Dialogue State Tracking with Self-Supervision",
    author = "Wu, Chien-Sheng  and
      Hoi, Steven C.H.  and
      Xiong, Caiming",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.findings-emnlp.400",
    doi = "10.18653/v1/2020.findings-emnlp.400",
    pages = "4462--4472",
}
</font>
</pre>

## Abstract
Existing dialogue state tracking (DST) models require plenty of labeled data. However, collecting high-quality labels is costly, especially when the number of domains increases. In this paper, we address a practical DST problem that is rarely discussed, i.e., learning efficiently with limited labeled data. We present and investigate two self-supervised objectives: preserving latent consistency and modeling conversational behavior. We encourage a DST model to have consistent latent distributions given a perturbed input, making it more robust to an unseen scenario. We also add an auxiliary utterance generation task, modeling a potential correlation between conversational behavior and dialogue states. The experimental results show that our proposed self-supervised signals can improve joint goal accuracy by 8.95{\%} when only 1{\%} labeled data is used on the MultiWOZ dataset. We can achieve an additional 1.76{\%} improvement if some unlabeled data is jointly trained as semi-supervised learning. We analyze and visualize how our proposed self-supervised signals help the DST task and hope to stimulate future data-efficient DST research.