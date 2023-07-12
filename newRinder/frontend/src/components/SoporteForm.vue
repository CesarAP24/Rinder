<template>
  <div class="support-form">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <input
          type="text"
          id="nombre"
          v-model="nombre"
          required
          placeholder="Ingrese su nombre"
        />
      </div>
      <div class="form-group">
        <input
          type="text"
          id="apellido"
          v-model="apellido"
          required
          placeholder=" Ingrese su apellido"
        />
      </div>
      <div class="form-group">
        <input
          type="email"
          id="correo"
          v-model="correo"
          required
          placeholder="Ingrese su correo electrónico"
        />
      </div>
      <div class="form-group">
        <input
          type="text"
          id="telefono"
          v-model="telefono"
          required
          placeholder="Ingrese su teléfono"
        />
      </div>
      <div class="form-group">
        <select id="problema" v-model="problema" required>
          <option value="" disabled selected>Selecciona tu problema</option>
          <option value="Problema técnico">Problema técnico</option>
          <option value="Duda general">Duda general</option>
          <option value="Reportar un error">Reportar un error</option>
          <option value="Solicitud de función">Solicitud de función</option>
          <option value="Otro">Otro</option>
        </select>
      </div>
      <div class="form-group">
        <textarea
          id="descripcion"
          v-model="descripcion"
          required
          placeholder="Describe detalladamente tu problema"
        ></textarea>
      </div>
      <button type="submit">Enviar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SoporteForm",
  data() {
    return {
      nombre: "",
      apellido: "",
      correo: "",
      telefono: "",
      problema: "",
      descripcion: "",
    };
  },
  methods: {
    submitForm(event) {
      event.preventDefault();
      // Lógica para enviar el formulario
    },
  },
};
</script>

<style scoped>
.support-form {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  overflow: auto;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 400px;
  padding: 40px;
  background-color: #f5f5f5;
  box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
  margin: auto;
}

h3 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
  width: 100%;
}

label {
  font-weight: bold;
  color: #555;
}

input[type="text"],
input[type="email"],
textarea,
select {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
  font-size: 14px;
  transition: border-color 0.3s ease;
}

input[type="text"]:focus,
input[type="email"]:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: #4285f4;
  box-shadow: 0 0 0 2px rgba(66, 133, 244, 0.2);
}

textarea {
  height: 120px;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #4285f4;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #1a73e8;
}

button:focus {
  outline: none;
}
</style>
