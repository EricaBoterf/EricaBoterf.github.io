---
layout: default
title: Portfolio
permalink: /portfolio
---

# Portfolio

{% for project in site.projects %}
- [{{ project.title }}]({{ project.url }}) — {{ project.summary }}
{% endfor %}
