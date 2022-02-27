# Markdown-Placeholder

> markdown 占位符拓展 ~~从处理方式来看 似乎是文本占位符拓展了~~

使用 `^number$` 作为默认占位符
> number 是正整数
> 内容文本与占位符按行对应 如 `^0$` 对应文本第一行

## 使用

`python main.py holder.file content [-o output][-i]`

-i : 原地修改
-o : 指定输出文件(默认输出到控制台)

## 示例

```bash
$ python main.py demo/README.md demo/content.txt -o demo/rel.md # 将结果存储到 rel.md 中
$ python main.py demo/README.md demo/content.txt -i # 将结果回写到 README.md 中
```
