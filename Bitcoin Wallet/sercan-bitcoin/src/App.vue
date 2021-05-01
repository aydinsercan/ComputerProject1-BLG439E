<template>
  <div id="app">
      <div class="grid-container">    
          <Header/>
          <router-view></router-view>
      </div>
  </div>
</template>

<script>

//import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header'


export default {
  name: 'App',
  components: {
    Header
  }
}
</script>


<style>
</style>
