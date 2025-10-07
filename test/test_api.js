// -----------------------------------------------------------
// Nerea Aguilar Fóres
// Desarrollado con Mocha + Request
// Verifica la comunicación con la API en Plesk
// -----------------------------------------------------------
import assert from "assert";
import request from "request";

const BASE_URL = "https://nagufor.upv.edu.es/app.php";

describe("API de Medidas", () => {

    //Prueba a insertar una medida
  it("POST /medida inserta una medida válida", (done) => {
    const data = { tipo: 11, medicion: 25.5 };
    request.post(
      {
        url: `${BASE_URL}/medida`,
        json: data,
      },
      (err, res, body) => {
        assert.strictEqual(res.statusCode, 200);
        done();
      }
    );
  });

  //Prueba a obtener la última medida
  it("GET /medida/ultima devuelve una medida", (done) => {
    request.get(`${BASE_URL}/medida/ultima`, (err, res, body) => {
      assert.strictEqual(res.statusCode, 200);
      const data = JSON.parse(body);
      assert.ok(data.medicion !== undefined);
      done();
    });
  });

});
