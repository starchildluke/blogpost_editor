import marimo

__generated_with = "0.12.10"
app = marimo.App(
    width="medium",
    layout_file="layouts/blogpost_editor.grid.json",
)


@app.cell
def _():
    import marimo as mo
    from datetime import datetime
    import json
    return datetime, json, mo


@app.cell
def _(mo):
    form = mo.ui.form(
        mo.md('''
        ## Frontmatter (metadata)

        {title}

        {description}

        {pub_date}

        {tags}
        ''')
    .batch(
        title=mo.ui.text(label="Title:", full_width=True),
        description=mo.ui.text(label="Description:", full_width=True),
        pub_date=mo.ui.date(label="Publish date:"),
        tags=mo.ui.text(label="Tags:", full_width=True)
    ),clear_on_submit=True
    )

    form
    return (form,)


@app.cell
def _(mo):
    body = mo.ui.text_area(debounce=False)

    mo.vstack([
        mo.md('## Body text'),
        body
    ])

    return (body,)


@app.cell
def _(form):
    frontmatter = f"""
    ---
    title: {form.value['title']}
    description: {form.value['description']}
    published: true
    pubDate: {form.value['pub_date'].strftime('%d %b %Y')}
    tags: {form.value['tags'].split(', ')}
    ---
    """
    return (frontmatter,)


@app.cell
def _(frontmatter):
    frontmatter
    return


@app.cell
def _(body, mo):
    body_preview = mo.callout(mo.md(body.value))
    post_button = mo.ui.button(label="Post")

    mo.vstack([
        mo.md('## Post preview'),
        body_preview,
        post_button
    ])


    return body_preview, post_button


@app.cell
def _(body, frontmatter, mo, post_button):
    mo.stop(not post_button.value)

    post_text = f"""{frontmatter.strip()}
    {body.value}
    """

    with open('testpost.md', 'w') as f:
        f.write(post_text)
    return f, post_text


if __name__ == "__main__":
    app.run()
