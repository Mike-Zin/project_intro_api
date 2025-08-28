from models import Tarefa
from models import db

class TarefaController:
    
    @staticmethod
    def get_listar_tarefas():
        return Tarefa.query.all()
    
    @staticmethod
    def get_listar_tarefas_id(tarefa_id):
        pass
    
    @staticmethod
    def post_criar_tarefa(id, tarefa, concluida):
        pass
    
    @staticmethod
    def delete_remove_tarefa(self, tarefa_id: int):
        pass
    
    @staticmethod
    def put_atualizar_tarefa(self, tarefa_id:int, dados:dict):
        pass