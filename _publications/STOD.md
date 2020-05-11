---
title: "A Simple Language Model for Task-Oriented Dialogue"
collection: publications
permalink: /publications/STOD
excerpt: 
date: 2020-04-30
venue: 
paperurl: 
citation: 
---

[[PDF]](https://arxiv.org/abs/2005.00796)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@article{hosseini2020simple,
  title={A Simple Language Model for Task-Oriented Dialogue},
  author={Hosseini-Asl, Ehsan and McCann, Bryan and Wu, Chien-Sheng and Yavuz, Semih and Socher, Richard},
  journal={arXiv preprint arXiv:2005.00796},
  year={2020}
}
</font>
</pre>


## Abstract
Task-oriented dialogue is often decomposed into three tasks: understanding user input, deciding actions, and generating a response. This allows for dedicated models for each sub-task, but we find a simple, unified approach leads to state-of-the-art performance across multiple settings on the MultiWOZ dataset. SimpleTOD is a simple approach to task-oriented dialogue that uses a single causal language model trained on all sub-tasks recast as a single sequence prediction problem. This allows SimpleTOD to fully leverage transfer learning from pre-trained, open domain, causal language models such as GPT-2. SimpleTOD improves over the prior state-of-the-art by 1.22 points in joint goal accuracy for dialogue state tracking. SimpleTOD also improves all three metrics used to evaluate action and response generation in the most complete setting for task-oriented dialog systems: inform rate by 8.1 points, success rate by 9.7 points, and BLEU by 23.5 points.
