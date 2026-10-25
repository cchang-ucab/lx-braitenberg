from typing import Tuple

import numpy as np
# Vehículo de Braitenberg que EVITA los patos:
# si hay un pato a la izquierda, el motor izquierdo acelera y el robot gira a la derecha
# (y al revés si el pato está a la derecha).


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    
    #res[:, shape[1]  // 2 :] = -1                  # mitad DERECHA frena el motor izquierdo
    
    # Zona de peligro, lado DERECHO: mitad de abajo, del 50% al 75% del ancho
    res[shape[0] // 3 :, shape[1] // 2 : shape[1] * 3 // 4] = -1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
     
    #res[:, : shape[1]  // 2] = -1                  # mitad IZQUIERDA frena el motor derecho
    
    # Zona de peligro, lado IZQUIERDO: mitad de abajo, del 25% al 50% del ancho
    res[shape[0] // 3 :, shape[1] // 4 : shape[1] // 2] = -1
    return res
