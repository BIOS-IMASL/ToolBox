# Plantilla Latex para tesis de grado o posgrado

En la mayora de las universidades no se brindan plantillas de LaTeX ni word para los trabajos finales de grado o tesis de posgrado. Incluso en muchas instituciones los requerimientos para estos documentos (tales como tamaño de letra, márgenes, tapa, contratapa, etc.) están subespecificados o ni siquera se han definido. La idea de este template es brindar un recurso básico para escribir un documento extenso como lo es una tesis. Además el uso de LaTeX posibilita adaptar facilmente la plantilla a distintos requerimientos tales como tipo y tamaño de letra, márgenes, encabezados y pies de página, entre otros. Por otra parte, LaTeX cuenta con numerosos paquetes que brindan mayor cantidad de recursos a la hora de armar documentos, tales como [_hyperlinks_](https://en.wikibooks.org/wiki/LaTeX/Hyperlinks) , [lista de acrónimos](https://ctan.org/pkg/acronym), [grafos](http://www.texample.net/tikz/), [algoritmos](https://ctan.org/pkg/algorithm2e), etc.

Este template fue creado para una tesis de doctorado en informática presentada en la _Facultad de Ciencias Físico-Matemáticas y Naturales (FCFMyN)_ de la _Universidad Nacional de San Luis (UNSL)_. Sin embargo, con pocos cambios, se puede adaptar para generar otro tipo de documentos tales como **informes finales de carrera**, **monografas**, **reportes técnicos**, entre otros.

###**Nota** Para quienes prefieran ampliar sus conicimientos en latex se recomienda leer el siguiente documento[_La introducción no-tan-corta a LATEX2ε_](http://ctan.sharelatex.com/tex-archive/info/lshort/spanish/lshort-a4.pdf)

# Como usar
## Generar PDF
Se debe abrir el archivo .tex que está en la raiz del proyecto y ejecutar con un editor de documentos Latex tal como [TexStudio](http://texstudio.sourceforge.net/), [TexMaker](http://www.xm1math.net/texmaker/), [Kile] (https://kile.sourceforge.io/), [WinEdt](http://www.winedt.com/), etc.
Por lo general, esta plantilla funciona bien con el comando PDFLatex. 

## Estructura 
En el archivo principal se encuentran las especificaciones de paquetes utilizados, carátula, titulo y las llamadas a los documentos de cada capítulo. 
Por cada capítulo se ha definido una carpeta separada que contiene el .tex con el texto y una carpeta con las imágenes referenciadas en dicho .tex. 
Los agradecimientos, dedicatoria, resumen y appendices son estructurados y llamados de la misma forma que un capítulo.



### Instrucciones para instalación de latex (motor):
-[Linux](https://linuxconfig.org/how-to-install-latex-on-ubuntu-18-04-bionic-beaver-linux) 
Nota: Una forma de evitar posteriores instalaciones de paquetes es instalar la versión full de _texlive_

-[Windows](https://miktex.org/download)

### Instrucciones para instalación de TexStudio (editor):

-[Linux y Windows](https://www.texstudio.org/) 

Manual de [TexStudio](http://texstudio.sourceforge.net/manual/current/usermanual_en.html)
