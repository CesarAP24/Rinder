import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
// import SideBar from "./components/SideBar.vue";

createApp(App).use(store).use(router).mount("#app");
