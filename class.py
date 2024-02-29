class Human:
    def __init__(self,name,occuption):
        self.name= name
        self.occuption=occuption

    def do_work(self):
        if self.occuption=='tennis player':
            print(self.name,'plays tennis')
        elif self.occuption=='actor':
            print(self.name,'shoots a film')

    def speaks(self):
        print(self.name,'says How are you?')

tom= Human('tom cruise','actor')
tom.do_work()
tom.speaks()
maria = Human("mario sharappva", 'tennis player')
maria.do_work()
maria.speaks()