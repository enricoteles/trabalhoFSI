
import unittest
from calculadora import fazer_conta

class TesteCalculadoraNovos(unittest.TestCase):
    def test_soma_positiva_negativa(self):
        self.assertEqual(fazer_conta(-10, 20, "+"), 10)

    def test_subtracao_resultado_negativo(self):
        self.assertEqual(fazer_conta(3, 10, "-"), -7)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(fazer_conta(99, 0, "*"), 0)

    def test_divisao_resultado_decimal(self):
        self.assertAlmostEqual(fazer_conta(5, 2, "/"), 2.5)

    def test_potencia_decimal(self):
        self.assertAlmostEqual(fazer_conta(9, 0.5, "^"), 3.0)

    def test_divisao_por_zero_invalida(self):
        self.assertIsNone(fazer_conta(10, 0, "/"))

    def test_operador_inexistente(self):
        self.assertIsNone(fazer_conta(4, 2, "//"))

    def test_texto_como_entrada(self):
        self.assertIsNone(fazer_conta("quatro", 2, "+"))

    def test_lista_como_entrada(self):
        self.assertIsNone(fazer_conta([4], 2, "-"))

    def test_tupla_como_entrada(self):
        self.assertIsNone(fazer_conta((5,), 2, "*"))

    def test_bool_como_entrada(self):
        self.assertIsNone(fazer_conta(True, 2, "+"))

    def test_soma_com_zero(self):
        self.assertEqual(fazer_conta(0, 100, "+"), 100)

    def test_subtracao_de_si_mesmo(self):
        self.assertEqual(fazer_conta(17, 17, "-"), 0)

    def test_potencia_zero_elevado_a_algo(self):
        self.assertEqual(fazer_conta(0, 5, "^"), 0)

    def test_potencia_qualquer_elevado_a_zero(self):
        self.assertEqual(fazer_conta(5, 0, "^"), 1)

    def test_float_resultado_soma(self):
        self.assertEqual(fazer_conta(0.1, 0.2, "+"), 0.30000000000000004)

    def test_multiplicacao_negativos(self):
        self.assertEqual(fazer_conta(-3, -3, "*"), 9)

    def test_potencia_com_expoente_negativo(self):
        self.assertAlmostEqual(fazer_conta(4, -1, "^"), 0.25)

    def test_operador_vazio(self):
        self.assertIsNone(fazer_conta(2, 2, ""))

    def test_entrada_nula(self):
        self.assertIsNone(fazer_conta(None, 2, "+"))

if __name__ == "__main__":
    unittest.main()
