<?php
//-------------------------------------------------------------
// Nerea Aguilar Forés
// API REST para recibir y consultar medidas
//-------------------------------------------------------------

header("Content-Type: application/json");
require_once 'logica.php';

$method = $_SERVER['REQUEST_METHOD'];
$path = $_SERVER['REQUEST_URI'];


// POST → Inserta una nueva medida
if ($method === 'POST' && strpos($path, '/medida') !== false) {
    $input = json_decode(file_get_contents('php://input'), true);

    // Validar datos recibidos
    if (!isset($input['tipo']) || !isset($input['medicion'])) {
        http_response_code(400);
        echo json_encode(["error" => "Datos incompletos"]);
        exit;
    }

    // Añadir medida y devolver resultado
    $res = anyadirMed($input['tipo'], $input['medicion']);
    echo json_encode($res);
}

// GET → Devuelve la última medida guardada
elseif ($method === 'GET' && strpos($path, '/medida/ultima') !== false) {
    $ultima = ultimaMed();
    if ($ultima) {
        echo json_encode($ultima);
    } else {
        http_response_code(404);
        echo json_encode(["error" => "No hay medidas"]);
    }
}

// Rutas no válidas
else {
    http_response_code(404);
    echo json_encode(["error" => "Ruta no encontrada"]);
}
?>
