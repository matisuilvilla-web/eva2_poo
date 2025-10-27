class Departamento:

    def __init__(self, idDepartamento=None, nombre_depto="", gerente_id=None):
        self._idDepartamento = idDepartamento
        self._nombre_depto = nombre_depto
        self._gerente_id = gerente_id

    @property
    def id_departamento(self):
        return self._idDepartamento

    @id_departamento.setter
    def id_departamento(self, value):
        self._idDepartamento = value

    @property
    def nombre_depto(self):
        return self._nombre_depto

    @nombre_depto.setter
    def nombre_depto(self, value):
        self._nombre_depto = value

    @property
    def gerente_id(self):
        return self._gerente_id

    @gerente_id.setter
    def gerente_id(self, value):
        self._gerente_id = value