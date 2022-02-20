from src.core.services.ServiceDados import ServiceDados
from src.core.services.ServiceODBC import ServiceODBC

if __name__ == "__main__":
    dict_tabelas = {}

    dict_tabelas["clientes"] = []
    dict_tabelas["transacoes"] = []
    
    while True:
        print("1 - Testar conexão com banco de dados")
        print("2 - Criar estruturas de tabela no banco de dados")
        print("3 - Apagar todos as tabelas do Banco de dados\n")

        print("4 - Carregar dados via csv")
        print("5 - Apagar dados carregados")
        print("6 - Sumarizar dados carregados\n")

        print("7 - Inserir no banco de dados os dados carregados")
        print("8 - Sumarizar dados salvos no Banco de dados")
        print("9 - Apagar todos os dados do Banco de dados")

        print("10 - Sair")

        opcao = int(input())

        match opcao:
            case 1:  # Conectar banco de dados
                ServiceODBC.testConnection()
            case 2:  # Criar estruturas de tabela
                ServiceDados.criarTabelasDB()
            case 3: # Apagar todos as tabelas do Banco de dados
                ServiceODBC.dropAllTables()
            case 4:  # Carregar dados do CSV
                dict_tabelas = ServiceDados.carregarDoCSV()
            case 5:  # Apagar dados carregados
                dict_tabelas = ServiceDados.apagarDadosCarregados(dict_tabelas)
            case 6:  # Sumarizar dados carregados
                ServiceDados.Sumarizar(dict_tabelas)
            case 7:  # Inserir no banco de dados os dados carregados
                ServiceDados.inserirNasTabelasDB(dict_tabelas)
            case 8:  # Sumarizar dados salvos no Banco de dados
                ServiceDados.SumarizarDB()
            case 9:  # Apagar todos os dados do Banco de dados
                ServiceODBC.deleteAllTables()
            case 10:
                break
            case _:
                print("\nOpção inválida\n")
