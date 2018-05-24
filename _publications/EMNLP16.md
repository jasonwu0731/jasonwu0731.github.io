---
title: "Real-Time Speech Emotion and Sentiment Recognition for Interactive Dialogue Systems"
collection: publications
permalink: /publications/EMNLP16
excerpt: 
date: 2016-11-01
venue: 'The Conference on Empirical Methods on Natural Language Processing. (EMNLP)'
paperurl: 
citation: 
---
[[PDF]](http://aclweb.org/anthology/D16-1110) 
<a href="https://scholar.googleusercontent.com/scholar.bib?q=info:AL_PtWU_WIkJ:scholar.google.com/&output=citation&scisig=AAGBfm0AAAAAWwa4_S_PBOXMFqH1m9UGk-mFUO08RQRu&scisf=4&ct=citation&cd=-1&hl=zh-TW&scfhb=1" target="_blank">[BibTeX]</a>  

## Abstract
In this paper, we describe our approach of enabling an interactive dialogue system to recognize user emotion and sentiment in realtime. These modules allow otherwise conventional dialogue systems to have “empathy” and answer to the user while being aware of their emotion and intent. Emotion recognition from speech previously consists of feature engineering and machine learning where the first stage causes delay in decoding time. We describe a CNN model to extract emotion from raw speech input without feature engineering. This approach even achieves an impressive average of 65.7% accuracy on six emotion categories, a 4.5% improvement when compared to the conventional feature based SVM classification. A separate, CNN-based sentiment analysis module recognizes sentiments from speech recognition results, with 82.5 Fmeasure on human-machine dialogues when trained with out-of-domain data.