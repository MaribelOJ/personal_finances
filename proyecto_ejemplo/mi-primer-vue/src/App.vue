<template>
  <MiComponenteSlot>
    <template #header>   
      <div class="row py-5">
        <VModel></VModel>
      </div>
      <LogoSena></LogoSena>
      <MiUsuario></MiUsuario>
      <MiContador></MiContador>
      <h1>Esto es el header de mi sitio</h1>
    </template>
    <div class="row">
      <VerifyLogin></VerifyLogin>
    </div>
      <div class="row">
        <HelloWorld
          msg="Star"
          texto="This is a description for the star"
          texto_enlace="shooting star"
        />
        <HelloWorld
          msg="Moon"
          texto="This is a description for the moon"
          texto_enlace="full moon"
        />
        <HelloWorld
          msg="Sun"
          texto="This is a description for the sun"
          texto_enlace="burning sun"
        />
        <HelloWorld
          msg="Jupiter"
          texto="This is a description for Jupiter"
          texto_enlace="big Jupiter"
        />
      </div>
      
    <template #footer>
      <div class="container">
        <div class="row bg-black text-white py-4">
          <MisProductos></MisProductos>
        </div>
        <MiBoton @mensaje-enviado="mostrarMensaje" />
      </div>
    </template>
  </MiComponenteSlot>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import LogoSena from "./components/LogoSena.vue";
import MiBoton from "./components/MiBoton.vue";
import MiComponenteSlot from "./components/MiComponenteSlot.vue";
import MiContador from "./components/MiContador.vue";
import MisProductos from "./components/MisProductos.vue";
import MiUsuario from "./components/MiUsuario.vue";
import VerifyLogin from "./components/VerifyLogin.vue";
import VModel from "./components/VModel.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
    MiBoton,
    MiComponenteSlot,
    MiContador,
    MiUsuario,
    LogoSena,
    VerifyLogin,
    MisProductos,
    VModel
  },
  methods: {
    mostrarMensaje(mensaje) {
      alert(mensaje);
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
