<template>
  <div class='home-frame' style=''>
    <img
      src="@/assets/iconlarge.png"
    />
    <div>

      <a class="button-add" v-on:click="navigateEczane()">
          Eczane girişi
      </a>
      <div class="lower-page-div">
        <h1>Thanks for working with us!</h1>
      </div>
      <img class="tobb-etu-png" src="@/assets/tobbetu.png"/>   

    
    </div>  

    <!-- <SearchCar/> -->
  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
    
  },
  methods: {
    navigateEczane() {
      this.$router.push({
          name: 'EczanePage',
          params: {
          }
      });     
    },

  }
}

</script>

<style>

.lower-page-div {
  position: absolute;
  bottom: 0;
  text-align: center;
  padding-left: 38%;
}
.tobb-etu-png {
  position: absolute;
  bottom: 0;
  width: 5%;
  right: 0;
}

</style>
