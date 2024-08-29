import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import '../public/css/sb-admin-2.min.css';
import { createPinia } from 'pinia';

const app = createApp(App);
const pinia = createPinia();
app.use(pinia);
app.use(router);  
app.mount('#app');
