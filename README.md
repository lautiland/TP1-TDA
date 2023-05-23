<div class="post-content">
    <h1 class="no_toc" id="trabajo-práctico-nº-1">Trabajo Práctico n.º 1</h1>

<p>Teoría de Algoritmos 1 - 1c 2023
Trabajo Práctico 1</p>
  <p>
    <a href="https://algoritmos-rw.github.io/tda/2023-1c/tp1/">Página de la cátedra</a>
  </p>

<h2 id="lineamientos-básicos">Lineamientos básicos</h2>

<ul>
  <li>
    <p>El trabajo se realizará en forma individual.</p>
  </li>
  <li>
    <p>Se debe entregar el informe en formato pdf en el aula virtual de la materia.</p>
  </li>
  <li>
    <p>El informe debe presentar carátula con datos del autor y fecha de entrega. Debe incluir número de hoja en cada página.</p>
  </li>
  <li>
    <p>La extensión del informe no debe superar las 7 páginas + carátula + índice + referencias.</p>
  </li>
  <li>
    <p>Debe presentar codigo fuente e instrucciones de compilación y ejecución</p>
  </li>
  <li>
    <p>En caso de re-entrega, entregar un apartado con las correcciones mencionadas</p>
  </li>
</ul>

<h2 id="parte-1-maximización-del-emparejamiento">Parte 1: Maximización del emparejamiento</h2>

<p>Sean A y B dos sets de “n” puntos en el plano p=(x,y). Un punto ai=(xi,yi) de A domina a un punto bj=(xj,yj) de B si y sólo si xi≥xj y yi ≥ yj. Un emparejamiento (match) entre un punto ai de A y uno bj B es posible si ai domina a bj. Llamamos matching M a un conjunto de emparejamientos(a1 , b1 ), (a2 , b2), . . . , (ak , bk )} y su tamaño corresponde a k. Un matching es máximo si no existe otro posible mátiching con mayor cantidad de puntos.</p>

<p>Se pide para los set A y B obtener el matching máximo.</p>

<p>Resuelva:</p>

<ol>
  <li>
    <p>Proponga una estrategia greedy óptima para resolver el problema con la menor complejidad espacial y temporal posible. Justifique su optimalidad. Justifique que sea greedy.</p>
  </li>
  <li>
    <p>Explique cómo implementar algorítmicamente esa estrategia. Brinde pseudocódigo y estructuras de datos a utilizar.</p>
  </li>
  <li>
    <p>Analice complejidad temporal y espacial de su propuesta</p>
  </li>
  <li>
    <p>Programe su algoritmo y entregue dos ejemplos para su prueba.</p>
  </li>
  <li>
    <p>¿Su programa mantiene la complejidad espacial y temporal de su algoritmo? Justifique referenciando a la documentación del lenguaje si es necesario.</p>
  </li>
  <li>
    <p>Analice la solución obtenida por su algoritmo. Es única? ¿Qué podría decir sobre ella? ¿Prevalece cierto emparejamiento frente a otro posible?</p>
  </li>
</ol>

<h3 id="formato-de-los-archivos">Formato de los archivos:</h3>

<p>El algoritmo debe recibir por parámetro el valor n y luego el nombre de dos archivos que contienen los puntos. El archivo de puntos corresponde a un archivo de texto que tiene una línea por punto con sus coordenadas separadas por un espacio.</p>

<p>Ejemplo “A.txt”:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>1,3 1,6
4,8 8,5
3,6 9,4
</code></pre></div></div>

<p>El programa debe mostrar en pantalla el matching encontrado y su tamaño. Respetando el siguiente formato:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Tamaño del matching: x
Matching:

(A → B)
a1 → b1
</code></pre></div></div>

  </div>
