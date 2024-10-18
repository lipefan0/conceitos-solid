class Programmer:
    def make(self):
        print('Programmer creating code')

class Seller:
    def make(self):
        print('Seller selling the product')

class Rh:
    def make(self):
        print('Human resources hiring devs')

class Company:
    def do_work(self, worker: any) -> None:
        # logica antes do make
        worker.make()

programmer = Programmer()
seller = Seller()
rh = Rh()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)