import re
from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'vim-auto-programming'
        self.mark = '[ap]'
        self.filetypes = []
        self.min_pattern_length = 0
        self.rank = 600
        self.ap_available = False

    def on_init(self, context):
        self.ap_available = True
        try:
            self.vim.call('autoprogramming#complete', 1, 0)
        except e:
            self.ap_available = False

    def get_complete_position(self, context):
        if self.vim.call('has', '*autoprogramming#complete'):
            self.ap_available = True
        if not self.ap_available:
            return 0
        return self.vim.call('autoprogramming#complete', 1, 0)

    def gather_candidates(self, context):
        if not self.ap_available:
            return []
        return self.vim.call('autoprogramming#complete', 0, context['input'])
