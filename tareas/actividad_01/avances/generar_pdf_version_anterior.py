from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, total_pages_count=None):
        super().__init__()
        self.total_pages_count = total_pages_count

    def header(self):
        if self.page_no() == 1:
            return
            
        # Header text
        self.set_font("helvetica", "B", 12)
        self.set_text_color(25, 45, 95)  # Dark blue
        self.cell(0, 10, "TRABAJO PRÁCTICO / AVANCE INSTITUCIONAL N° 1", border=0, align="L", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "B", 18)
        self.cell(0, 10, "Contexto, Modelo de Gestión y Gobernanza", border=0, align="L", new_x="LMARGIN", new_y="NEXT")
        
        # Line
        self.set_draw_color(25, 45, 95)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        if self.page_no() == 1:
            return
            
        self.set_y(-15)
        self.set_font("helvetica", "I", 10)
        self.set_text_color(128, 128, 128)
        current_page = self.page_no() - 1
        total = self.total_pages_count if self.total_pages_count else "{nb}"
        self.cell(0, 10, f"Planeamiento y Control de las Organizaciones - Avance 1: CURZAS", 0, 0, "L")
        self.set_x(10)
        self.cell(0, 10, f"Página {current_page} de {total}", 0, 0, "R")


def build_pdf(total_pages=None):
    pdf = PDF(total_pages_count=total_pages)
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- COVER PAGE ---
    pdf.set_font("helvetica", "B", 16)
    pdf.set_text_color(25, 45, 95)
    pdf.cell(0, 8, "UNIVERSIDAD NACIONAL DEL COMAHUE", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(200, 150, 50)
    pdf.cell(0, 8, "COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS)", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10)
    pdf.set_draw_color(25, 45, 95)
    pdf.set_line_width(1)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)
    
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "PLANEAMIENTO Y CONTROL DE LAS ORGANIZACIONES", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(25, 45, 95)
    pdf.multi_cell(0, 10, "Avance 1: Contexto, Modelo de Gestión y Gobernanza", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 14)
    pdf.set_text_color(50, 100, 150)
    pdf.cell(0, 10, "Análisis Institucional sobre el CURZAS (UNCo)", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(25)
    
    # Metadata for cover
    pdf.set_text_color(0, 0, 0)
    metadata = [
        ("Alumno:", "Héctor Daniel Ayarachi Fuentes"),
        ("Carrera:", "Licenciatura en Recursos Humanos"),
        ("Institución:", "Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)"),
        ("Sede Académica:", "Viedma, Provincia de Río Negro"),
        ("Marco Teórico:", "Cao & Blutman, Abal Medina, Oszlak"),
        ("Año Académico:", "2026")
    ]
    
    for label, value in metadata:
        pdf.set_font("helvetica", "B", 11)
        pdf.cell(45, 8, label, border=0)
        pdf.set_font("helvetica", "", 11)
        pdf.cell(0, 8, value, border=0, new_x="LMARGIN", new_y="NEXT")
        
    pdf.ln(40)
    pdf.set_draw_color(200, 200, 200)
    pdf.set_line_width(0.2)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)
    
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 10, "Viedma, Río Negro - República Argentina", align="C", new_x="LMARGIN", new_y="NEXT")

    # --- CONTENT PAGES ---
    pdf.add_page() # Page 2
    
    # Metadata block again for page 2 header
    metadata_page2 = [
        ("Alumno:", "Héctor Daniel Ayarachi Fuentes"),
        ("Organización:", "Complejo Universitario Regional Zona Atlántica y Sur (CURZAS) - UNCo"),
        ("Ubicación:", "Sede Viedma, Provincia de Río Negro, Argentina"),
        ("Marco Teórico:", "H. Cao & G. Blutman, J. M. Abal Medina, O. Oszlak")
    ]
    pdf.set_text_color(0, 0, 0)
    for label, value in metadata_page2:
        pdf.set_font("helvetica", "B", 10)
        pdf.cell(35, 6, label, border=0)
        pdf.set_font("helvetica", "", 10)
        pdf.cell(0, 6, value, border=0, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)

    # --- Section 1 ---
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(25, 45, 95)
    pdf.cell(0, 10, "1. Identificación y Marco Institucional de la Organización", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    text_sec1 = """El objeto de estudio del presente trabajo es el Complejo Universitario Regional Zona Atlántica y Sur (CURZAS), unidad académica dependiente de la Universidad Nacional del Comahue (UNCo), asentada en la ciudad de Viedma, Provincia de Río Negro. Su estatus institucional responde al mandato constitucional de autonomía y autarquía universitaria (Art. 75 inc. 19 de la Constitución Nacional Argentina y Ley de Educación Superior N° 24.521).

Su marco de creación y funcionamiento se encuentra regido por el Estatuto de la Universidad Nacional del Comahue (Ordenanza N° 470/1993 y sus modificatorias), que establece la estructura organizativa, los órganos co-gobernados de decisión y las misiones fundamentales de docencia, investigación y extensión universitaria.

MISIÓN Y FUNCIONES INSTITUCIONALES
El CURZAS tiene como misión institucional la generación, formación y democratización del conocimiento científico, técnico y humanístico en el territorio de la Patagonia Norte y la Línea Sur rionegrina. Su estructura organizativa combina áreas académicas, departamentos docentes, secretarías administrativas (Académica, de Investigación, de Extensión y de Gestión Administrativa) y órganos de gobierno colegiados."""
    pdf.multi_cell(0, 6, text_sec1.replace('—', '-').replace('“', '"').replace('”', '"'), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # --- Section 2 ---
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(25, 45, 95)
    pdf.cell(0, 10, "2. Identificación del Modelo de Administración Predominante", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    text_sec2 = """Para analizar el modelo de administración del CURZAS, se coteja la realidad institucional con la tipología teórica provista por Cao y Blutman (2019) y Abal Medina (2014). Según Cao y Blutman (2019), el modelo burocrático tradicional se enfoca en la formalidad de los procesos, la separación estricta de jerarquías y el apego a la norma legal. En contraste, la Nueva Gestión Pública (NGP) introducida en los años 90 busca flexibilizar estas estructuras, orientando la gestión hacia los resultados y el usuario como "cliente" de la administración.

A. Rasgos del Modelo Burocrático Tradicional (Weberiano) - PREDOMINANTE
El análisis empírico demuestra la prevalencia estructural de la Burocracia Tradicional Weberiana. En primer lugar, la toma de decisiones normativo-administrativas responde a una Estructura Jerárquica y Centralizada fijada estatutariamente (Decanato -> Secretarías -> Direcciones -> Departamentos). En segundo lugar, rige un fuerte Principio de Legalidad y Procedimentalismo: todo acto administrativo debe encuadrarse estrictamente en resoluciones o reglamentos vigentes, supeditando la discrecionalidad a expedientes regulados. Finalmente, la gestión de personal se rige por un Estatuto del Personal y Carrera Administrativa rígida mediante Convenios Colectivos de Trabajo que garantizan estabilidad y concursos de oposición.

B. Elementos Híbridos de la Nueva Gestión Pública (NGP)
A pesar del predominio burocrático, se identifican rasgos procedimentales e instrumentales de la NGP, impulsados por la modernización. Existe una Descentralización Operativa, ya que el CURZAS posee autonomía de gestión presupuestaria a través de su Consejo Directivo. Asimismo, se observa una Orientación al Usuario/Estudiante, evidente en la digitalización de trámites a través del sistema SIU-Guaraní y ventanillas únicas.

Conclusión: El CURZAS presenta un Modelo Burocrático Tradicional Fuertemente Formalizado con Hibridación Instrumental de NGP."""
    pdf.multi_cell(0, 6, text_sec2.replace('—', '-').replace('“', '"').replace('”', '"'), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # --- Section 3 ---
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(25, 45, 95)
    pdf.cell(0, 10, "3. Análisis de Mecanismos de Rendición de Cuentas (Accountability)", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    text_sec3 = """Tomando las dimensiones desarrolladas por Guillermo O'Donnell y sintetizadas por Abal Medina (2014), la rendición de cuentas puede dividirse conceptualmente en tres ejes: la accountability horizontal (donde agencias estatales controlan a otras agencias del mismo Estado), la vertical (donde la ciudadanía ejerce premio o castigo mediante elecciones) y la social (mecanismos de la sociedad civil para exigir transparencia e información). El CURZAS presenta mecanismos estructurados en estos tres ejes:"""
    pdf.multi_cell(0, 6, text_sec3.replace('—', '-').replace('“', '"').replace('”', '"'), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    # Table using HTML
    html_table = """
    <table border="1" width="100%">
        <thead>
            <tr bgcolor="#192d5f" color="#ffffff">
                <th width="20%"><b>Tipo de Accountability</b></th>
                <th width="45%"><b>Mecanismos Vigentes</b></th>
                <th width="35%"><b>Evidencia Normativa</b></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Horizontal</td>
                <td>Auditoría Interna UNCo, AGN y SIGEN. Control institucional entre órganos.</td>
                <td>Informes de auditoría, Ley 24.156.</td>
            </tr>
            <tr>
                <td>Vertical</td>
                <td>Elecciones periódicas para renovar autoridades. Cogobierno.</td>
                <td>Estatuto General UNCo, Calendario Electoral.</td>
            </tr>
            <tr>
                <td>Social</td>
                <td>Publicación de datos presupuestarios, licitaciones y nóminas.</td>
                <td>Portal de Transparencia, Ley 27.275.</td>
            </tr>
        </tbody>
    </table>
    """
    pdf.write_html(html_table)
    pdf.ln(5)

    # --- Section 4 ---
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(25, 45, 95)
    pdf.cell(0, 10, "4. Evaluación de Gobernanza Pública Inteligente (Según Oszlak)", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    text_sec4 = """Siguiendo los desarrollos teóricos de Oscar Oszlak (2020) sobre el tránsito desde el Gobierno Electrónico hacia el "Estado Inteligente" y la Gobernanza Algorítmica, se procedió a evaluar la presencia de automatización e Inteligencia Artificial en la organización.

A. Digitalización e Interoperabilidad Administrativa (Fase Pre-Inteligente)
El CURZAS ha completado de manera satisfactoria la fase de digitalización burocrática mediante la implementación obligatoria del sistema SUDOCU y el ecosistema SIU. Esto permite trazabilidad, firmas digitales y gestión transparente.

B. Análisis: Algoritmos e IA en RR.HH.
¿Cuenta el área con normativas vigentes sobre la incorporación de algoritmos o software predictivo en la selección o monitoreo de personal?
Respuesta: Inexistencia de Sistemas Algorítmicos Predictivos. Oszlak (2020) señala que la gobernanza algorítmica implica el uso de tecnologías disruptivas y automatizadas para la toma de decisiones. Si el CURZAS implementara esto en RR.HH., significaría utilizar IA para filtrar perfiles o evaluar el desempeño predictivamente. Sin embargo, esto no ocurre y se encuentra bloqueado por una Garantía de Control Humano y Paritario: el concurso público se rige 100% por jurados y comisiones paritarias integradas por personas humanas, conforme lo estipulan los Convenios Colectivos de Trabajo. Esto demuestra que la ausencia de IA no responde solo a barreras tecnológicas, sino a protecciones institucionales y sindicales tradicionales.

Estado Actual: El organismo se ubica en un estadio de Digitalización Avanzada de Trámites, muy distante de una Gobernanza Algorítmica en materia de recursos humanos."""
    pdf.multi_cell(0, 6, text_sec4.replace('—', '-').replace('“', '"').replace('”', '"'), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # --- Section 5 ---
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(25, 45, 95)
    pdf.cell(0, 10, "5. Conclusión Sintética", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    text_sec5 = """El CURZAS constituye un modelo claro de administración pública universitaria donde se conjuga una matriz burocrática tradicional garante de derechos laborales, con herramientas de la Nueva Gestión Pública orientadas a la transparencia y digitalización. La incorporación de la Inteligencia Artificial (Estado Inteligente propuesto por Oszlak) permanece como una asignatura pendiente, fuertemente regulada y limitada por los mecanismos constitucionales y paritarios vigentes."""
    pdf.multi_cell(0, 6, text_sec5.replace('—', '-').replace('“', '"').replace('”', '"'), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # --- Bibliografia ---
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(25, 45, 95)
    pdf.cell(0, 10, "Bibliografía y Fuentes Consultadas", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(0, 0, 0)
    bibliografia = [
        "- Cao, H. y Blutman, G. (2019). Continuidades y rupturas en las ideas sobre reforma y modernización del Estado. INAP.",
        "- Abal Medina, J. M. (2014). Manual de Administración Pública. Buenos Aires: Ariel. Capítulos 1 y 5.",
        "- Oszlak, O. (2020). El Estado en la era exponencial: Tecnologías disruptivas y gestión pública. INAP.",
        "- Universidad Nacional del Comahue (1993/2023). Estatuto de la UNCo.",
        "- Leyes Nacionales y CCT: Leyes N° 24.521 y N° 27.275; CCT Decretos 366/06 y 1246/15."
    ]
    for item in bibliografia:
        pdf.set_x(10)
        pdf.multi_cell(0, 6, item.replace('—', '-').replace('“', '"').replace('”', '"'), new_x="LMARGIN", new_y="NEXT")

    return pdf

# First pass to get total pages
temp_pdf = build_pdf()
total_content_pages = temp_pdf.page_no() - 1

# Second pass to generate final PDF with correct total pages
final_pdf = build_pdf(total_pages=total_content_pages)
final_pdf.output("Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")
print("PDF generado con éxito.")
