from denite.base.source import Base

import subprocess


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'man'
        self.kind = 'man'

        self.__cmd = ['man', '-k']

    def gather_candidates(self, context):
        word = context['input']

        if len(word) == 0:
            word = self._get_arg(context, 0, default='.')

        command = self.__cmd
        command.append(word)

        process = subprocess.run(
            command,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )

        if process.returncode != 0:
            return []

        candidates = process.stdout.split("\n")
        candidates = [{'word': result, 'addr': result, 'kind': 'man'} for result in candidates]

        return candidates

    @staticmethod
    def _get_arg(context, idx, default):
        args = context['args']
        argc = len(args)

        if argc <= idx:
            return default

        arg = args[idx]

        if arg is None or arg == '':
            return default

        return arg
