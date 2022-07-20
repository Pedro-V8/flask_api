import psycopg2

'''class PostgreSQL():
    def init(self, usuario, senha, host, porta, banco):
        import psycopg2

        self._usuario = usuario
        self._senha = senha
        self._host = host
        self._porta = porta
        self._banco = banco

        try:
            self._conexao = psycopg2.connect(dbname=self._banco,
                                       user=self._usuario,
                                       password=self._senha,
                                       host=self._host,
                                       port=self._porta,
                                       connect_timeout=10)
            self._cur = self._conexao.cursor()
            print("CONEXÂO ESTABELECIDA COM {}".format(self._banco))

        except Exception as e:
            print("DB CONNECTION - FALHA AO CONECTAR COM O BANCO - ERRO: {}".format(e))
            return'''


class DBConnet:
    def __init__(self , databse , user , passw , host):
        self.database = databse
        self.user = user
        self.password = passw
        self.host = host
        self.port = "5432"
        self.conn = self.connection()
        self.cursor = self.conn.cursor()

    def connection(self):
        try:
            conn = psycopg2.connect(
                    database = self.database , 
                    user=self.user ,
                    password=self.password, 
                    host=self.host, 
                    port= self.port
                )
            print(" * CONEXÃO ESTABELECIDA COM {}".format(self.database))
            return conn
        except Exception  as err:
            print("ERRO NA CONEXÃO: {}".format(err))

    def search(self , cmd):
        data_result = []
        campos_tuple = ('id'  ,'hash' , 'title' , 'genre' , 'videos' , 'cover' , 'type', 'slug' , 'date_added')
        try:
            self.cursor.execute(cmd)
            result_manga = self.cursor.fetchall()
            #dict_data = dict(result_manga)
            #print(dict_data)
            for i in result_manga:
                res = dict(zip(campos_tuple, i))
                data_result.append(res)
            return data_result
        except (Exception, psycopg2.Error) as error:
            print("Failed  2to insert record into mobile table", error)


