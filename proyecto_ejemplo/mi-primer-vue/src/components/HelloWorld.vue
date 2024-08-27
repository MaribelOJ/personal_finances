<template>

    <!-- <p>{{ message }} </p>
    <button @click="updateMessage">Actualizar Mensaje</button> -->
    <div class="col-12 col-sm-6 col-md-3">
      <div class="card">
        <img src="../assets/logo.png" class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">{{msg}}</h5>
          <p class="card-text">{{texto}}</p>
          <a href="#" class="btn btn-primary">{{texto_enlace}}</a>
        </div>
      </div>
    </div>
</template>

<script>
// import { ref } from 'vue';
// export default {
//   setup() {
//     const message = ref("Estamos aprendiendo Fundamentos de vue");
//     const updateMessage = () => {
//       message.value = "¡Mensaje Actualizado!";
//     };
//     return {message, updateMessage}
//   }
// }

export default {
  name: "App",
  props: {
    msg: String,
    texto: String,
    texto_enlace: String
  },
};
</script>
