from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
from crud.CRUD import Cliente as CRUD


class ControladorCliente(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Clientes")
        self.setGeometry(100, 100, 400, 300)

        # Elementos de la interfaz
        self.label_cedula = QLabel("Cédula:")
        self.input_cedula = QLineEdit()
        self.label_nombre = QLabel("Nombre:")
        self.input_nombre = QLineEdit()
        self.boton_crear_cliente = QPushButton("Crear Cliente")
        self.boton_buscar_cliente = QPushButton("Buscar Cliente")
        self.boton_actualizar_cliente = QPushButton("Actualizar Cliente")
        self.boton_eliminar_cliente = QPushButton("Eliminar Cliente")
        

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.boton_crear_cliente)
        layout.addWidget(self.boton_buscar_cliente)
        layout.addWidget(self.boton_actualizar_cliente)
        layout.addWidget(self.boton_eliminar_cliente)
        self.setLayout(layout)

        # Conexiones de los botones
        self.boton_crear_cliente.clicked.connect(self.crear_cliente)
        self.boton_buscar_cliente.clicked.connect(self.buscar_cliente)
        self.boton_actualizar_cliente.clicked.connect(self.actualizar_cliente)
        self.boton_eliminar_cliente.clicked.connect(self.eliminar_cliente)

        

    def crear_cliente(self):
        cedula = int(self.input_cedula.text())
        nombre = self.input_nombre.text()
        cliente = CRUD.buscar_cliente(cedula)
        if cliente is None:
            CRUD.crear_cliente(cedula, nombre)
            QMessageBox.information(self, "Éxito", "Cliente creado exitosamente.")
        else:
            QMessageBox.warning(self, "Error", "El cliente ya existe.")

    def buscar_cliente(self):
        cedula = int(self.input_cedula.text())
        
        if cedula is not None:
            cliente = CRUD.buscar_cliente(cedula)
            if cliente is None:
                QMessageBox.warning(self, "Error", "No se encontró el cliente.")
            else:
                nombre_cliente = cliente[1]
                QMessageBox.information(self, "Cliente Encontrado", f"Cliente encontrado: {nombre_cliente}")
                nombres_columnas, facturas = CRUD.buscar_factura_cedula(cedula)
                if facturas:
                    dialog = QDialog()
                    dialog.setWindowTitle("Facturas del Cliente")
                    dialog.setGeometry(100, 100, 600, 400)

                    table = QTableWidget()
                    table.setColumnCount(len(nombres_columnas))
                    table.setHorizontalHeaderLabels(nombres_columnas)

                    table.setRowCount(len(facturas))
                    for i, factura in enumerate(facturas):
                        for j, dato in enumerate(factura):
                            item = QTableWidgetItem(str(dato))
                            table.setItem(i, j, item)

                    layout = QVBoxLayout()
                    layout.addWidget(table)
                    dialog.setLayout(layout)
                    dialog.exec_()
                else:
                    QMessageBox.information(self, "No se encontraron facturas", "No se encontraron facturas para el cliente.")
                
        else:
            QMessageBox.warning(self, "Error", "Digite cedula.")

    def actualizar_cliente(self):
        cedula = int(self.input_cedula.text())
        nombre = self.input_nombre.text()

        cliente = CRUD.buscar_cliente(cedula)
        if cliente is not None:
            CRUD.actualizar_cliente(cedula, nombre)
            QMessageBox.information(self, "Éxito", "Cliente actualizado exitosamente.")
        else:
            QMessageBox.warning(self, "Error", "El cliente no existe.")

    def eliminar_cliente(self):
        cedula = int(self.input_cedula.text())

        cliente = CRUD.buscar_cliente(cedula)
        if cliente is not None:
            CRUD.eliminar_cliente(cedula)
            QMessageBox.information(self, "Éxito", "Cliente eliminado exitosamente.")
        else:
            QMessageBox.warning(self, "Error", "El cliente no existe.")
