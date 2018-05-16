---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## 2018
<b>[Mem2Seq: Effectively Incorporating Knowledge Bases into End-to-End Task-Oriented Dialog Systems](https://jasonwu0731.github.io/publications/Mem2Seq)</b> <br>
Andrea Madotto* , <b>Chien-Sheng Wu*</b>, Pascale Fung. ACL 2018. 

## 2017
<b>[A Study of AI Population Dynamics with Million-agent Reinforcement Learning]</b>


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
