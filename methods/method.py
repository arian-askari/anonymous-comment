import abc

class Method(abc.ABC):
    @abc.abstractmethod
    def dataset_generator(self):
        pass

    @abc.abstractmethod
    def privacy_measures(self):
        pass

    @abc.abstractmethod
    def utility_loss1(self):
        pass

    @abc.abstractmethod
    def utility_loss2(self):
        pass