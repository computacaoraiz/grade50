# gradelab50

This is a small tool to be used in combination with the [CS50 automarker check50][check50] and
optionally with the [Autolab autograding program][Autolab]. This tool is a fork of **grade50**,
by Patrick Totzke (the original `grade50` tool [can be accessed here][grade50]).

It allows to grade a student's submission based on check50's json report and a given grading
scheme, and output a json report in a standard or in an Autolab format.

## Synopsis
```
usage: gradelab50 [-h] [-v] [-o {ansi,json,autojson,autojsonsb}] [-t TEMPLATE] [-V] scheme report

grade student submissions based on check50 json reports.


positional arguments:
  scheme
  report

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose
  -o {ansi,json,autojson,autojsonsb}, --output {ansi,json,autojson,autojsonsb}
                        output format
  -t TEMPLATE, --template TEMPLATE
                        jinja2 template for ansi output
  -V, --version         output version information and exit
```

## Installation

```
pip install gradelab50
```

## Grading Schemes

Are given in YAML format and have to contain a list of parts, each of which is a dictionary defining a name and a list of checks. A check is a dictionary with

- `name` a string, has to appear as check name in the check50 report file. This means our problem set has a check (python function) by that name.
- `points`, an integer, the number of points given if the check passes. Can be zero.
- `fail_comment` (optional), a string that will be added as a feedback comment in case the check fails. This may contain variables that will be replaced by the contend of the check50 check. For instance, "{log}" for the logging strings or "{cause[rationale]}" for the rationale in failing checks. This will default to "{cause[rationale]}" if not given, i.e. the short string produced by check50 on the console if the check fails.
- `pass_comment` (optional), a string that will be added as a feedback comment in case the check passes. Sometimes it is nice to say "well done for X". This will default to no comment if unset.

### Example:
```yaml
- name: "Part 1"
  checks:
    - name: caesar_exists
      points: 0
      fail_comment: "Caesar.java was not submitted"
    - name: caesar_compiles
      points: 0
      fail_comment: "Caesar.java does not compile\n{log}"


- name: "Part 2"
  checks:
    - name: caesar_rotate_string_shift_5
      points: 2
      # no fail_comment set. This is equivalent to
      # fail_comment: {cause[rationale]}
      pass_comment: Your rotation seems to work. Well done!

    - name: caesar_many_args
      points: 2
      fail_comment: |
        Caesar does not print the right error message whe run with too many arguments (too many newlines/spaces?).
        expected was
        ---
        {cause[expected]}
        actual was
        ---
        {cause[actual]}
```


## Output

gradelab50 can output either plain text or json data for further use in scripts.

### json
use `gradlab50 -o json` to output json data.
This will be a dictionary mapping `points` and `points_possible` to the total score and total possible score, respectively.
Further, it maps `parts` to a list of dicts, each with 

- `name`
- `points`
- `points_possible`
- `comments` (a list of comment strings for all checks in this part)

### autojson
use `gradlab50 -o autojson` to output json data on Autolab format (without scoreboard).
This will be a dictionary mapping `problems` and `points` for use on Autolab autograding
program.

### autojsonsb
use `gradlab50 -o autojsonsb` to output json data on Autolab format (with scoreboard).
This will be a dictionary mapping `problems` and `points`, with a `scoreboard` points
for each problem and `total points`.

### text
Textual output is the default. It is based on the above and the default template (see `gradelab50/templates/default.jinja2`).
You can pass any other jinja2 template as by means of the `--template` option.
This way one can easily generate for example latex sources that can be compiled into pdf feedback files for students.



[check50]: https://github.com/cs50/check50
[Autolab]: https://github.com/autolab/Autolab
[grade50]: https://github.com/pazz/grade50
