---
title: "Global-to-local Memory Pointer Networks for Task-Oriented Dialogue"
collection: publications
permalink: /publications/nips18
excerpt: 
date: 2019-01-01
venue: 'The Conference on Neural Information Processing Systems (NeurIPS)'
paperurl: 
citation: 
---

[[PDF]](https://arxiv.org/abs/1901.04713) [[Slide]](/files/GLMP@NeurIPS 2018.pdf)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@InProceedings{wu2019global,
  author = 	"Wu, Chien-Sheng and Socher, Richard and Xiong, Caiming",
  title = 	"Global-to-local Memory Pointer Networks for Task-Oriented Dialogue",
  booktitle = 	"Proceedings of the 7th International Conference on Learning Representations",
  year = 	"2019",
}
</font>
</pre>


## Abstract
End-to-end task-oriented dialogue is challenging since knowledge bases are usually large, dynamic and hard to incorporate into a learning framework. We propose the global-to-local memory pointer (GLMP) networks to address this issue. In our model, a global memory encoder and a local memory decoder are proposed to share an external knowledge. The encoder encodes dialogue history, modifies global contextual representation that is shared with the decoder, and generates a global memory pointer. The decoder first generates a sketch response with unfilled slots. Next, it passes the global memory pointer to filter the external knowledge for relevant information, then instantiates the slots via the local memory pointers which points to specific entries in the external knowledge. We empirically show that our model can improve copy accuracy and mitigate the common outof-vocabulary problem. As a result, GLMP is able to improve over the previous state-of-the-art models in both simulated bAbI Dialogue and human-human Stanford Multi-domain Dialogue datasets on automatic and human evaluation.
