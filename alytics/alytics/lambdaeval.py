

def prepare ( s ) :
    s = s.replace ( '__', '' )
    return s


def evaluate ( s, locals={} ) :
    s = prepare ( s )

    safe = [ 'Exception', 'None', 'True', 'False', 'abs', 'all', 'any', 'ascii', 'bin', 'callable', 'chr', 'delattr', 'dir', 'divmod', 'format', 'globals', 'hasattr', 'hash', 'hex', 'id', 'isinstance', 'issubclass', 'iter', 'len', 'locals', 'max', 'min', 'next', 'oct', 'ord', 'pow', 'repr', 'round', 'setattr', 'sorted', 'sum', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple', 'type', 'zip' ]

    from math import sin

    globals = { '__builtins__' : {
        **locals,
        **{ 'sin' : sin },
        **{ key : __builtins__[ key ] for key in __builtins__ if key in safe } }
    }

    r = eval ( s, globals, locals )

    return r



#                             Thoughts about unsafetyness of eval
# "input" blocking the output.
# "help" and "license" runs in shell the program blocking the output. "copyright" and "credits" are safe tho.
# "exec" can run import, "eval" can run __import__, and both can evaluate modified strings. "compile" is safe tho.
# "exit" and "quit" cannot be evaluated through eval but make noise in shell.
# "print" is the main function for making noise in shell.
# "open" can create and modify existing files.
# "vars" and "getattr" can be used to call class methods by string ( it is bad, see below ).
# Making __builtins__ empty does not save you from exploiting original __builtins__ ;
# this is how you can get unmodified builtins from eval :
# [ c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings' ][0]()._module.__builtins__
# To prevent this I do replace all "__"s with other characters, wich prevents you from getting __class__ from empty tuple,
# but only if you cannot get that value as dictionary key, wich can be done removing getattr and vars from __builtins__.
