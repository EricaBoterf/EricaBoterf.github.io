---
layout: default
title: Contact
permalink: /contact/
---

# Contact Me 📬

Fill out the form below to reach me directly:

<form action="https://formspree.io/f/xandkjvq" method="POST" accept-charset="UTF-8" class="space-y-4">
  <!-- Redirect to your Thank You page after a successful submit -->
  <input type="hidden" name="_next" value="{{ '/thankyou/' | absolute_url }}">
  <!-- Optional: customize email subject -->
  <input type="hidden" name="_subject" value="New message from portfolio site">
  <!-- Honeypot (spam protection) – keep hidden -->
  <input type="text" name="_gotcha" class="hidden" tabindex="-1" autocomplete="off">

  <label class="block">
    <span class="text-gray-700">Your Name</span>
    <input type="text" name="name" class="mt-1 block w-full border p-2 rounded" required>
  </label>

  <label class="block">
    <span class="text-gray-700">Your Email</span>
    <input type="email" name="_replyto" class="mt-1 block w-full border p-2 rounded" required>
  </label>

  <label class="block">
    <span class="text-gray-700">Message</span>
    <textarea name="message" rows="5" class="mt-1 block w-full border p-2 rounded" required></textarea>
  </label>

  <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
    Send
  </button>
</form>
