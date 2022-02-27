# Markdown-Placeholder

> Placeholder extension for markdown ~~it seems to be text placeholder extension~~

use `^number$` as default stub symbol
> number is positive integer

## usage

`python main.py main.md content [-o output][-i]`

-i : In-place modification
-o : Specify the output file(output to console as default)

```bash
$ python main.py demo/README.md demo/content.txt -o demo/rel.md # save result to rel.md
$ python main.py demo/README.md demo/content.txt -i # write result back
```
