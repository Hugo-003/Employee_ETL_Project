import pandas as pd
import numpy as np
import logging
from data_schema.empleados_schema import schemaEmpleado

class Empleados:
    def __init__(self, config, logger):
        self._config = config
        self._logger = logger
        self.input_df = None

    def leer_datos(self, df):
        self.input_df = df

        self._logger.logger.log(logging.INFO, "Imprimir primeros registros")
        print(self.input_df.head(5))

    def rellenar_columnas(self, df):
        self.input_df = df

        for index, row in self.input_df.iterrows():
            if row[schemaEmpleado.FULL_TIME.value] > row[schemaEmpleado.PART_TIME.value]:
                self.input_df.at[index, schemaEmpleado.PART_TIME.value] = \
                    1 - self.input_df.at[index, schemaEmpleado.FULL_TIME.value]

            elif row[schemaEmpleado.PART_TIME.value] > row[schemaEmpleado.FULL_TIME.value]:
                self.input_df.at[index, schemaEmpleado.FULL_TIME.value] =\
                    1 - self.input_df.at[index, schemaEmpleado.PART_TIME.value]

            else:
                np.random.seed(0)
                random_num = np.random.rand()
                self.input_df.at[index, schemaEmpleado.FULL_TIME.value] = random_num
                self.input_df.at[index, schemaEmpleado.PART_TIME.value] = \
                    1 - self.input_df.at[index, schemaEmpleado.FULL_TIME.value]

        print(self.input_df.head(4))


    def bonus_adicional(self, df):
        self.input_df = df
        self.input_df['bonus_adicional'] = self.input_df[schemaEmpleado.SALARY.value]*0.1/12

        print (self.input_df.head(5))

    def aumento_salario(self, df):
        self.input_df = df
        self.input_df['diferencia_años'] = self.input_df[schemaEmpleado.YEARS_IN_THE_COMPANY.value] - \
                                            self.input_df[schemaEmpleado.PRIOR_YEARS_EXPERIENCE.value]

        self.input_df['aumento_salario'] = 0
        condition = self.input_df['diferencia_años'] > self.input_df[schemaEmpleado.PRIOR_YEARS_EXPERIENCE.value]*0.2
        self.input_df.loc[condition, 'aumento_salario'] = self.input_df[schemaEmpleado.SALARY.value] * 0.15

        self.input_df.drop(columns=['diferencia_años'], inplace=True)

        print(self.input_df.head(5))

    def clave_compuesta(self, df):
        self.input_df = df

        self.input_df['clave_compuesta'] = self.input_df[schemaEmpleado.COMPANY.value].astype(str) + \
                                           '_' + self.input_df[schemaEmpleado.DEPARTMENT.value].astype(str) + \
                                           '_' + self.input_df[schemaEmpleado.EMPLOYEE_ID.value].astype(str)
        print(self.input_df.head(5))



    def rangos_edad(self, df):
        self.input_df = df
        self.input_df['rango_edad'] = ''
        self.input_df.loc[(self.input_df[schemaEmpleado.AGE.value] >= 0) & (self.input_df[schemaEmpleado.AGE.value] <= 20), 'rango_edad'] = '0-20'
        self.input_df.loc[(self.input_df[schemaEmpleado.AGE.value] > 20) & (self.input_df[schemaEmpleado.AGE.value] <= 30), 'rango_edad'] = '21-30'
        self.input_df.loc[(self.input_df[schemaEmpleado.AGE.value] > 30) & (self.input_df[schemaEmpleado.AGE.value] <= 40), 'rango_edad'] = '31-40'
        self.input_df.loc[(self.input_df[schemaEmpleado.AGE.value] > 40) & (self.input_df[schemaEmpleado.AGE.value] <= 50), 'rango_edad'] = '41-50'
        self.input_df.loc[(self.input_df[schemaEmpleado.AGE.value] > 50) & (self.input_df[schemaEmpleado.AGE.value] <= 60), 'rango_edad'] = '51-60'
        self.input_df.loc[(self.input_df[schemaEmpleado.AGE.value] > 60) & (self.input_df[schemaEmpleado.AGE.value] <= 70), 'rango_edad'] = '61-70'
        self.input_df.loc[self.input_df[schemaEmpleado.AGE.value] > 70, 'rango_edad'] = '+70'

        print(self.input_df.head(5))

    def diferencia_edad_y_edad_promdeio(self, df):
        self.input_df = df

        grupos = self.input_df.groupby([schemaEmpleado.COMPANY.value, schemaEmpleado.DEPARTMENT.value])
        edad_promedio_por_grupo = grupos[schemaEmpleado.AGE.value].mean().reset_index()
        edad_promedio_por_grupo.rename(columns={schemaEmpleado.AGE.value: 'edad_promedio'}, inplace=True)
        self.input_df = pd.merge(self.input_df, edad_promedio_por_grupo,
                                 on=[schemaEmpleado.COMPANY.value, schemaEmpleado.DEPARTMENT.value],how='left')
        self.input_df['diferencia_edad_promedio'] = self.input_df[schemaEmpleado.AGE.value] - self.input_df['edad_promedio']

        print(self.input_df.head(5))


class EmpresaGlasses(Empleados):
    def __init__(self, config, logger):
        super().__init__(config, logger)

class EmpresaCheerper(Empleados):
    def __init__(self, config, logger):
        super().__init__(config, logger)

class EmpresaPear(Empleados):
    def __init__(self, config, logger):
        super().__init__(config, logger)






