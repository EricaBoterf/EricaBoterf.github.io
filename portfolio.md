---
layout: default
title: Portfolio
permalink: /portfolio
---

# Portfolio
<ul class="mt-6 space-y-6">
  {% for project in site.projects %}
    <li class="p-4 rounded border hover:border-brand transition">
      <h2 class="text-xl font-semibold">
        <a href="{{ project.url }}">{{ project.title }}</a>
      </h2>
      {% if project.description %}
        <p class="text-gray-700">{{ project.description }}</p>
      {% endif %}
      {% if project.tech %}
        <p class="text-sm text-gray-500">Tech: {{ project.tech | join: ", " }}</p>
      {% endif %}
      {% if project.link %}
        <a class="text-blue-600 hover:underline" href="{{ project.link }}" target="_blank">GitHub →</a>
      {% endif %}
    </li>
  {% endfor %}
</ul>

{% for project in site.projects %}
- [{{ project.title }}]({{ project.url }}) — {{ project.summary }}
{% endfor %}
