# TODO: Handle properly cases when it's not a trange. Just make a counter.
# TODO: Customizable look.

class progress_bar:
    def __init__(self, iterable, bar_length=20, newline=True):
        self.iterable = iterable
        self._iter = iter(iterable)
        self._done = False
        self.bar_length = bar_length
        self.newline = newline

        if hasattr(iterable, "__len__"):
            self.total = len(iterable)
        else:
            self.total = None

    def __iter__(self):
        return self

    def _display_bar(self, current: int, total = None):
        if total is None:
            # TODO
            raise NotImplementedError("Total length is unknown, cannot display progress bar.")

        progress_n = int(current / total * self.bar_length)

        bar = "█" * progress_n + "." * (self.bar_length - progress_n)
        bar_colored = f"\033[32m{bar[:progress_n]}\033[0m{bar[progress_n:]}"
        progress = f"{bar_colored} {current}/{total}"
        if self.newline:
            print(progress, flush=True)
        else:
            print("\r" + progress, end="", flush=True)

    def _on_finish(self):
        self._display_bar(self.total, self.total)
        print()

    def _on_next(self, element):
        self._display_bar(element, self.total)

    def __next__(self):
        try:
            next_ = next(self._iter)
            self._on_next(next_)
            return next_
        except StopIteration:
            if not self._done:
                self._done = True
                self._on_finish()
            raise
