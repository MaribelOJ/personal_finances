import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import '../public/css/sb-admin-2.min.css'

const app = createApp(App);
app.use(router);  
app.mount('#app');
