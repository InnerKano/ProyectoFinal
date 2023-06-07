from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
from crud.CRUD import Pedido as CRUD
from PyQt5.QtCore import QObject


class ControladorPedido(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Pedidos")
        self.setGeometry(100, 100, 400, 300)

        # Elementos de la interfaz
        self.boton_crear_pedido = QPushButton("Crear Pedido")
        self.boton_buscar_pedido = QPushButton("Buscar Pedido")
        self.boton_pagar_pedido = QPushButton("Pagar Pedido")
        self.boton_actualizar_pedido = QPushButton("Actualizar Pedido")
        self.boton_eliminar_pedido = QPushButton("Eliminar Pedido")
        self.boton_productos_control = QPushButton("Productos Control")
        self.boton_antibioticos = QPushButton("Antibioticos")
        self.boton_confirmar_buscar_pedido = QPushButton("Confirmar")
        self.boton_confirmar_pagar_pedido = QPushButton("Confirmar")
        self.boton_confirmar_actualizar_pedido =  QPushButton("Confirmar")
        self.boton_confirmar_eliminar_pedido = QPushButton("Confirmar")
        self.boton_confirmar_crear_pedido = QPushButton("Confirmar")

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.boton_crear_pedido)
        layout.addWidget(self.boton_buscar_pedido)
        layout.addWidget(self.boton_pagar_pedido)
        layout.addWidget(self.boton_actualizar_pedido)
        layout.addWidget(self.boton_eliminar_pedido)
        self.setLayout(layout)

        # Conexiones de los botones
        self.boton_crear_pedido.clicked.connect(self.mostrar_opciones_pedido)
        self.boton_buscar_pedido.clicked.connect(self.mostrar_campos_buscar_pedido)
        self.boton_pagar_pedido.clicked.connect(self.mostrar_campos_pagar_pedido)
        self.boton_actualizar_pedido.clicked.connect(self.mostrar_campos_actualizar_pedido)
        self.boton_eliminar_pedido.clicked.connect(self.mostrar_campos_eliminar_pedido)

        # Atributo input_cedula
        self.input_cedula = QLineEdit()
        self.input_fecha = QLineEdit()
        self.input_id_pedido = QLineEdit()
        self.input_ica = QLineEdit()
        self.input_antibiotico = QLineEdit()

        self.widgets_dinamicos = []

    def mostrar_opciones_pedido(self):
        self.limpiar_campos2()

        # Agregar botones de opciones
        self.boton_productos_control = QPushButton("Productos Control")
        self.boton_productos_control.clicked.connect(self.mostrar_campos_productos_control)

        self.boton_antibioticos = QPushButton("Antibióticos")
        self.boton_antibioticos.clicked.connect(self.mostrar_campos_antibioticos)

        layout = self.layout()
        layout.addWidget(self.boton_productos_control)
        layout.addWidget(self.boton_antibioticos)

    def mostrar_campos_productos_control(self):
        self.opcion_seleccionada = 1  # Almacenar la opción seleccionada
        self.limpiar_campos2()

        nombres_columnas, productos = CRUD.leer_productos_control()
        nombres_columnas_str = "    |".join(nombres_columnas)

        dialog = QDialog()
        dialog.setWindowTitle("Productos de Control")
        dialog.setGeometry(100, 100, 600, 400)

        table = QTableWidget()
        table.setColumnCount(len(nombres_columnas))
        table.setHorizontalHeaderLabels(nombres_columnas)

        table.setRowCount(len(productos))
        for i, fila in enumerate(productos):
            for j, dato in enumerate(fila):
                item = QTableWidgetItem(str(dato))
                table.setItem(i, j, item)
        layout = QVBoxLayout()
        # Agregar campo de entrada de cédula
        self.label_cedula = QLabel("Cédula:")
        self.input_cedula = QLineEdit()
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)

        # Agregar campo de entrada de fecha
        self.label_fecha = QLabel("Fecha:")
        self.input_fecha = QLineEdit()
        layout.addWidget(self.label_fecha)
        layout.addWidget(self.input_fecha)

        self.label_ica = QLabel("Registro ICA:")
        self.input_ica = QLineEdit()
        layout.addWidget(self.label_ica)
        layout.addWidget(self.input_ica)

        self.boton_confirmar_crear_pedido = QPushButton("Confirmar")
        self.boton_confirmar_crear_pedido.clicked.connect(self.confirmar_crear_pedido)
        layout.addWidget(self.boton_confirmar_crear_pedido)

        
   
        layout.addWidget(table)
        dialog.setLayout(layout)
        dialog.exec_()



    def mostrar_campos_antibioticos(self):
        self.opcion_seleccionada = 2  # Almacenar la opción seleccionada
        self.limpiar_campos2()

        nombres_columnas, antibioticos = CRUD.leer_antibioticos()
        nombres_columnas_str = "    |".join(nombres_columnas)

        dialog = QDialog()
        dialog.setWindowTitle("Antibióticos")
        dialog.setGeometry(100, 100, 600, 400)

        table = QTableWidget()
        table.setColumnCount(len(nombres_columnas))
        table.setHorizontalHeaderLabels(nombres_columnas)

        table.setRowCount(len(antibioticos))
        for i, fila in enumerate(antibioticos):
            for j, dato in enumerate(fila):
                item = QTableWidgetItem(str(dato))
                table.setItem(i, j, item)

        layout = QVBoxLayout()

        # Agregar campo de entrada de cédula
        self.label_cedula = QLabel("Cédula:")
        self.input_cedula = QLineEdit()
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)

        # Agregar campo de entrada de fecha
        self.label_fecha = QLabel("Fecha:")
        self.input_fecha = QLineEdit()
        layout.addWidget(self.label_fecha)
        layout.addWidget(self.input_fecha)

        self.label_antibiotico = QLabel("Nombre completo del antibiótico:")
        self.input_antibiotico = QLineEdit()
        layout.addWidget(self.label_antibiotico)
        layout.addWidget(self.input_antibiotico)

        self.boton_confirmar_crear_pedido = QPushButton("Confirmar")
        self.boton_confirmar_crear_pedido.clicked.connect(self.confirmar_crear_pedido)
        layout.addWidget(self.boton_confirmar_crear_pedido)

        layout.addWidget(table)
        dialog.setLayout(layout)
        dialog.exec_()




    
    def mostrar_campos_buscar_pedido(self):
        self.limpiar_campos()
        self.label_cedula = QLabel("Cédula:")
        self.input_cedula = QLineEdit()
        self.boton_confirmar_buscar_pedido = QPushButton("Confirmar")
        self.boton_confirmar_buscar_pedido.clicked.connect(self.buscar_pedido)

        self.widgets_dinamicos.extend([self.label_cedula, self.input_cedula, self.boton_confirmar_buscar_pedido])

        layout = self.layout()
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)
        layout.addWidget(self.boton_confirmar_buscar_pedido)

    def mostrar_campos_pagar_pedido(self):
        self.limpiar_campos()
        self.label_id_pedido = QLabel("ID del Pedido:")
        self.input_id_pedido = QLineEdit()
        self.boton_confirmar_pagar_pedido = QPushButton("Confirmar")
        self.boton_confirmar_pagar_pedido.clicked.connect(self.pagar_pedido)

        layout = self.layout()
        layout.addWidget(self.label_id_pedido)
        layout.addWidget(self.input_id_pedido)
        layout.addWidget(self.boton_confirmar_pagar_pedido)

    def mostrar_campos_actualizar_pedido(self):
        self.limpiar_campos()
        self.label_id_pedido = QLabel("ID del Pedido:")
        self.input_id_pedido = QLineEdit()
        self.label_cedula = QLabel("Cédula:")
        self.input_cedula = QLineEdit()
        self.label_fecha = QLabel("Fecha:")
        self.input_fecha = QLineEdit()
        self.boton_confirmar_actualizar_pedido = QPushButton("Confirmar")
        self.boton_confirmar_actualizar_pedido.clicked.connect(self.actualizar_pedido)

        layout = self.layout()
        layout.addWidget(self.label_id_pedido)
        layout.addWidget(self.input_id_pedido)
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)
        layout.addWidget(self.label_fecha)
        layout.addWidget(self.input_fecha)
        layout.addWidget(self.boton_confirmar_actualizar_pedido)

    def mostrar_campos_eliminar_pedido(self):
        self.limpiar_campos()
        self.label_id_pedido = QLabel("ID del Pedido:")
        self.input_id_pedido = QLineEdit()
        self.boton_confirmar_eliminar_pedido = QPushButton("Confirmar")
        self.boton_confirmar_eliminar_pedido.clicked.connect(self.eliminar_pedido)

        layout = self.layout()
        layout.addWidget(self.label_id_pedido)
        layout.addWidget(self.input_id_pedido)
        layout.addWidget(self.boton_confirmar_eliminar_pedido)


    def confirmar_crear_pedido(self):
        opcion = self.opcion_seleccionada  # Obtener la opción almacenada
        cedula = int(self.input_cedula.text())
        fecha = self.input_fecha.text()

        if opcion == 1:
            producto_ica = self.input_ica.text()
            CRUD.crear_pedido(producto_ica, cedula, fecha, opcion)
        elif opcion == 2:
            antibiotico = self.input_antibiotico.text()
            CRUD.crear_pedido(antibiotico, cedula, fecha, opcion)

        QMessageBox.information(self, "Éxito", "Pedido creado exitosamente.")
        self.limpiar_campos2()

    def limpiar_campos2(self):
        layout = self.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


        
    def buscar_pedido(self):
        cedula = self.input_cedula.text()

        if cedula:
            nombres_columnas, pedido = CRUD.buscar_pedido(cedula)
            nombres_columnas_str = "    |".join(nombres_columnas)
            if pedido:
                dialog = QDialog()
                dialog.setWindowTitle("Pedido Encontrado")
                dialog.setGeometry(100, 100, 600, 400)

                table = QTableWidget()
                table.setColumnCount(len(nombres_columnas))
                table.setHorizontalHeaderLabels(nombres_columnas)

                table.setRowCount(len(pedido))
                for i, fila in enumerate(pedido):
                    for j, dato in enumerate(fila):
                        item = QTableWidgetItem(str(dato))
                        table.setItem(i, j, item)

                layout = QVBoxLayout()
                layout.addWidget(table)
                dialog.setLayout(layout)
                dialog.exec_()
            else:
                QMessageBox.information(self, "No se encontró el pedido", "No se encontró ningún pedido para la cédula especificada.")
            
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete el campo de cédula.")

    def pagar_pedido(self):
        id_pedido = self.input_id_pedido.text()

        if id_pedido:
            CRUD.pagar_pedido(id_pedido)
            QMessageBox.information(self, "Éxito", "Pedido pagado exitosamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete el campo de ID del pedido.")

    def actualizar_pedido(self):
        id_pedido = self.input_id_pedido.text()
        cedula = self.input_cedula.text()
        fecha = self.input_fecha.text()

        if id_pedido and cedula and fecha:
            CRUD.actualizar_pedido(id_pedido, cedula, fecha)
            QMessageBox.information(self, "Éxito", "Pedido actualizado exitosamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")


    def eliminar_pedido(self):
        id_pedido = self.input_id_pedido.text()

        if id_pedido:
            CRUD.eliminar_pedido(id_pedido)
            QMessageBox.information(self, "Éxito", "Pedido eliminado exitosamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete el campo de ID del pedido.")

    def limpiar_campos(self):
        # Eliminar los widgets dinámicos de la interfaz
        layout = self.layout()
        for widget in self.widgets_dinamicos:
            layout.removeWidget(widget)
            widget.deleteLater()
        self.widgets_dinamicos = []
        
        # Restaurar los botones originales
        self.layout().addWidget(self.boton_crear_pedido)
        self.layout().addWidget(self.boton_buscar_pedido)
        self.layout().addWidget(self.boton_pagar_pedido)
        self.layout().addWidget(self.boton_actualizar_pedido)
        self.layout().addWidget(self.boton_eliminar_pedido)

        # Limpiar la lista de widgets dinámicos
        self.widgets_dinamicos = []

        # Establecer los atributos como None, excepto self.input_cedula
        self.input_fecha = None
        self.input_id_pedido = None
        self.input_ica = None
        self.input_antibiotico = None