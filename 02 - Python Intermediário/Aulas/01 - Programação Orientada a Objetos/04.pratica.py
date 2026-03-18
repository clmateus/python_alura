# Exercícios
# 1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
# 2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
# 3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Nome do titular: {self.titular} | Saldo: {self.saldo}'
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def ativar_conta(self):
        self._ativo = not self._ativo

pessoa1 = ContaBancaria('João da Silva', 1000)
pessoa1.ativar_conta()

pessoa2 = ContaBancaria('Maria dos Santos', 3000)

print(pessoa1, pessoa1.ativo)
print(pessoa2.titular)

# 6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
# 7 - Crie um método de classe para a conta ClienteBanco.
class ClienteBanco:
    clientes = []

    def __init__(self, a, b, c, d, e):
        self.a = str(a)
        self.b = str(b)
        self.c = str(c)
        self.d = str(d)
        self.e = str(e)
        ClienteBanco.clientes.append(self)

    @classmethod
    def listar_clientes(cls):
        print(f'{"Nome do Cliente".ljust(20)} | {"Tipo da Conta".ljust(15)} | {"Data de Nascimento".ljust(20)} | {"Endereço".ljust(20)} | {"Documento".ljust(10)}')
        for i in cls.clientes:
            print(f'{i.a.ljust(20)} | {i.b.ljust(15)} | {i.c.ljust(20)} | {i.d.ljust(20)} | {i.e.ljust(10)}')

cliente1 = ClienteBanco(1,2,3,4,5)
cliente2 = ClienteBanco(6,7,8,9,0)
cliente3 = ClienteBanco('a','b','c','d','e')

ClienteBanco.listar_clientes()