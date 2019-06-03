---
title: "Personalizing Dialogue Agents via Meta-Learning"
collection: publications
permalink: /publications/DAML
excerpt: 
date: 2019-06-02
venue: 'The 57th Annual Meeting of the Association for Computational Linguistics (ACL)'
paperurl: 
citation: 
---

[[PDF]](https://arxiv.org/abs/1905.10033) [[Code]](https://github.com/HLTCHKUST/PAML)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@InProceedings{WuTradeDST2019,
  author = 	"Madotto, Andrea
    and Lin, ZhaoJiang
    and Wu, Chien-Sheng
		and Fung, Pascale",
  title = 	"Personalizing Dialogue Agents via Meta-Learning",
  booktitle = 	"Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  year = 	"2019",
  publisher = 	"Association for Computational Linguistics"
}
</font>
</pre>


## Abstract
Existing personalized dialogue models use human designed persona descriptions to improve dialogue consistency. Collecting such descriptions from existing dialogues is expensive and requires hand-crafted feature designs. In this paper, we propose to extend Model-Agnostic Meta-Learning (MAML)(Finn et al., 2017) to personalized dialogue learning without using any persona descriptions. Our model learns to quickly adapt to new personas by leveraging only a few dialogue samples collected from the same user, which is fundamentally different from conditioning the response on the persona descriptions. Empirical results on Persona-chat dataset (Zhang et al., 2018) indicate that our solution outperforms non-meta-learning baselines using automatic evaluation metrics, and in terms of human-evaluated fluency and consistency.
