# Usage

`py3html` has very simple usage simple as html.

### Getting Starting

After installing now import `py3html`.

```python
{!./tests/test_py3html.py[ln:1]!}
```

### Basic usage

```python
{!./tests/test_py3html.py[ln:4-7]!}
```

### More complex usage

```python
{!./tests/test_py3html.py[ln:9-15]!}
```

### Html escape usage

```python
{!./tests/test_py3html.py[ln:18-22]!}
```

### Attributes usage

```python
{!./tests/test_py3html.py[ln:25-30]!}
```

### Usage for `add` method, to create dynamic content

```python
{!./tests/test_py3html.py[ln:33-64]!}
```

### Create new element

```python
{!./tests/test_py3html.py[ln:73-79]!}
```

### Create new element and update its html process methods

#### Preprocess

Runs at first

```python
{!./tests/test_py3html.py[ln:82-90]!}
```

#### On process

Runs when its element processed

```python
{!./tests/test_py3html.py[ln:93-101]!}
```

#### Post process

Runs when last tag appended

```python
{!./tests/test_py3html.py[ln:104-112]!}
```

### Sample new element usage

This is a new element sample

```python
{!./tests/test_py3html.py[ln:115-130]!}
```
