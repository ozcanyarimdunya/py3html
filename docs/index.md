# py3html

> A very simple tool to generate html with python code.

| Project       | Tabler                                                                                   |
|---------------|------------------------------------------------------------------------------------------|
| Author        | Özcan Yarımdünya                                                                         |
| Documentation | [https://ozcanyarimdunya.github.io/py3html](https://ozcanyarimdunya.github.io/py3html)   |
| Source code   | [https://github.com/ozcanyarimdunya/py3html](https://github.com/ozcanyarimdunya/py3html) |

`py3html` is a library that you can generate html by using same tree-structure python code.

## Installation

Only `python3.9+` required, no extra dependencies.

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
        " continue!",
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
  <p>Login <small>to</small> continue!</p>
</div>
```

## Test

This project using `pytest`.

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

## LICENSE

```text
MIT License

Copyright (c) 2022 yarimdunya.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```
