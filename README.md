# blogpost_editor

<img src="blogging-team-rocket-still.jpg" width="250" height="188" align="right" alt="Jessie, James, and Meowth from Team Rocket are on their laptops" loading="eager">

> For when an IDE or Markdown editor doesn't quite cut it.

This is a [Marimo notebook](https://marimo.io/) that functions as a blog post editor.

It works best in app mode with a grid layout to mimic the UI of a minimalist post editor but you can follow the usual flow in edit mode too. I use [Astro](https://astro.build/) for my website so I built this to make blog editing more visual. It comes with a section to add my metadata and the body text, view a preview (which renders the Markdown), and when I click the "Post" button, it generates an MD file with all the correct Markdown (so far)

## How to use

```
marimo edit blogpost_editor.py
```

## Preview

![the app in all its glory with sections for adding metadata, body text, and a preview of what you've written](Screenshot%202025-04-18%20at%2009.39.00.png)

## Why did I make this

After reading about [Vincent Warmerdam's cool blog post editor made with Flask](https://koaning.io/posts/a-flask-app-to-help-me-write-blogposts/), I tried it myself. But I soon realised that my version didn't work as well and I know nothing about Flask so rather than debug someone else's concept, I'd make my own. I use [Sublime Text](https://www.sublimetext.com/) normally but I've also tried [Obsidian](https://obsidian.md/) and other Markdown editors in the past. This was a nice idea because it gives more immediate feedback after I've written something rather than saving and switching to my browser (which doesn't always update immediately).

## Things I could do

- At the moment the blog editor just saves the Markdown file in the directory that your notebook sits in so I will add a file browser to select the folder my blog post should go in.
- This only works for regular posts but I have different post types such as shorter blogs called <span lang="pt">recortes</span>, posts that are just lists, morsels which are code-based blogs and others. I could add a dropdown of different frontmatter options as they all require unique metadata and then I won't have to manually edit anything.
