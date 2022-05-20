# py3html

> A very simple tool to generate html with python code.

| Project       | Tabler                                     |
|---------------|--------------------------------------------|
| Author        | Özcan Yarımdünya                           |
| Documentation | https://ozcanyarimdunya.github.io/py3html  |
| Source code   | https://github.com/ozcanyarimdunya/py3html |

`py3html` is a library that you can generate html by using same tree-structure python code.

## Installation

```shell
pip install py3html
```

## Usage

Basic usage

```python
import py3html as ph

code = ph.P("Hello, World")

code.html()
```

**Output**

```html
<p>Hello, World</p>
```

You can add more elements with attributes.

```python
import py3html as ph

code = ph.Div(
    ph.H1("Welcome", attrs={"style": "color: red"}),
    ph.A("Click here!", attrs={"href": "example.com"}),
    ph.P(
        "Login ",
        ph.Small("to"),
        " continue !",
    ),
    attrs={"class": "container"}
)

code.html()
```

**Output**

```html

<div class="container">
  <h1 style="color: red">Welcome</h1>
  <a href="example.com">Click here!</a>
  <p>Login <small>to</small> continue !</p>
</div>
```

## Test

This project using `pytest` and `pytest-cov`.

```shell
make test
```

## Documentation

**Live preview**

```shell
make serve-docs
```

**Building**

```shell
build-docs
```
