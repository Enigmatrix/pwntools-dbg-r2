# pwntools-dbg-r2
A pip package that lets pwntools use r2 as a debugger


## Install
`pip install pwntools-dbg-r2`

## How to use

### New instance everytime
```python
from pwn import *
from r2dbg import *
p = r2dbg('/bin/ls')
...
```

### Existing r2 instance
1. Run ```. `!r2-session <port>` ``` inside the r2 instance
2. Specify r2port when debugging:
```python
from pwn import *
from r2dbg import *
p = r2dbg('/bin/ls', r2port=<port>)
...
```
## Options
Same options as [pwnlib.gdb.debug](http://docs.pwntools.com/en/stable/gdb.html#pwnlib.gdb.debug)

