// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./_layouts/**/*.html",
    "./_includes/**/*.html",
    "./*.{html,md}",
    "./_posts/**/*.md",
    "./_projects/**/*.md",
    "./_site/**/*.html",
  ],
  theme: { extend: {} },
  plugins: [],
};
