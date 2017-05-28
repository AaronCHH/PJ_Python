
# Creating an IPython Notebook programatically


```python
import nbformat as nbf
```


```python
nb = nbf.v4.new_notebook()
```

This notebook will simply have three cells that read `print 0`, `print 1`, etc:


```python
text = "This is an auto-generated notebook."
code = "1+2"

nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code) ]
```

Next, we write it to a file on disk that we can then open as a new notebook.

Note: This should be as easy as: `nbf.write(nb, fname)`, but the current api is a little more verbose and needs a real file-like
object.


```python
fname = 'test.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)
```

This notebook can be run at the command line with:

    ipython -c '%run test.ipynb'

Or you can open it [as a live notebook](test.ipynb).
