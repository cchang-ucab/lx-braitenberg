from typing import Tuple

import numpy as np
# Vehículo de Braitenberg que EVITA los patos:
# si hay un pato a la izquierda, el motor izquierdo acelera y el robot gira a la derecha
# (y al revés si el pato está a la derecha).


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    # TODO define left matrix
    # La mitad izquierda de la imagen activa el motor izquierdo
    # Todas las filas (:), columnas desde el inicio hasta la mitad del ancho (shape[1] // 2): mitad izquierda = 1
    res[:, : shape[1] // 2] = -1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    # TODO define right matrix
    # La mitad derecha de la imagen activa el motor derecho
    # Todas las filas (:), columnas desde la mitad del ancho (shape[1] // 2) hasta el final: mitad derecha = 1
    res[:, shape[1] // 2 :] = -1
    return res
