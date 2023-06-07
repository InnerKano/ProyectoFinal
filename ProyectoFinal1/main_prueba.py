from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from controladores.cliente_controlador import ControladorCliente
from controladores.pedido_controlador import ControladorPedido
#from controladores.main_pedido import ControladorPedido
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación Tienda Agricola")
        self.setGeometry(100, 100, 300, 150)

        # Botón para abrir la ventana de gestión de clientes
        self.boton_cliente = QPushButton("Gestión de Clientes")
        self.boton_cliente.clicked.connect(self.abrir_ventana_cliente)

        # Botón para abrir la ventana de gestión de pedidos
        self.boton_pedido = QPushButton("Gestión de Pedidos")
        self.boton_pedido.clicked.connect(self.abrir_ventana_pedido)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.boton_cliente)
        layout.addWidget(self.boton_pedido)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def abrir_ventana_cliente(self):
        ventana_cliente = ControladorCliente()
        ventana_cliente.exec_()

    def abrir_ventana_pedido(self):
        ventana_pedido = ControladorPedido()
        ventana_pedido.exec_()


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
