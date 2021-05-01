<template>

    <div  class="product-card">

        <div class="headWallet">
            <p >My Wallet</p>
        </div>
        

        <div class="product-info">
            <p class="product-price"> Wallet Address : {{publicKey}} </p>
            <p class="product-price"> Balance : {{balance}} </p>
        </div>

        <div class="cart-buttons"  >
                <button  @click="$router.push({name: 'sendBitcoin'})"  class="login btn btn-success sendBitcoin" href="#" variant="primary">Send bitcoin</button>
                <button  @click="$router.push({name: 'askBitcoin'})"  class="login btn btn-danger askBitcoin" variant="primary">
                    Request bitcoin
                </button>
        </div>


    </div>

</template>


<script>


export default {
    name: 'myWallet',


    data(){

        return{

            publicKey : this.$store.state.publicKey,
            balance : this.$store.state.balance

        }

    }
    ,

    methods:{

    },

    computed:{

    }

}
</script>







<style>

.headWallet{
    width: 100%;
    height: 5rem;
    background-color: rgb(238, 238, 238);
    color: rgb(39, 39, 39);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom:3rem;
    padding-top: 0.5rem;
    font-size: 3rem;
    font-weight: 600;
}

.product-card {

  font-family:'Poppins', sans-serif;   
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 2px 2px 3px 2px rgb(206, 156, 156);
  height: 35%;
  width: 70%;
}



.product-price{
    font-size: 1.7rem ;
    font-weight: 600;
    color: rgb(255, 103, 48);
    margin-bottom: 4rem;
    text-align: center;
}

@media (max-width: 1500px) {

.headWallet{
width: 100%;
height: 3.5rem;
background-color: rgb(238, 238, 238);
display: flex;
align-items: center;
justify-content: center;
margin-bottom:3rem;
font-size: 2.5rem;
}

.product-card {
   
  font-family:'Poppins', sans-serif;   
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex; /* so child elements can use flexbox stuff too! */
  flex-direction: column;
  align-items: center;
  box-shadow: 2px 2px 3px 2px rgb(206, 156, 156);
  height: 40%;
  width: 70%;
 
}


.product-price{
    font-size: 1.3rem ;
    font-weight: 600;
    color: rgb(255, 103, 48);
    margin-bottom: 2rem;
    text-align: center;
}
}

/* buttons */

.cart-buttons{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
}


.sendBitcoin{
    flex-basis: 20%;
    align-items: center;
}

.askBitcoin{
    flex-basis: 20%; 
     align-items: center;
}

.btn.buy.btn-primary{
    background-color: rgb(255, 166, 0);
    font-size: 1.rem;
}

.btn.arrange.btn-primary{
   background-color : #007bff ;
}
.btn.remove.btn-primary{
    background-color: rgb(243, 45, 45) ;
}

</style>