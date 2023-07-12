import { createRouter, createWebHistory } from "vue-router";
import RindYourLove from "../views/RindYourLove.vue";
import SideBar from "../components/SideBar.vue";

const routes = [
  {
    path: "/",
    name: "RindYourLove",
    components: {
      default: RindYourLove,
      sidebar: SideBar,
    },
  },
  {
    path: "/login",
    name: "LoginForm",
    components: {
      default: import("../views/LoginView.vue"),
    },
  },
  {
    path: "/register",
    name: "RegisterForm",
    components: {
      default: import("../views/RegisterView.vue"),
    },
  },
  {
    path: "/profile",
    name: "Profile",
    components: {
      default: import("../views/ProfileView.vue"),
    },
  },
  {
    path: "/messages",
    name: "Messages",
    components: {
      default: import("../views/MensajesView.vue"),
    },
  },
  {
    path: "/plans",
    name: "Plans",
    components: {
      default: import("../views/PlanesView.vue"),
    },
  },
  {
    path: "/soporte",
    name: "Soporte",
    components: {
      default: import("../views/SoporteView.vue"),
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
