---
title: "Code-Switching Language Modeling using Syntax-Aware Multi-Task Learning"
collection: publications
permalink: /publications/codeswitch2
excerpt: 
date: 2018-06-02
venue: 'The Association for Computational Linguistics (ACL) Code-Switching Workshop'
paperurl: 
citation: 
---
[[PDF]](https://arxiv.org/pdf/1805.12070.pdf)

<pre style="background-color: rgb(230,230,230);white-space: pre-wrap;">
<font size="1">
@article{CS2,
    title={Code-Switching Language Modeling using Syntax-Aware Multi-Task Learning},
    author={Genta Indra Winata, Madotto Andrea, Chien-Sheng Wu, Pascale Fung},
    publisher = {3rd Workshop in Computational Approaches in Linguistic Code-switching},
    year = {2018}
}
</font>
</pre>

## Abstract
Lack of text data has been the major issue on code-switching language modeling. In this paper, we introduce multi-task learning based language model which shares syntax representation of languages to leverage linguistic information and tackle the low resource data issue. Our model jointly learns both language modeling and Part-of-Speech tagging on code-switched utterances. In this way, the model is able to identify the location of code-switching points and improves the prediction of next word. Our approach outperforms standard LSTM based language model, with an improvement of 9.7% and 7.4% in perplexity on SEAME Phase I and Phase II dataset respectively.
