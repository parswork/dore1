class parameter():
    def __init__(self) -> None:
        self._data=""
    @property
    def data(self,a):
        self._data=a
    @data.getter
    def data(self):
        return self._data