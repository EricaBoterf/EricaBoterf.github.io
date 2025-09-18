---
layout: default
title: Portfolio
permalink: /portfolio/
---

# Portfolio

{% if site.projects and site.projects.size > 0 %}
<h2 class="text-2xl font-bold mt-4">Featured Projects</h2>
<ul class="mt-6 space-y-6">
  {% for project in site.projects %}
    <li class="p-4 rounded border hover:border-brand transition">
      <h2 class="text-xl font-semibold"><a href="{{ project.url }}">{{ project.title }}</a></h2>
      {% if project.description %}<p class="text-gray-700">{{ project.description }}</p>{% endif %}
      {% if project.tech %}<p class="text-sm text-gray-500">Tech: {{ project.tech | join: ", " }}</p>{% endif %}
      {% if project.link %}<a class="text-blue-600 hover:underline" href="{{ project.link }}" target="_blank" rel="noopener">GitHub →</a>{% endif %}
    </li>
  {% endfor %}
</ul>
{% endif %}

<h2 class="text-2xl font-bold mt-12">All GitHub Repositories</h2>

{% assign gh = site.github %}
{% if gh and gh.public_repositories %}
  {% assign all_repos = gh.public_repositories
     | where_exp: "r", "r.owner.login == 'EricaBoterf'"
     | where_exp: "r", "r.fork == false"
     | sort: "pushed_at" | reverse %}
  {% if all_repos and all_repos.size > 0 %}
  <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-3 mt-6">
    {% for repo in all_repos %}
      <article class="border rounded-xl p-4 shadow-sm hover:shadow transition">
        <h3 class="text-xl font-semibold mb-1"><a href="{{ repo.html_url }}" target="_blank" rel="noopener">{{ repo.name }}</a></h3>
        {% if repo.description %}<p class="text-sm text-gray-700 mb-3">{{ repo.description }}</p>{% endif %}
        <p class="text-sm mb-2">⭐ {{ repo.stargazers_count }} · 🍴 {{ repo.forks_count }}{% if repo.language %} · {{ repo.language }}{% endif %}{% if repo.archived %} · 📦 Archived{% endif %}</p>
        <p class="text-xs text-gray-600 mb-3">Updated {{ repo.pushed_at | date: "%b %-d, %Y" }}</p>
        {% if repo.homepage %}<a class="inline-block text-sm underline" href="{{ repo.homepage }}" target="_blank" rel="noopener">Live demo</a>{% endif %}
      </article>
    {% endfor %}
  </div>
  {% else %}
    <p class="mt-4"><em>No public repositories found for @EricaBoterf.</em></p>
  {% endif %}
{% else %}
  <p class="mt-4"><em>GitHub data not available at build time. See steps below.</em></p>
{% endif %}
