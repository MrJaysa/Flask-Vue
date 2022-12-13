<script setup>
import Main from "./components/Main.vue";
import Side from "./components/Side.vue";
</script>

<template>
  <header>
    <img
      alt="Vue logo"
      class="logo"
      src="./assets/flask-vue.png"
      width="250"
      height="150"
    />

    <div class="wrapper">
      <Main msg="Flask + Vue!" />
    </div>
  </header>

  <main>
    <Side />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
  border-radius: 10px;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
