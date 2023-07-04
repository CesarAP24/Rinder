<template>
  <div>
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="item in lista" :key="item.id">
        <h2>{{ item.name }}</h2>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
    lista: Array,
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
