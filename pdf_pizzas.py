from IPython.display import display, HTML
from xhtml2pdf import pisa

def convertir_a_pdf(input, output):

    result_file = open(output, "w+b")

    pisa_status = pisa.CreatePDF(input,dest=result_file)

    result_file.close()                

    return pisa_status.err


if __name__ == "__main__":
    pisa.showLogging()
    html = '''
        <html>
        <body>
            <img src="logo_maven_pizzas.png" width="130" height="130" align="right">
            <h1 Style="font: 21px calibri;font-weight: bold;">
                Reporte Ejecutivo. Pizzas Maven
            </h1>
                <p Style="font: 12px calibri;">
                    Podemos observar que las pizzas menos vendidas son la "Greek" de tamaño XXL,
                    con menos de 40 ventas anuales. 
                    En general, el tamaño XXL ha sido el menos pedido, siendo el más pedido  y
                    el que reporta mayores beneficios el L.
                    La pizza "Chicken Alfredo" es también de las menos populares, vendiéndose menos
                    de 200 tanto en su tamaño S como L.
                </p>
                <p>
                <img src="top_pizzas.png" width="300" height="260">
                <img src="bottom_pizzas.png" width="300" height="260">
                </p>
                <p>
                <img src="pedidos_horas.png" width="600" height="270">
                </p>
                <p Style="font: 12px calibri;">
                    Las horas de mayor actividad son el mediodía (12:00-13:00)
                    y la tarde (especialmente de 17:00 a 19:00).
                    Se podría reducir el horario para ahorrar en gastos de mantenimiento
                    y personal (de 11:00 a 22:00), sin una reducción significativa en las ventas.

                    En la siguiente página se encuentra un desglose semanal de las
                    porciones de ingredientes necesarias.
                </p>
                <p>
                <img src="los15.png">
                <img src="tabla_ingredientes.jpg">
                </p>

        </body>
        </html>
        '''
    convertir_a_pdf(html, 'report.pdf')

    