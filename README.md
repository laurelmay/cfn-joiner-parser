# CloudFormation Joiner/Parser

Are you reading old CloudFormation docs and blog posts from before
[`Fn::Sub`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-sub.html)
existed? Do you have a coworker who just really loves to keep using
[`Fn::Join`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.html)
and writes it like it's their first language? The syntax is awful to read and write, whether
in YAML or JSON. Luckily, it's pretty easy to automate creating.

## joiner.py

Pass `joiner.py` a file (or just send the data over stdin) that contains your string, and joiner
will join it with `''`. Quickly generate those long `!Join` calls for a convenient conversation.
For readability and ease of commenting, `joiner.py` only support printing in YAML. Also, for
consistency, you may only split on `''`.

```
$ echo "Wow! Your CloudFormation is really good" | joiner.py
Fn::Join:
- ''
- - W
  - o
  - w
  - '!'
  - ' '
  - Y
  - o
  - u
  - r
  - ' '
  - C
  - l
  - o
  - u
  - d
  - F
  - o
  - r
  - m
  - a
  - t
  - i
  - o
  - n
  - ' '
  - i
  - s
  - ' '
  - r
  - e
  - a
  - l
  - l
  - y
  - ' '
  - g
  - o
  - o
  - d
  - '

    '
```

## parser.py

Pass `parser.py` a file (or again, just send the data over stdin) with your long `Fn::Join` call
and `parser.py` will turn it into a beautiful string that you can actually communicate to a human
being. No CloudFormation function except `Fn::Join` is support. Only the `Fn::Join` call is
supported.

```
$ cat << EOF | ./parser.py
Fn::Join:
- ''
- - W
  - o
  - w
  - '!'
  - ' '
  - Y
  - o
  - u
  - r
  - ' '
  - C
  - l
  - o
  - u
  - d
  - F
  - o
  - r
  - m
  - a
  - t
  - i
  - o
  - n
  - ' '
  - i
  - s
  - ' '
  - r
  - e
  - a
  - l
  - l
  - y
  - ' '
  - g
  - o
  - o
  - d
  - '

    '
EOF

Wow! Your CloudFormation is really good
```

## FAQs

**Couldn't you have just used a single file and made one script with a flag to toggle the direction?**

I guess I didn't consider that while lost admiring the beauty of CloudFormation.

**Wasn't this waste of time?**

Yes.

**Did you really need to share this with the world?**

No.

**How can I use this to replace `cat(1)`?**

Put these scripts somewhere that they'll be on your path. Then put the following function at the
end of your shell's rc file.

```
cat() {
  /bin/cat "$@" | joiner.py | parser.py
}
```

## License

This work is licensed under the MIT license, that way you're free to incorporate it into whatever
work you'd like.
