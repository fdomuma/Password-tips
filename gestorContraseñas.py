class contraseña:
    def __init__(self, __structure="", __place="", __keyword=""):
        self.__structure = __structure
        self.__place = __place
        self.__keyword = __keyword

    # Setters

    ## Private structure
    @property
    def structureSetter(self):
        return self.__structure

    @structureSetter.setter
    def structureSetter(self, structure):
        self.__structure = structure

    ## Private place
    @property
    def placeSetter(self):
        return self.__place

    @placeSetter.setter
    def placeSetter(self, place):
        self.__place = place

    ## Private keyword
    @property
    def keywordSetter(self):
        return self.__keyword

    @keywordSetter.setter
    def keywordSetter(self, keyword):
        self.__keyword = keyword


    # Getters
    @property
    def structureGetter(self):
        return self.__structure

    @property
    def placeGetter(self):
        return self.place

    @property
    def keywordGetter(self):
        return self.keyword