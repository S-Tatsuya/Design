class Observer:
    def changed(self, chainring, cog):
        self._chainring = chainring
        self._cog = cog
