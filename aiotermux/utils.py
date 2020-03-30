import asyncio
from typing import Tuple


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
