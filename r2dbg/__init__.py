from pwn import *

def r2dbg(args, r2script=None, r2port=None, exe=None, ssh=None, env=None, sysroot=None, **kwargs):
    gdbscript = ""
    if r2port:
        gdbscript += "#>port="+str(r2port)+"\n"
    if r2script:
        gdbscript += '\n'.join("#r2"+c for c in r2script.split('\n'))
    return gdb.debug(args, gdbscript, exe, ssh, env, sysroot, **kwargs)

