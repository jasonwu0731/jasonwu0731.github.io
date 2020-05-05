---
title: "Explicit Memory Tracker with Coarse-to-Fine Reasoning for Conversational Machine Reading"
collection: publications
permalink: /publications/EMT
excerpt: 
date: 2020-04-01
venue: 'ACL 2020'
paperurl: 
citation: 
---

[[PDF]]()

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@article{GaoExplicit2020,
        title={Explicit Memory Tracker with Coarse-to-Fine Reasoning for Conversational Machine Reading},
        author={Gao, Yifan 
          and Wu, Chien-Sheng
          and Joty, Shafiq
          and Xiong, Caiming
          and Socher, Richard
          and King, Irwin 
          and Lyu, Michael R.
          and Hoi, Steven C.H.},
        journal={ACL},
        year={2020}
}
</font>
</pre>


## Abstract
Conversational machine reading aims to teach machines to interact with users and answer their questions. It is challenging because machines have to understand the knowledge base text, evaluate and keep track of the user scenario, ask clarification questions, and then make a final decision. Existing approaches have implicit rule text reasoning processes for decision making and weak abilities for question-related rule extraction.  In this paper, we present a new framework of conversational machine reading with a novel \textbf{E}xplicit \textbf{M}emory \textbf{T}racker (EMT) that explicitly tracks whether conditions listed in the rule text have already been satisfied to make a decision. Moreover, our framework generates clarifying questions by adopting a coarse-to-fine reasoning strategy, utilizing sentence-level selection scores to weight token-level distributions.  On the ShARC benchmark (blind, held-out test set), EMT achieves new state-of-the-art results of 74.8\% micro-averaged decision accuracy and 46.0 BLEU4.  We also show that EMT is more interpretable by visualizing the entailment-oriented reasoning process as the conversation flows. Code and models will be released to facilitate research along this line.
