---
title: "GraPPa: Grammar-Augmented Pre-Training for Table Semantic Parsing"
collection: publications
permalink: /publications/grappa
excerpt: 
date: 2021-02-01
venue: 'The International Conference on Learning Representations. (ICLR)'
paperurl: 
citation: 
---
[[PDF]](https://openreview.net/forum?id=kyaIeYj4zZ)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@article{yu2020grappa,
  title={GraPPa: Grammar-Augmented Pre-Training for Table Semantic Parsing},
  author={Yu, Tao and Wu, Chien-Sheng and Lin, Xi Victoria and Wang, Bailin and Tan, Yi Chern and Yang, Xinyi and Radev, Dragomir and Socher, Richard and Xiong, Caiming},
  journal={arXiv preprint arXiv:2009.13845},
  year={2020}
}
</font>
</pre>

## Abstract
We present GraPPa, an effective pre-training approach for table semantic parsing that learns a compositional inductive bias in the joint representations of textual and tabular data. We construct synthetic question-SQL pairs over high-quality tables via a synchronous context-free grammar (SCFG). We pre-train our model on the synthetic data to inject important structural properties commonly found in semantic parsing into the pre-training language model. To maintain the model's ability to represent real-world data, we also include masked language modeling (MLM) on several existing table-related datasets to regularize our pre-training process.  Our proposed pre-training strategy is much data-efficient. When incorporated with strong base semantic parsers, GraPPa achieves new state-of-the-art results on four popular fully supervised and weakly supervised table semantic parsing tasks.
