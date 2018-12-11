from pwn import *
import r2pipe

def r2dbg(args, r2script=None, r2port=None, exe=None, ssh=None, env=None, sysroot=None, **kwargs):
    r2 = r2pipe.open('http://127.0.0.1:'+str(r2port))
    p = process(args,env=env)
    r2.cmd("o dbg://"+str(p.pid))
    def load_modules():
        modules = r2.cmdj("dmmj")
        for module in modules:
            if '{mod_name:s}' == os.path.basename(module['file']):
                command = "oba {{addr:d}} {{file_name:s}}".format(file_name=module['file'], addr=module['address'])
                r2.cmd(command)
    load_modules()
    r2.cmd('ib') # Reload the buffer info
    r2.cmd("aaa;ood")
    for cmd in r2script.split('\n'):
        r2.cmd(cmd)
    pause()
    return p
