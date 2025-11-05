import logging
from src.logger.logger import Logger
from src.config.config import Config
from src.empleados.empleados import *
from data_schema.empleados_schema import schemaEmpleado
import pandas as pd

def main():

    config = Config()

    logger = Logger(log_path=config.log_path, log_level=config.log_level, log_identifier=config.etl_name,
                    show_file_line=False)
    # Executing the ETL
    try:
        logger.start_log()
        # Primero compruebo las empresas que hay, para poder crear las clases hijas
        input_df = pd.read_csv(config.input_csv)
        print(input_df[schemaEmpleado.COMPANY.value].unique())

        empleados_obj = Empleados(config=config, logger=logger)
        glasses_obj = EmpresaGlasses(config=config, logger=logger)
        cheerper_obj = EmpresaCheerper(config=config, logger=logger)
        pear_obj = EmpresaPear(config=config, logger=logger)

        while True:
            logger.logger.log(logging.INFO, "1) Cargar CSV e imprimir 5 lineas (obligatorio hacer primero, para cargar datos)")
            logger.logger.log(logging.INFO, "2) Rellenar columnas full_time ")
            logger.logger.log(logging.INFO, "3) Asignar bonus adicional")
            logger.logger.log(logging.INFO, "4) Calcular aumento de salario")
            logger.logger.log(logging.INFO, "5) Crear clave compuesta")
            logger.logger.log(logging.INFO, "6) Clasificación de la edad por rangos")
            logger.logger.log(logging.INFO, "7) Diferencia entre la edad y la edad promedio")
            logger.logger.log(logging.INFO, "8) Guardar todas las operaciones en un solo DataFrame")
            logger.logger.log(logging.INFO, "9) Salir")


            opc = int(input("Insertar opción"))

            if opc == 1:
                print('empleados df:')
                empleados_obj.leer_datos(input_df)
                print('glasses df:')
                glasses = input_df[input_df[schemaEmpleado.COMPANY.value] == 'Glasses']
                glasses_obj.leer_datos(glasses)
                print('cheerper df:')
                cheerper = input_df[input_df[schemaEmpleado.COMPANY.value] == 'Cheerper']
                cheerper_obj.leer_datos(cheerper)
                print('pear df:')
                pear = input_df[input_df[schemaEmpleado.COMPANY.value] == 'Pear']
                pear_obj.leer_datos(pear)

            elif opc == 2:
                input_df = pd.read_csv(config.input_csv)
                empleados_obj.rellenar_columnas(df=input_df)
                # Guardar transformación (los csv que guarde serán del dataframe conjunto, no de los dataframes de cada empresa)
                input_df.to_csv(config.out_csv, index=False)

                glasses_obj.rellenar_columnas(df=glasses)
                cheerper_obj.rellenar_columnas(df=cheerper)
                pear_obj.rellenar_columnas(df=pear)

            elif opc == 3:
                input_df = pd.read_csv(config.input_csv)
                empleados_obj.bonus_adicional(df=input_df)
                input_df.to_csv(config.out_csv2, index=False)

                glasses_obj.bonus_adicional(df=glasses)
                cheerper_obj.bonus_adicional(df=cheerper)
                pear_obj.bonus_adicional(df=pear)

            elif opc == 4:
                input_df = pd.read_csv(config.input_csv)
                empleados_obj.aumento_salario(df=input_df)
                input_df.to_csv(config.out_csv3, index=False)

                glasses_obj.aumento_salario(df=glasses)
                cheerper_obj.aumento_salario(df=cheerper)
                pear_obj.aumento_salario(df=pear)

            elif opc == 5:
                input_df = pd.read_csv(config.input_csv)
                empleados_obj.clave_compuesta(df=input_df)
                input_df.to_csv(config.out_csv4, index=False)

                glasses_obj.clave_compuesta(df=glasses)
                cheerper_obj.clave_compuesta(df=cheerper)
                pear_obj.clave_compuesta(df=pear)

            elif opc == 6:
                input_df = pd.read_csv(config.input_csv)
                empleados_obj.rangos_edad(df=input_df)
                input_df.to_csv(config.out_csv5, index=False)

                glasses_obj.rangos_edad(df=glasses)
                cheerper_obj.rangos_edad(df=cheerper)
                pear_obj.rangos_edad(df=pear)

            elif opc == 7:
                input_df = pd.read_csv(config.input_csv)
                empleados_obj.diferencia_edad_y_edad_promdeio(df=input_df)
                input_df.to_csv(config.out_csv6, index=False)

                glasses_obj.diferencia_edad_y_edad_promdeio(df=glasses)
                cheerper_obj.diferencia_edad_y_edad_promdeio(df=cheerper)
                pear_obj.diferencia_edad_y_edad_promdeio(df=pear)

            elif opc == 8:
                input_df = pd.read_csv(config.input_csv)
                empleados_obj.rellenar_columnas(df=input_df)
                empleados_obj.bonus_adicional(df=input_df)
                empleados_obj.aumento_salario(df=input_df)
                empleados_obj.clave_compuesta(df=input_df)
                empleados_obj.rangos_edad(df=input_df)
                empleados_obj.diferencia_edad_y_edad_promdeio(df=input_df)

                input_df.to_csv(config.out_csv7, index=False)


            elif opc == 9:
                logger.logger.log(logging.INFO, "Has salido del programa")
                break


    except:
        logger.logger.log(logging.ERROR, "Error")
        exit(1)


    logger.logger.log(logging.INFO, "Esto es un test")
    
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

