<?php
//-------------------------------------------------------------
// Nerea
// Contiene la lógica de negocio. Conexión y operaciones con la BBDD
//-------------------------------------------------------------

date_default_timezone_set('Europe/Madrid');

// Inicializa la base de datos y crea la tabla si no existe
function init_db() {
    $db = new SQLite3('datos.db');
    $db->exec('CREATE TABLE IF NOT EXISTS datosMedidas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo INTEGER,
        medicion REAL,
        fecha TEXT
    )');
    return $db;
}

// Añade una nueva medida a la base de datos
// Parámetros: tipo (int), medicion (float)
// Devuelve: array con los datos insertados
function anyadirMed($tipo, $medicion) {
    $db = init_db();
    $stmt = $db->prepare('INSERT INTO datosMedidas (tipo, medicion, fecha) VALUES (:tipo, :medicion, :fecha)');
    $stmt->bindValue(':tipo', $tipo, SQLITE3_INTEGER);
    $stmt->bindValue(':medicion', $medicion, SQLITE3_FLOAT);
    $stmt->bindValue(':fecha', date('Y-m-d H:i:s'), SQLITE3_TEXT);
    $stmt->execute();

    // Corfrima el guardado
    return [
        "id" => $db->lastInsertRowID(),
        "tipo" => $tipo,
        "medicion" => $medicion,
        "fecha" => date('Y-m-d H:i:s')
    ];
}

// Consulta la última medida registrada
// Devuelve: array con la última medida o null si no hay datos
function ultimaMed() {
    $db = init_db();
    $result = $db->query('SELECT * FROM datosMedidas ORDER BY id DESC LIMIT 1');
    $row = $result->fetchArray(SQLITE3_ASSOC);
    return $row ? $row : null;
}
?>
