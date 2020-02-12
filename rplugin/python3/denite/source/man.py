from denite.base.source import Base

import subprocess


class Source(Base):
    SEARCH_TYPE_SWITCH = {
        'desc' : '--apropos',
        'name' : '--whatis',
    }

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'man'
        self.kind = 'man'

    def gather_candidates(self, context):
        word = context['input']

        if len(word) == 0:
            word = self._get_arg(context, 0, default='.')

        sections = self._get_arg(context, 1, default=None)

        if word != '.':
            search_type = self._get_arg(context, 2, default='desc')
            assert(search_type in self.SEARCH_TYPE_SWITCH.keys())
        else:
            search_type = 'desc'

        command = ['man', self.SEARCH_TYPE_SWITCH[search_type]]
        command.append(word)

        if sections:
            command += ['--section', sections]

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
