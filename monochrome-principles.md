Design principles for monoochrome themes
----------------------------------------

As an ambitious side goal I'm trying to design a syntax highlighting theme that
only uses monotone colors (and formatting styles), but still manages to make
the code readable. Below are some properties that I'm trying to achieve:

- comments should be clearly secondary to the code
- other less important/boilerplace/common elements (such as types) should also
  be softer, not drawing attention
- rare token types requiring special attention (e.g. exceptions) should use
  formatting that draws attention to them
- Class and function definitions should stand apart to make high-level code
  navigation easy
- special words (builtins, predefined values such as booleans) should have some
  formatting distinguishing them from user-defined values, so that it's obvious
  when you make a typo
