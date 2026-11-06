# Calculator

A small interactive command-line calculator written in Python. Enter arithmetic expressions at the prompt; enter `q`, `quit`, or `exit` to close it.

## Features

- Addition, subtraction, multiplication, and division
- Floor division (`//`), remainder (`%`), and powers (`**`)
- Parentheses and positive or negative numbers
- Safe expression parsing without Python's `eval`
- Clear errors for unsupported input and arithmetic errors

Example session:

```text
Calculator: enter an expression, or 'q' to quit.
> (12 + 8) / 4
5.0
> 2 ** 5
32
> q
Goodbye!
```

## Run It

Requirements: Python 3.13 or newer and [uv](https://docs.astral.sh/uv/).

From the project directory, install the locked dependencies and start the calculator:

```powershell
uv sync
uv run python main.py
```

If `uv` is not installed, install it with `py -m pip install uv`, then run the commands above.

## Try These Inputs

```text
2 + 3 * 4
(10 - 4) / 2
-3 ** 2
1 / 0
hello
q
```

The calculator follows Python arithmetic precedence. Errors are displayed without closing the session. Only numeric arithmetic expressions are accepted.

## Project Guide

See [instruction.md](instruction.md) for a step-by-step introduction to project planning, Git, and publishing this project to GitHub.
