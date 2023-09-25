**README - Página Web de Compras**

**Descripción General:**
Esta página web de compras proporciona a los usuarios la capacidad de buscar productos, cargar información de usuarios, solicitar productos y proporcionar detalles de envío. A continuación, se detalla cómo funcionan las principales características de la página y las URL disponibles.

**URLs de la Página:**

1. **Inicio (http://127.0.0.1:8000/AppPietra/):**
   - Página principal donde los usuarios pueden buscar productos.
   - Un campo de entrada permite a los usuarios ingresar el nombre de un producto.
   - Una vez realizada la búsqueda, se muestran los productos coincidentes y los colores disponibles para cada producto.

2. **Usuario (http://127.0.0.1:8000/AppPietra/your_u/):**
   - Aquí los usuarios pueden cargar su información de usuario.
   - Se solicita el nombre, el apellido y el correo electrónico del usuario.

3. **Solicitar Producto (http://127.0.0.1:8000/AppPietra/wishlist/):**
   - Permite a los usuarios agregar un producto a la base de datos.
   - Se solicita el nombre del artículo y su color.
   - Una vez enviado, el producto estará disponible para futuras búsquedas.

4. **Envío (http://127.0.0.1:8000/AppPietra/delivery/):**
   - Los usuarios pueden cargar detalles de envío aquí.
   - Se solicita el barrio, la calle, la altura del domicilio y una fecha para el envío del producto.

**Uso de la Página:**

- Los usuarios pueden comenzar en la página de inicio y realizar búsquedas de productos.
- Si desean comprar un producto, deben cargar su información de usuario en la página de usuario.
- Para solicitar un producto que no se encuentra en la base de datos, pueden utilizar la página de "Solicitar Producto".
- Una vez que tienen un producto en mente y su información de usuario cargada, pueden utilizar la página de envío para proporcionar detalles de entrega.

