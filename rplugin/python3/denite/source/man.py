from denite.base.source import Base

import subprocess


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'man'
        self.kind = 'man'

        self._cmd = ['man', '-k']

    def on_init(self, context):
        pass

    def gather_candidates(self, context):
        word = context['input']

        if len(word) == 0:
            word = '.'

        command = self._cmd
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
