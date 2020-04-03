import asyncio
from typing import Tuple


def make_command(*args, **kwargs) -> str:
    """
    >>> make_command('termux-dialog', confirm={'-i': 'text hint', '-t': 'Title'})
    'termux-dialog confirm -i text hint -t Title'

    :param args:
    :param kwargs:
    :return:
    """
    head = [args[0]] if args else []
    for a, b in kwargs.items():
        head.append(a)
        if isinstance(b, dict):
            fragment = make_command(**b)
        elif isinstance(b, list):
            fragment = ' '.join(b)
        else:
            fragment = str(b)
        head.append(fragment)
    head.extend(str(s) for s in args[1:])

    return ' '.join(head)


async def run_command(cmd: str) -> Tuple[str, int]:
    """
    Run a shell command as subprocess.

    :param cmd:
    :return:
    """
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    data = f'[{cmd!r} exited with {proc.returncode}]'

    if stdout:
        data = f'{stdout.decode()}'
    if stderr:
        data = f'{stderr.decode()}'

    return data, proc.returncode
